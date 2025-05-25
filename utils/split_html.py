from pathlib import Path
from bs4 import BeautifulSoup

# -------- CONFIG -------------------------------------------------------------
SOURCE_FILE   = "extractor/apidocs/wikipedia/wikipedia.html"        # path to the big file you have now
OUTPUT_PREFIX = "extractor/apidocs/wikipedia"       # will yield api_doc_part_01.html … 10.html
PARTS         = 10                    # how many slices you want
# -----------------------------------------------------------------------------

def split_html_into_parts(in_path: str, n_parts: int, out_prefix: str):
    html = Path(in_path).read_text(encoding="utf-8")

    soup = BeautifulSoup(html, "html.parser")

    # pull out <head> once so we can re-use it verbatim
    head_html = str(soup.head) if soup.head else ""

    # grab *everything* that would normally be rendered inside <body>
    body = soup.body if soup.body else soup
    body_html = "".join(str(child) for child in body.contents)

    # break the body string into ~equal chunks
    chunk_len = len(body_html) // n_parts + 1
    chunks = [body_html[i:i + chunk_len] for i in range(0, len(body_html), chunk_len)]
    if len(chunks) < n_parts:                       # file shorter than n_parts?
        chunks.extend([""] * (n_parts - len(chunks)))

    # write out each part with the original head
    for idx, chunk in enumerate(chunks[:n_parts], 1):
        part_path = f"{out_prefix}{idx:02}.html"
        with open(part_path, "w", encoding="utf-8") as f:
            f.write("<!DOCTYPE html>\n<html>\n")
            f.write(head_html + "\n")
            f.write("<body>\n")
            f.write(chunk)
            f.write("\n</body>\n</html>")
        print(f"✓ wrote {part_path}")

if __name__ == "__main__":
    split_html_into_parts(SOURCE_FILE, PARTS, OUTPUT_PREFIX)