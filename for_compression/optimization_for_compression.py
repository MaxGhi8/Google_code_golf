#! /usr/bin/env python
import ast
import copy
import json
import keyword
import os
import random
import re
import signal
import sys
import warnings

import zopfli.zlib

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from code_golf_utils import *

# =============================
# Configuration Constants
# =============================
# These constants control the behavior of the variable renaming optimizer.
# You can tweak them to trade off speed, exploration, and stability.

# Characters (variable names) the optimizer may try when renaming.
OPT_CANDIDATE_NAMES = "qertyuiopasdfghjklzxcbnm"

# Starting rebase interval (iterations). A rebase fully validates the current best
# against the entire example set and refreshes the variable template.
OPT_REBASE_START = 500

# Factor by which the rebase interval grows after each rebase.
OPT_REBASE_GROWTH = 1.3

# Maximum number of variable name changes attempted in a single trial.
OPT_MAX_CHANGES_PER_TRIAL = 6

# Payload overhead added to compressed size + penalty to approximate transport cost.
OPT_PAYLOAD_OVERHEAD = 60

# Default total iteration cap for optimization runs (can still be overridden via function arg 'limit').
OPT_DEFAULT_LIMIT = 40000

# If True (not currently exposed), could allow skipping some examples initially more aggressively.
# Kept for potential future expansion.
OPT_UNSAFE_MODE = False


# --- Core Utilities ---

def create_template_from_function(code_string: str) -> tuple[str, list]:
    tree = ast.parse(code_string)
    variable_names = {node.id for node in ast.walk(tree) if isinstance(node, ast.Name) and node.id not in keyword.kwlist and node.id not in ['Counter', 'next', 'int', 'chain','enumerate', 'combinations', 'product', 'str', 'abs', 'exec','len', 'min', 'max', 'range', 'set','any', 'filter', 'list', 'map', 'sum', 'tuple', 'zip', 'all', 'sorted']}
    template = code_string
    for name in sorted(list(variable_names), key=len, reverse=True):
        template = re.sub(r'\b' + re.escape(name) + r'\b', f'##{name}##', template)
    return template.replace("def ##p##", "def p").replace("##p##=lambda", "p=lambda").replace("##f##'", "f'").replace('##f##"', 'f"'), sorted(list(variable_names))

def get_score(code: str, examples_to_check: list) -> tuple[int, int]:
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=SyntaxWarning)
            solution_namespace = {}
            exec(code, solution_namespace)
            p_func = solution_namespace.get('p')
            for _, example in examples_to_check:
                if json.dumps(p_func(copy.deepcopy(example['input']))) != json.dumps(example['output']):
                    return 999, 999
            compressed = zopfli.zlib.compress(code.encode())
            # compressed = zlib.compress(code.encode(), 9)
            penalty = sum(compressed.count(c) for c in [b'\\', b'\0', b'\n', b'\r']) + min(compressed.count(b"'"), compressed.count(b'"'))
            return len(compressed), penalty
    except Exception:
        return 998, 998

def validate_code(code: str, all_examples_to_check: list) -> tuple | None:
    """Checks code against all examples. Returns the first failing example or None."""
    # UNSAFE_MODE removed in refactor; keep full set here.
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=SyntaxWarning)
            signal.alarm(1)
            solution_namespace = {}
            exec(code, solution_namespace)
            p_func = solution_namespace.get('p')
            signal.alarm(0)
            
            for i, example in all_examples_to_check:
                # signal.alarm(1)
                if json.dumps(p_func(copy.deepcopy(example['input']))) != json.dumps(example['output']):
                    # signal.alarm(0)
                    return i, example # FAILED
                # signal.alarm(0)
            return None # PASSED
    except Exception:
        # Code fails to execute, so it's invalid. Return the first example as the failure point.
        return all_examples_to_check[0]

###############################
# Functional API Additions    #
###############################

