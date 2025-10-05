#! /usr/bin/env python
import ast, keyword, re, random, json, zopfli.zlib, copy, sys, os, zipfile, glob, warnings

from code_golf_utils import *

# --- Core Utilities ---
#
UNSAFE_MODE = True


def create_template_from_function(code_string: str) -> (str, list):
    tree = ast.parse(code_string)
    variable_names = {
        node.id
        for node in ast.walk(tree)
        if isinstance(node, ast.Name)
        and node.id not in keyword.kwlist
        and node.id
        not in [
            "chain",
            "enumerate",
            "combinations",
            "product",
            "str",
            "abs",
            "exec",
            "len",
            "min",
            "max",
            "range",
            "set",
            "any",
            "filter",
            "list",
            "map",
            "sum",
            "tuple",
            "zip",
            "all",
            "sorted",
        ]
    }
    template = code_string
    for name in sorted(list(variable_names), key=len, reverse=True):
        template = re.sub(r"\b" + re.escape(name) + r"\b", f"##{name}##", template)
    return template.replace("def ##p##", "def p").replace(
        "##p##=lambda", "p=lambda"
    ).replace("##f##'", "f'").replace('##f##"', 'f"'), sorted(list(variable_names))


def get_score(code: str, examples_to_check: list) -> (int, int):
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=SyntaxWarning)
            solution_namespace = {}
            exec(code, solution_namespace)
            p_func = solution_namespace.get("p")
            for _, example in examples_to_check:
                if json.dumps(p_func(copy.deepcopy(example["input"]))) != json.dumps(
                    example["output"]
                ):
                    return 999, 999
            compressed = zopfli.zlib.compress(code.encode())
            penalty = sum(
                compressed.count(c) for c in [b"\\", b"\0", b"\n", b"\r"]
            ) + min(compressed.count(b"'"), compressed.count(b'"'))
            return len(compressed), penalty
    except Exception:
        return 998, 998


def validate_code(code: str, all_examples_to_check: list) -> tuple | None:
    """Checks code against all examples. Returns the first failing example or None."""
    if UNSAFE_MODE:
        all_examples_to_check = all_examples_to_check[:1]
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=SyntaxWarning)
            solution_namespace = {}
            exec(code, solution_namespace)
            p_func = solution_namespace.get("p")
            for i, example in all_examples_to_check:
                if json.dumps(p_func(copy.deepcopy(example["input"]))) != json.dumps(
                    example["output"]
                ):
                    return i, example  # FAILED
            return None  # PASSED
    except Exception:
        # Code fails to execute, so it's invalid. Return the first example as the failure point.
        return all_examples_to_check[0]


