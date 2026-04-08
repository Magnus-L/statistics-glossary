"""
Build the glossary HTML page.

Reads glossary_merged.csv and embeds the data as JSON into index.html.
Run: python3 build.py
Output: docs/index.html (ready for GitHub Pages)
"""

import csv
import json
from pathlib import Path

PROJECT = Path(__file__).parent
MERGED = PROJECT / "glossary_merged.csv"
TEMPLATE = PROJECT / "index.html"
OUTPUT_DIR = PROJECT / "docs"
OUTPUT = OUTPUT_DIR / "index.html"


def main():
    # Read merged glossary
    terms = []
    with open(MERGED, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            terms.append({
                "english": row["english"].strip(),
                "swedish": row["swedish"].strip(),
                "source": row["source"].strip(),
                "notes": row.get("notes", "").strip(),
            })

    print(f"Loaded {len(terms)} terms")

    # Sort alphabetically by English
    terms.sort(key=lambda t: t["english"].lower())

    # Read template
    html = TEMPLATE.read_text(encoding="utf-8")

    # Replace placeholder with JSON data
    json_data = json.dumps(terms, ensure_ascii=False, separators=(",", ":"))
    html = html.replace("GLOSSARY_DATA_PLACEHOLDER", json_data)

    # Update count in subtitle
    count_str = f"{len(terms):,}".replace(",", "\u00a0")
    html = html.replace("2 050 termer", f"{count_str} termer")
    html = html.replace("2 050", str(len(terms)))

    # Write output
    OUTPUT_DIR.mkdir(exist_ok=True)
    OUTPUT.write_text(html, encoding="utf-8")
    print(f"Built {OUTPUT} ({OUTPUT.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
