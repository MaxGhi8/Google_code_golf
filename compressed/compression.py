#! /usr/bin/env python
import ast
import base64
import os
import re
import sys
import zipfile
import zlib  # added

# Optional pretty printing (fallback to std print if rich unavailable)
try:
    from rich import print as print_rich  # type: ignore
    from rich.panel import Panel  # type: ignore
    from rich.syntax import Syntax  # type: ignore
except Exception:  # pragma: no cover

    def print_rich(*a, **k):  # type: ignore
        print(*a, **k)

    class Panel:  # type: ignore
        def __init__(self, renderable, title=None, border_style=None):
            self.renderable = renderable
            self.title = title

        def __str__(self):
            hdr = f"[{self.title}]\n" if self.title else ""
            return f"{hdr}{self.renderable}"

    class Syntax:  # type: ignore
        def __init__(self, code, *_, **__):
            self.code = code

        def __str__(self):
            return self.code


# Compression backend (prefer zopfli, fallback to stdlib zlib)
# try:
import zopfli.zlib as zopfli_zlib  # type: ignore

try:
    import zopfli.deflate as zopfli_deflate  # type: ignore
except Exception:  # pragma: no cover
    zopfli_deflate = None


def _best_compress(data: bytes) -> bytes:
    return zopfli_zlib.compress(data)


# except Exception:  # pragma: no cover
#     import zlib as _zl
#     def _best_compress(data: bytes) -> bytes:
#         # Use max compression level as fallback
#         return _zl.compress(data, 9)

# Attempt Kaggle-style import; fallback silently if unavailable
try:
    sys.path.append("/kaggle/input/google-code-golf-2025/code_golf_utils")
    from code_golf_utils import *  # type: ignore
except Exception:  # pragma: no cover
    pass

# Determine submission directory depending on environment (Kaggle vs local)
if os.path.isdir("/kaggle") and os.access("/kaggle", os.W_OK):
    SUBMISSION_DIR = "/kaggle/working/submission"
else:
    SUBMISSION_DIR = os.path.join(os.path.dirname(__file__), "_submission")

try:
    os.makedirs(SUBMISSION_DIR, exist_ok=True)
except Exception:
    # Fallback to in-place directory if creation fails
    SUBMISSION_DIR = os.path.join(os.path.dirname(__file__), "_submission_local")
    os.makedirs(SUBMISSION_DIR, exist_ok=True)

BASE_DIR = os.path.dirname(__file__)


def _compress_variants(data: bytes):
    variants = []
    # Standard zlib levels
    for lvl in (9, 7, 6, 3):
        try:
            variants.append((f"zlib{lvl}", zlib.compress(data, lvl)))
        except Exception:
            pass
    # Raw deflate via zlib (no header)
    for lvl in (9, 6):
        try:
            compobj = zlib.compressobj(lvl, zlib.DEFLATED, -15)
            raw = compobj.compress(data) + compobj.flush()
            variants.append((f"deflate{lvl}", raw))
        except Exception:
            pass
    # Zopfli zlib (header) best compress
    try:
        zopfli_bytes = _best_compress(data)
        variants.append(("zopfli_zlib", zopfli_bytes))
    except Exception:
        pass
    # Zopfli raw deflate (often slightly smaller) if available
    if zopfli_deflate:
        try:
            variants.append(("zopfli_raw", zopfli_deflate.compress(data)))
        except Exception:
            pass
    # Deduplicate
    dedup = {}
    for name, blob in variants:
        if blob not in dedup or len(blob) < len(dedup[blob][1]):
            dedup[blob] = (name, blob)
    return [v for _, v in dedup.items()]


def _latin1_literal(data: bytes) -> bytes:
    # Simpler, safer escaping ensuring round‑trip via latin1 decoding
    s = ''.join(chr(b) for b in data)
    s = (s
         .replace('\\', r'\\')
         .replace('\n', r'\n')
         .replace('\r', r'\r')
         .replace('\0', r'\0')
         .replace('"', r'\"')
         .replace("'", r"\'")
    )
    return b'"' + s.encode('latin1') + b'"'