def _run_variable_minimization(raw_function_code:str, task_id:int, limit:int=OPT_DEFAULT_LIMIT, unsafe:bool=False, payload_overhead:int=OPT_PAYLOAD_OVERHEAD, seed:int|None=None, verbose:bool=True):
    if seed is not None:
        random.seed(seed)
    task_data = load_examples(task_id)
    all_examples = list(enumerate(task_data.get('train', []) + task_data.get('test', []) + task_data.get('arc-gen', [])))
    # Start with one example for speed, will expand on failures (adaptive like original idea)
    checked_example_ids = {0} if all_examples else set()
    checked_examples = [ex for ex in all_examples if ex[0] in checked_example_ids]
    UNSAFE_MODE = unsafe

    FUNCTION_TEMPLATE, original_vars = create_template_from_function(raw_function_code)
    if verbose:
        print(f"Initial variables: {original_vars}\n")
    candidate_names = list(OPT_CANDIDATE_NAMES)
    initial_code = FUNCTION_TEMPLATE.replace("##","")

    if validate_code(initial_code, all_examples) is not None:
        raise ValueError("Initial code does not pass all examples for task " + str(task_id))
    if verbose:
        print("Initial code PASSED validation.")

    base, penalty = get_score(initial_code, checked_examples)
    total = payload_overhead + base + penalty

    if verbose:
        print(f"Initial size: {total} (Base: {base}, Penalty: {penalty})\n{initial_code}\n" + "-"*30)

    best_code=initial_code;best_base=base;best_penalty=penalty;best_total=total
    last_good=best_code;last_good_base=base;last_good_penalty=penalty;last_good_total=total

    REBASE_INTERVAL=OPT_REBASE_START;next_rebase=OPT_REBASE_START

    for i in range(limit):
        if i and i%next_rebase==0:
            REBASE_INTERVAL=int(REBASE_INTERVAL*OPT_REBASE_GROWTH)
            next_rebase+=REBASE_INTERVAL
            failing=validate_code(best_code,all_examples)
            if failing:
                fail_id,_=failing
                best_code=last_good;best_base=last_good_base;best_penalty=last_good_penalty;best_total=last_good_total
                if fail_id not in checked_example_ids:
                    checked_example_ids.add(fail_id)
                    checked_examples=[ex for ex in all_examples if ex[0] in checked_example_ids]
                if verbose:
                    print(f"\n[Rebase {i}] FAIL on example {fail_id}; added to active set (now {len(checked_examples)}). Reverted to size {best_total}.")
            else:
                last_good=best_code;last_good_base=best_base;last_good_penalty=best_penalty;last_good_total=best_total
                if verbose:
                    print(f"\n[Rebase {i}] Validation pass. Checkpoint updated. Current best size {best_total}.")
            FUNCTION_TEMPLATE,original_vars=create_template_from_function(best_code)
            base,penalty=get_score(best_code,checked_examples)
            if verbose:
                print(f"Rebase vars: {original_vars} | Score (Base:{base} Pen:{penalty})\n"+"-"*30)

        if not original_vars: continue
        trial_mapping={v:v for v in original_vars}
        n_changes=random.randint(1,min(OPT_MAX_CHANGES_PER_TRIAL,len(original_vars)))
        for v,new in zip(random.sample(original_vars,n_changes),random.sample(candidate_names,n_changes)):
            trial_mapping[v]=new
        trial_code=FUNCTION_TEMPLATE
        for v in original_vars:
            trial_code=trial_code.replace(f"##{v}##",trial_mapping[v])
        trial_base,trial_penalty=get_score(trial_code,checked_examples)
        trial_total=payload_overhead+trial_base+trial_penalty
        if trial_total<=best_total:
            is_new=trial_total<best_total
            best_code=trial_code;best_base=trial_base;best_penalty=trial_penalty;best_total=trial_total
            if verbose and is_new:
                print(f"\nNew best: {trial_total} (B:{trial_base}, P:{trial_penalty}) @{i+1}")
                print(trial_code)

    # Final full validation
    if validate_code(best_code,all_examples) is not None:
        raise ValueError("Optimized code failed full validation for task "+str(task_id))
    if verbose:
        print("\nFinal code PASSED validation.")
        print(f"Best score: {best_total} bytes (Base:{best_base} Pen:{best_penalty})")
        print("\nFinal optimized code:\n"+best_code)
    return {
        'task':task_id,
        'code':best_code,
        'base':best_base,
        'penalty':best_penalty,
        'total':best_total,
        'vars':original_vars
    }

