#!/usr/bin/env python3
"""
Remove any empty parameter files (size == 0 bytes *or* only whitespace).

Usage:
    python delete_empty_files.py /path/to/dir
"""
import argparse,requests
import pathlib
import sys
from typing import Iterable, List


def find_empty_files(root: pathlib.Path, exts: Iterable[str] = (".py",)) -> List[pathlib.Path]:
    """
    Return a list of files that are 'empty':
      • zero bytes  OR
      • only whitespace/new-lines.
    """
    empty_files: List[pathlib.Path] = []
    for p in root.rglob("*"):
        if p.is_file() and p.suffix.lower() in exts:
            # Fast check: size == 0 bytes
            if p.stat().st_size == 0:
                empty_files.append(p)
                continue

            # Slower check: file contains only whitespace
            try:
                if p.read_text(encoding="utf-8").strip() == "":
                    empty_files.append(p)
            except UnicodeDecodeError:
                # Binary or unreadable -> keep it, don't delete
                pass
    return empty_files


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", type=pathlib.Path,
                        help="Root folder to scan")
    parser.add_argument(
        "--ext",
        action="append",
        default=[".py"],
        help="File extension(s) to consider (can be repeated)",
    )
    parser.add_argument("-n", "--dry-run", action="store_true",
                        help="Report but do NOT delete")
    args = parser.parse_args()

    if not args.directory.is_dir():
        print(f"{args.directory} is not a directory", file=sys.stderr)
        sys.exit(1)

    empty_files = find_empty_files(args.directory, exts=args.ext)

    if not empty_files:
        print("No empty files found.")
        return

    print(f"Found {len(empty_files)} empty file(s):")
    for p in empty_files:
        print("  ", p)

    if args.dry_run:
        print("\nDry-run mode: nothing deleted.")
        return

    for p in empty_files:
        try:
            p.unlink()
        except Exception as exc:
            print(f"Could not delete {p}: {exc}", file=sys.stderr)

    print("\nDone – empty files removed.")


if __name__ == "__main__":
    main()





# import shutil
# from pathlib import Path

# ROOT = Path("extractor/apidocs")           # adjust if the folder lives elsewhere
# CONFIG_TEXT = """{
#     "base_url": "https://http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:8023"
# }
# """

# for md_file in ROOT.glob("*.md"):
#     base_name = md_file.stem                    # "access_requests"
#     html_name = f"{base_name}.html"             # "access_requests.html"
#     html_path = md_file.with_suffix(".html")    # apidocs/access_requests.html

#     # 1 — rename *.md ➜ *.html
#     md_file.rename(html_path)

#     # 2 — make <base_name>/ and move the html inside it
#     folder = ROOT / base_name                   # apidocs/access_requests/
#     folder.mkdir(exist_ok=True)
#     shutil.move(str(html_path), folder / html_name)

#     # 3 — write .config with the required JSON
#     (folder / ".config").write_text(CONFIG_TEXT, encoding="utf-8")

# print("Done!")





# import json, math

# SRC = "tmp/shopping-customer.json"   # original spec
# NUM_CHUNKS = 10                            # how many pieces you want

# with open(SRC, "r") as f:
#     spec = json.load(f)

# paths_items = list(spec.get("paths", {}).items())
# chunk_size  = math.ceil(len(paths_items) / NUM_CHUNKS)

# for i in range(NUM_CHUNKS):
#     start, end   = i * chunk_size, (i + 1) * chunk_size
#     slice_items  = paths_items[start:end]
#     if not slice_items:      # fewer paths than chunks ⇒ stop early
#         break

#     chunk = {
#         "server_url": spec.get("server_url"),
#         "paths"     : dict(slice_items),
#         "components": spec.get("components", {})
#     }

#     out = f"extractor/apidocs/shopping_chunk_{i+1}.html"
#     with open(out, "w") as f_out:
#         json.dump(chunk, f_out, indent=2)

#     print(f"Wrote {out} with {len(slice_items)} paths")
