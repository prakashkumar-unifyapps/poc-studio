#!/usr/bin/env python3
"""POC Studio · wireframes coverage check.

usage: coverage.py <scoping-document.docx | .pdf> <wireframe-manifest.json>
Prints what the scoping document builds but the wireframes do not show (and the reverse), as JSON, and exits 1 when
anything is missing. Pages are matched by their PG- ID (the wireframe page id is the scoping page id); components by
the CMP- IDs in section 23, carried on wireframe blocks as "cmp".
"""
import json, re, subprocess, sys

PG = r"\bPG-[A-Z]*\d+\b"   # the scoping checker's page-ID shape (PG-03, PG-A01)
uniq = lambda xs: list(dict.fromkeys(xs))

def ids_in_pdf(path):
    """A BRD given as PDF: page IDs that start a line, CMP IDs anywhere (pdftotext ships with the collateral tools)."""
    text = subprocess.run(["pdftotext", "-layout", path, "-"], capture_output=True, text=True, check=True).stdout
    pages = [m for line in text.splitlines() for m in re.findall(PG, line.strip()[:12])]
    return uniq(pages), uniq(re.findall(r"\bCMP-[\w-]+", text))

def ids_in_docx(path):
    if path.lower().endswith(".pdf"): return ids_in_pdf(path)
    from docx import Document
    doc = Document(path)
    pages, cmps = [], []
    for para in doc.paragraphs:
        if para.style.name.lower().startswith("heading"):
            pages += re.findall(PG, para.text)
    for t in doc.tables:
        for row in t.rows:
            cell = row.cells[0].text.strip()
            if re.fullmatch(r"CMP-[\w-]+", cell): cmps.append(cell)
    return uniq(pages), uniq(cmps)

def main(docx, manifest):
    pages, cmps = ids_in_docx(docx)
    m = json.load(open(manifest))
    wf_pages = [p["id"] for p in m["pages"]]
    base = lambda f: next((q for q in pages if re.fullmatch(rf"{re.escape(q)}[a-z]?", f)), None)  # PG-03b → PG-03
    wf_cmps = {c for comp in m["components"] for c in comp.get("cmp", [])}
    unnamed = [c["component"] for c in m["components"] if c["type"] in ("slot",) and not c.get("cmp")]
    out = {
        "scoping_pages": len(pages), "wireframe_pages": len(wf_pages),
        "pages_missing_from_wireframes": [p for p in pages if p not in wf_pages],
        "wireframe_pages_not_in_scoping": [f for f in wf_pages if base(f) is None],
        "scoping_components": len(cmps),
        "components_missing_from_wireframes": [c for c in cmps if c not in wf_cmps],
        "components_in_manifest": len(m["components"]),
        "slots_without_cmp": unnamed,
    }
    print(json.dumps(out, indent=2))
    sys.exit(1 if out["pages_missing_from_wireframes"] or out["components_missing_from_wireframes"] or out["wireframe_pages_not_in_scoping"] else 0)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