def optimize_task(task_id:int, tasks_dir:str|None=None, output_dir:str|None=None, limit:int=4000, unsafe:bool=False, seed:int|None=None, verbose:bool=True)->dict:
    """Optimize one task file.

    Source resolution priority (when tasks_dir not explicitly provided):
      1. Existing file in output_dir (default: for_compression/taskNNN.py) so manual edits here are respected.
      2. Fallback to ../tasks/taskNNN.py from the main tasks directory.
    The optimized code is always written to output_dir (default for_compression).
    """
    base_dir=os.path.dirname(os.path.abspath(__file__))
    if output_dir is None:
        output_dir=base_dir
    os.makedirs(output_dir,exist_ok=True)

    source_path=None
    # If caller did not force a tasks_dir, prefer a local copy if it exists
    if tasks_dir is None:
        local_candidate=os.path.join(output_dir,f'task{task_id:03d}.py')
        if os.path.exists(local_candidate):
            source_path=local_candidate
        else:
            tasks_dir=os.path.abspath(os.path.join(base_dir,'..','tasks'))
            source_path=os.path.join(tasks_dir,f'task{task_id:03d}.py')
    else:
        source_path=os.path.join(tasks_dir,f'task{task_id:03d}.py')

    if not os.path.exists(source_path):
        raise FileNotFoundError(source_path)

    with open(source_path,'r') as f:
        raw=f.read().strip()
    if verbose:
        print(f"Source path: {source_path}")
    res=_run_variable_minimization(raw,task_id,limit=limit,unsafe=unsafe,seed=seed,verbose=verbose)
    out_path=os.path.join(output_dir,f'task{task_id:03d}.py')
    with open(out_path,'w') as f:
        f.write(res['code']+'\n')
    return res

def optimize_all(tasks_dir:str|None=None, output_dir:str|None=None, limit:int=4000, unsafe:bool=False, seed:int|None=None, subset:list[int]|None=None, verbose:bool=True)->list[dict]:
    base_dir=os.path.dirname(os.path.abspath(__file__))
    # When tasks_dir is None we now ONLY operate on the local for_compression directory (output_dir)
    if output_dir is None:
        output_dir=base_dir
    if tasks_dir is None:
        tasks_dir=output_dir  # restrict scope to local optimized copies
        if verbose:
            print(f"optimize_all: restricting to local directory {tasks_dir}")
    files=[f for f in os.listdir(tasks_dir) if re.match(r'task\d+\.py$',f)]
    ids=sorted(int(re.findall(r'\d+',f)[0]) for f in files)
    if subset:
        ids=[i for i in ids if i in subset]
    results=[]
    for tid in ids:
        try:
            print(f'Optimizing task {tid:03d}...')
            res=optimize_task(tid,tasks_dir=tasks_dir,output_dir=output_dir,limit=limit,unsafe=unsafe,seed=seed,verbose=verbose)
            results.append(res)
            print(f' -> {res["total"]} bytes')
        except Exception as e:
            print(f' !! Task {tid:03d} failed: {e}')
    return results

if __name__=='__main__':
    if len(sys.argv)>1:
        arg=sys.argv[1]
        if arg=='all':
            optimize_all()
        else:
            optimize_task(int(arg))
    else:
        # default behavior: optimize the task referenced by this script's previous constant (80)
        optimize_task(80)