def _validate_latin1_literal(comp_bytes: bytes, lit: bytes) -> bool:
    try:
        # lit is bytes containing quoted python string literal
        py_str = ast.literal_eval(lit.decode('latin1'))  # type: ignore
        return py_str.encode('latin1') == comp_bytes
    except Exception:
        return False


def _build_wrappers(comp_bytes: bytes, original_len: int, raw: bool):
    wrappers = []
    lit = _latin1_literal(comp_bytes)
    if _validate_latin1_literal(comp_bytes, lit):
        if raw:
            code = b"#coding:L1\nimport zlib;exec(zlib.decompress(bytes(" + lit + b",'L1'),-15))"
            wrappers.append(('latin1_import_raw', code))
        else:
            code = b"#coding:L1\nimport zlib;exec(zlib.decompress(bytes(" + lit + b",'L1')))"
            wrappers.append(('latin1_import', code))
    # Fallback: base85 (always safe ascii) if no valid latin1 or if latin1 produced different bytes
    # (We still add it as alternative so size competition can choose smallest valid)
    b85 = base64.b85encode(comp_bytes)
    if raw:
        code = b"import zlib,base64;exec(zlib.decompress(base64.b85decode('" + b85 + b"'),-15))"
        wrappers.append(('b85_raw', code))
    else:
        code = b"import zlib,base64;exec(zlib.decompress(base64.b85decode('" + b85 + b"')))"
        wrappers.append(('b85', code))
    return wrappers


def save_final_solution(
    task_id: int, solution_code: str, output_dir: str = SUBMISSION_DIR
):
    # Force best compression even if larger than original; pick shortest wrapper among variants
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, f"task{task_id:03d}.py")
    source = solution_code.strip().encode("utf-8")
    original_len = len(source)

    # Generate compression variants
    variants = _compress_variants(source)
    candidates = []
    for name, blob in variants:
        # Treat both explicit deflate* and * _raw variants as raw (no zlib header)
        raw = name.startswith("deflate") or name.endswith("_raw")
        for wname, wrapper in _build_wrappers(blob, original_len, raw):
            candidates.append((f"{name}:{wname}", wrapper))
    # Choose minimal total length
    best_name, best_code = min(candidates, key=lambda x: len(x[1]))
    final_len = len(best_code)
    delta = final_len - original_len
    status = "[green]-" if delta < 0 else "[red]+" if delta > 0 else "[yellow]="
    print_rich(
        f"Best wrapper '{best_name}' => {final_len} bytes (original {original_len}, Δ {delta} {status})"
    )

    with open(file_path, "wb") as f:
        f.write(best_code)

    display_code = best_code.decode("latin1", errors="replace")
    panel_title = f"✓ Compressed Task {task_id} ({final_len} bytes)"
    panel = Panel(
        Syntax(display_code.strip(), "python", theme="monakai", line_numbers=False),
        title=panel_title,
        border_style="green",
    )
    print_rich(panel)


def create_submission_zip():
    zip_path = "/kaggle/working/submission.zip"
    print_rich(f"\nCreating submission file at {zip_path} ...")
    saved_solutions = [
        f
        for f in os.listdir(SUBMISSION_DIR)
        if f.startswith("task") and f.endswith(".py")
    ]
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for filename in sorted(saved_solutions):
            file_path = os.path.join(SUBMISSION_DIR, filename)
            zipf.write(file_path, arcname=filename)
    print_rich(f"Packaged {len(saved_solutions)} solutions -> {zip_path}")


