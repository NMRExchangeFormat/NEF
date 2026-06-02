#!/usr/bin/env python3
"""Convert specification/v1_2_under_review/namespaces.json to namespaces.nef."""

import json
import pynmrstar
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
VERSION   = (REPO_ROOT / "specification" / "current_version").read_text().strip()
JSON_PATH = REPO_ROOT / "specification" / VERSION / "namespaces.json"
NEF_PATH  = REPO_ROOT / "specification" / VERSION / "namespaces.nef"


def main():
    entries = json.loads(JSON_PATH.read_text(encoding="utf-8"))

    entry = pynmrstar.Entry.from_scratch("nef_namespaces_registry")

    sf = pynmrstar.Saveframe.from_scratch("nns_namespaces", tag_prefix="nns_namespaces")
    sf.add_tag("sf_category",  "nns_namespaces")
    sf.add_tag("sf_framecode", "nns_namespaces")

    loop = pynmrstar.Loop.from_scratch(category="nns_namespaces_namespace")
    for col in ("id", "name", "description", "url", "dictionary_url"):
        loop.add_tag(col)

    for item in entries:
        raw_url = item.get("url") or item.get("urls") or "."
        url = (raw_url[0] if isinstance(raw_url, list) else raw_url) or "."
        dict_url = item.get("dict_url") or "."
        loop.add_data([
            item.get("id",          "."),
            item.get("name",        "."),
            item.get("description", "."),
            url,
            dict_url,
        ])

    sf.add_loop(loop)
    entry.add_saveframe(sf)

    NEF_PATH.write_text(str(entry), encoding="utf-8")
    print(f"Written {len(entries)} namespaces to {NEF_PATH}")


if __name__ == "__main__":
    main()