def find_best_code(task_id):
    # --- Setup ---
    with open(f"for_compression/task{task_id:03d}.py") as f:
        RAW_FUNCTION_STRING = "".join(f.readlines())
    task_data = load_examples(task_id)
    all_examples = list(
        enumerate(
            task_data.get("train", [])
            + task_data.get("test", [])
            + task_data.get("arc-gen", [])
        )
    )
    checked_examples = [ex for ex in all_examples if ex[0] in [0]]
    checked_example_ids = {ex[0] for ex in checked_examples}

    # --- Optimization Pipeline ---
    FUNCTION_TEMPLATE, original_vars = create_template_from_function(
        RAW_FUNCTION_STRING
    )
    print(f"Initial variables: {original_vars}\n")
    candidate_names = list("qertyuiopasdfghjklzxcbnm")

    initial_code = FUNCTION_TEMPLATE.replace("##", "")
    PAYLOAD_OVERHEAD = 60

    # --- Initial Validation ---
    print("Running initial validation against all examples...")
    if validate_code(initial_code, all_examples) is not None:
        print("FATAL: Initial raw function is incorrect. Exiting.")
        sys.exit(1)
    print("Initial code PASSED validation.")

    current_base, current_penalty = get_score(initial_code, checked_examples)
    current_total_size = PAYLOAD_OVERHEAD + current_base + current_penalty

    # Global best tracking
    global_best_code = initial_code
    global_best_base, global_best_penalty = current_base, current_penalty
    global_best_total_size = current_total_size

    # Last known good tracking
    last_known_good_code = initial_code
    last_known_good_base, last_known_good_penalty = current_base, current_penalty
    last_known_good_total_size = current_total_size

    print(
        f"Initial size: {global_best_total_size} (Base: {current_base}, Penalty: {current_penalty})\n{initial_code}\n"
        + "-" * 30
    )

    LIMIT = 8000
    REBASE_INTERVAL = 1000

    for i in range(LIMIT):
        if i > 0 and i % REBASE_INTERVAL == 0:
            print(
                f"\n--- Rebase at iter {i}: Validating global best (Size: {global_best_total_size}) ---"
            )

            failing_example = validate_code(global_best_code, all_examples)

            if failing_example:
                fail_id, fail_ex = failing_example
                print(
                    f"VALIDATION FAILED on example #{fail_id}! Reverting to last known good solution."
                )
                # Revert global best to the last one that passed
                global_best_code = last_known_good_code
                global_best_base, global_best_penalty = (
                    last_known_good_base,
                    last_known_good_penalty,
                )
                global_best_total_size = last_known_good_total_size
                print(f"Reverted to size: {global_best_total_size}")

                # Add the new failing example to the checked set if it's not already there
                if fail_id not in checked_example_ids:
                    checked_examples.append(failing_example)
                    checked_example_ids.add(fail_id)
                    print(
                        f"Added example #{fail_id} to the active test set. (Now checking {len(checked_examples)} examples)"
                    )
            else:
                print("VALIDATION PASSED. Updating last known good checkpoint.")
                # Update the checkpoint to the current global best
                last_known_good_code = global_best_code
                last_known_good_base, last_known_good_penalty = (
                    global_best_base,
                    global_best_penalty,
                )
                last_known_good_total_size = global_best_total_size

            FUNCTION_TEMPLATE, original_vars = create_template_from_function(
                global_best_code
            )
            current_mapping = {var: var for var in original_vars}
            current_base, current_penalty = get_score(
                global_best_code, checked_examples
            )  # Rescore with potentially new examples
            print(f"New rebase variables: {original_vars}\n" + "-" * 30)

        if not original_vars:
            continue

        trial_mapping = {
            var: var for var in original_vars
        }  # Start from identity map for the current template
        num_changes = random.randint(1, min(6, len(original_vars)))
        vars_to_change = random.sample(original_vars, k=num_changes)
        for var, new_name in zip(
            vars_to_change, random.sample(candidate_names, k=num_changes)
        ):
            trial_mapping[var] = new_name

        trial_code = FUNCTION_TEMPLATE
        for var in original_vars:
            trial_code = trial_code.replace(f"##{var}##", trial_mapping[var])

        trial_base, trial_penalty = get_score(trial_code, checked_examples)
        trial_total_size = PAYLOAD_OVERHEAD + trial_base + trial_penalty

        if trial_total_size < global_best_total_size:
            global_best_total_size = trial_total_size
            global_best_code = trial_code
            global_best_base, global_best_penalty = trial_base, trial_penalty
            print(
                f"\n New GLOBAL best: {global_best_total_size} (B:{global_best_base}, P:{global_best_penalty}) @{i+1} \n{trial_code}"
            )

        if (trial_base, trial_penalty) <= (current_base, current_penalty):
            is_local_improvement = (trial_base, trial_penalty) < (
                current_base,
                current_penalty,
            )
            current_base, current_penalty = trial_base, trial_penalty
            if is_local_improvement and trial_total_size > global_best_total_size:
                print(
                    f"Local improvement: {trial_total_size} (B:{trial_base}, P:{trial_penalty}) @{i+1}"
                )

    # --- Final Result ---
    print(f"\nFinal validation of best code found...")
    if validate_code(global_best_code, all_examples) is not None:
        print(
            "WARNING: The final best code failed full validation. Something may be wrong."
        )
    else:
        print("Final code PASSED validation.")

    print(
        f"\nBest score achieved: {global_best_total_size} bytes (Base: {global_best_base}, Penalty: {global_best_penalty})"
    )
    print("\nFinal optimized code:")
    return global_best_code


SUB_DIR = "./compressed"
os.makedirs(SUB_DIR, exist_ok=True)


def save_solution(task_id, code):
    raw_bytes = code.strip().encode()
    compressed = zopfli.zlib.compress(raw_bytes)
    quote = b"'" if b'"' in compressed else b'"'
    wrapper = b"#coding:L1\nimport zlib;exec(zlib.decompress(bytes(%s,'L1')))" % (
        quote + compressed + quote
    )

    use_compressed = len(wrapper) < len(raw_bytes)
    final_bytes = wrapper if use_compressed else raw_bytes

    path = os.path.join(SUB_DIR, f"task{task_id:03d}.py")
    with open(path, "wb") as f:
        f.write(final_bytes)
    print(
        f"Saved Task {task_id} solution ({'compressed' if use_compressed else 'raw'}, {len(final_bytes)} bytes)"
    )


if __name__ == "__main__":
    if len(sys.argv) > 1:
        task_ids = [int(sys.argv[1])]
    else:
        task_ids = range(1, 401)
    for task_id in task_ids:
        try:
            save_solution(task_id, find_best_code(task_id))
        except FileNotFoundError:
            print(f"Task {task_id} not completed (by us) yet")