def _find_original_source(task_num: int):
    task_filename = f"task{task_num:03d}.py"
    parent = os.path.dirname(BASE_DIR)
    # Support either naming: prefer 'for_compressed' if present, else 'for_compression'
    fc_dir = os.path.join(parent, 'for_compressed')
    if not os.path.isdir(fc_dir):
        fc_dir = os.path.join(parent, 'for_compression')
    src_path = os.path.join(fc_dir, task_filename)
    if os.path.isfile(src_path):
        print_rich(f"[cyan]Info:[/cyan] Using source from {os.path.basename(fc_dir)}/{task_filename}")
        return src_path
    return None


def _load_and_recover(path: str) -> str:
    raw_bytes = open(path, "rb").read()
    for enc in ("utf-8", "latin1"):
        try:
            code_text = raw_bytes.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    else:
        raise RuntimeError("Unable to decode source file")

    def recover_original(maybe_wrapped: str) -> str:
        m = re.search(r"b85decode\('([!-u]+)'\)\)\)?", maybe_wrapped)
        if m and "b85decode" in maybe_wrapped:
            try:
                comp_bytes = base64.b85decode(m.group(1).encode())
                if ",-15" in maybe_wrapped:
                    return zlib.decompress(comp_bytes, -15).decode("utf-8")
                return zlib.decompress(comp_bytes).decode("utf-8")
            except Exception:
                pass
        m = re.search(r"b64decode\('([A-Za-z0-9+/=]+)'\)\)\)?", maybe_wrapped)
        if m and "b64decode" in maybe_wrapped:
            try:
                comp_bytes = base64.b64decode(m.group(1).encode())
                if ",-15" in maybe_wrapped:
                    return zlib.decompress(comp_bytes, -15).decode("utf-8")
                return zlib.decompress(comp_bytes).decode("utf-8")
            except Exception:
                pass
        m = re.search(r"bytes\((['\"])(.*?)\1,'L1'\)\)\)?", maybe_wrapped)
        if m:
            try:
                lit = ast.literal_eval(m.group(1) + m.group(2) + m.group(1)).encode("latin1")
                if ",-15" in maybe_wrapped:
                    return zlib.decompress(lit, -15).decode("utf-8")
                return zlib.decompress(lit).decode("utf-8")
            except Exception:
                pass
        return maybe_wrapped

    return recover_original(code_text)


def _compress_single(task_num: int):
    path = _find_original_source(task_num)
    if not path:
        print_rich(f"[red]Error:[/red] task{task_num:03d}.py not found in for_compression/ or for_compressed/.")
        return False
    try:
        original_source = _load_and_recover(path)
    except Exception as e:
        print_rich(f"[red]Decode error:[/red] task{task_num:03d}: {e}")
        return False
    save_final_solution(task_num, original_source, output_dir=BASE_DIR)
    return True

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python compression.py <task_number | all>")
        sys.exit(1)
    arg = sys.argv[1].strip().lower()
    if arg == "all":
        parent = os.path.dirname(BASE_DIR)
        fc_dir = os.path.join(parent, 'for_compressed')
        if not os.path.isdir(fc_dir):
            fc_dir = os.path.join(parent, 'for_compression')
        if not os.path.isdir(fc_dir):
            print_rich("[red]No source directory 'for_compression' or 'for_compressed' found.[/red]")
            sys.exit(1)
        pattern = re.compile(r"task(\d{3})\.py$")
        task_nums = {int(m.group(1)) for fn in os.listdir(fc_dir) if (m := pattern.match(fn))}
        if not task_nums:
            print_rich("[red]No task files found to compress in source directory.[/red]")
            sys.exit(1)
        print_rich(f"[cyan]Batch compression starting for {len(task_nums)} tasks from {os.path.basename(fc_dir)}...[/cyan]")
        ok = 0
        for n in sorted(task_nums):
            ok += _compress_single(n) or 0
        print_rich(f"[bold]Batch done:[/bold] {ok}/{len(task_nums)} tasks compressed.")
        sys.exit(0)
    if not re.fullmatch(r"\d+", arg):
        print("Usage: python compression.py <task_number | all>")
        sys.exit(1)
    _compress_single(int(arg))