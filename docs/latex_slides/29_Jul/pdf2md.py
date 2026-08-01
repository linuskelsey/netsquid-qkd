#!/usr/bin/env python3
"""Convert all PDFs in ./artefacts/pdf to markdown using pymupdf4llm.
Output files are named <lead-author>-<year>-<journal>.md.
Running again renames existing MDs and converts new PDFs.
"""
import sys
import re
from pathlib import Path
from collections import Counter
import fitz  # pymupdf
import pymupdf4llm

ARTEFACTS = Path(__file__).parent / "artefacts"
PDF_DIR = ARTEFACTS / "pdf"
MD_DIR = ARTEFACTS / "md"
MD_DIR.mkdir(exist_ok=True)

# DOI prefix → journal abbreviation (most reliable)
DOI_JOURNALS = [
    (r'10\.1103/PhysRevLett', 'PRL'),
    (r'10\.1103/PhysRevX\b', 'PRX'),
    (r'10\.1103/PhysRevB\b', 'PRB'),
    (r'10\.1103/PhysRevA\b', 'PRA'),
    (r'10\.1103/PhysRevApplied', 'PRApplied'),
    (r'10\.1038/nnano|10\.1038/s41565', 'NatNano'),
    (r'10\.1038/s41467', 'NatComms'),
    (r'10\.1038/s41563', 'NatMat'),
    (r'10\.1038/s41567', 'NatPhys'),
    (r'10\.1038/s41586', 'Nature'),
    (r'10\.1002/adma', 'AdvMat'),
    (r'10\.22331/q', 'Quantum'),
    (r'10\.1126/science', 'Science'),
    (r'10\.1038/npjqi|10\.1038/s41534', 'npjQI'),
    (r'10\.1088/1367-2630|10\.1088/njp', 'NJP'),
    (r'10\.1016/j\.jmr', 'JMR'),
    (r'10\.1063/\d', 'APL'),
]

TEXT_JOURNALS = [
    (r'Physical Review Letters|Phys\.?\s*Rev\.?\s*Lett', 'PRL'),
    (r'Physical Review X|Phys\.?\s*Rev\.?\s*X\b', 'PRX'),
    (r'Physical Review B|Phys\.?\s*Rev\.?\s*B\b', 'PRB'),
    (r'Physical Review Applied', 'PRApplied'),
    (r'Nature Nanotechnology', 'NatNano'),
    (r'Nature Communications', 'NatComms'),
    (r'Nature Materials', 'NatMat'),
    (r'Nature Physics', 'NatPhys'),
    (r'Nature\b', 'Nature'),
    (r'Advanced Materials', 'AdvMat'),
    (r'npj Quantum', 'npjQI'),
    (r'Journal of Magnetic Resonance', 'JMR'),
    (r'Applied Physics Letters', 'APL'),
    (r'New Journal of Physics', 'NJP'),
    (r'PhD\s+[Tt]hesis|[Tt]h[eè]se\s+de\s+[Dd]octorat|THESE\s+DE\s+DOCTORAT', 'thesis'),
]

AUTHOR_SUFFIX = r'[\d∗*†‡§⇑]|(?<=[a-z])\s+[a-e](?=,|\s)'


def normalize(text):
    for smart, plain in [(''', "'"), (''', "'"), ('"', '"'),
                         ('"', '"'), ('—', '-'), ('–', '-')]:
        text = text.replace(smart, plain)
    return text


def slugify(s):
    s = s.strip().lower()
    s = re.sub(r"[''`]", '', s)
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[\s_]+', '-', s)
    return s.strip('-')


def extract_year(text, pdf_path=None):
    m = re.search(r'\(Dated:\s+\w+\s+\d+,\s+(\d{4})\)', text[:4000])
    if m:
        return m.group(1)

    m = re.search(r'published\s+\d+\s+\w+\s+(20\d{2}|19[89]\d)', text[:4000], re.I)
    if m:
        return m.group(1)

    m = re.search(r'(?:souten|defend)\w*\s+.*?(20\d{2}|19[89]\d)', text[:6000], re.I)
    if m:
        return m.group(1)

    m = re.search(r'(?:Accepted|Available online)\s+\d+\s+\w+\s+(20\d{2})', text[:6000], re.I)
    if m:
        return m.group(1)

    m = re.search(r'Received\s+\d+\s+\w+\s+(20\d{2})', text[:6000], re.I)
    if m:
        return m.group(1)

    m = re.search(r'©\s*(20\d{2}|19[89]\d)', text[:6000])
    if m:
        return m.group(1)

    if pdf_path:
        m = re.match(r'(\d{2})(\d{2})-\d', pdf_path.name)
        if m:
            return '20' + m.group(1)

    years = re.findall(r'\b(20\d{2}|199\d)\b', text[:10000])
    if years:
        return Counter(years).most_common(1)[0][0]

    return 'unknown'


def extract_lead_author(text):
    m = re.search(
        r"(?:^[Pp]ar|^[Bb]y)\s+([A-Z][a-z'-]+\s+[A-Z][a-z'-]+)",
        text[:6000], re.MULTILINE
    )
    if m:
        name = m.group(1).strip()
        return slugify(name.split()[-1])

    m = re.search(
        r"(?:^|\n)((?:[A-Z][a-zA-Z'-]*\.?\s+){1,3}"
        r"[A-Z][a-zA-Z'-]+(?:-[A-Z][a-zA-Z'-]+)?)"
        r"[,\s]*[\d*∗†‡§]",
        text[:3000], re.MULTILINE
    )
    if m:
        name = m.group(1).strip()
        words = name.split()
        if 2 <= len(words) <= 6 and not name.isupper():
            return slugify(words[-1])

    m = re.search(
        r"(?:^|\n)([A-Z]\w+\s+[A-Z]\w+),\s+[A-Z]",
        text[:3000], re.MULTILINE
    )
    if m:
        name = m.group(1).strip()
        words = name.split()
        if len(words) == 2:
            return slugify(words[-1])

    m = re.search(
        r"(?:^|\n|,\s*)([A-Z]\.(?:[A-Z]\.)*\s+[A-Z][a-z'-]{2,})"
        r"[,\s]*[\d*∗†‡§]",
        text[:3000], re.MULTILINE
    )
    if m:
        parts = m.group(1).strip().split()
        return slugify(parts[-1])

    m = re.search(
        r"(?:^|\n)([A-Z][a-z'-]+\s+(?:[A-Z]\.)+\s+[A-Z][a-z'-]+)"
        r"\s+[a-e],",
        text[:3000], re.MULTILINE
    )
    if m:
        name = m.group(1).strip()
        return slugify(name.split()[-1])

    m = re.search(
        r"(?:^|\n)([A-Z][a-z'-]+\s+[A-Z][a-z'-]+)\s*[*∗⇑]",
        text[:3000], re.MULTILINE
    )
    if m:
        name = m.group(1).strip()
        return slugify(name.split()[-1])

    return 'unknown'


def extract_journal(text):
    doi_match = re.search(r'10\.\d{4,}/\S+', text[:8000])
    if doi_match:
        doi = doi_match.group(0)
        for pattern, abbrev in DOI_JOURNALS:
            if re.search(pattern, doi, re.I):
                return abbrev

    sample = text[:8000]
    for pattern, abbrev in TEXT_JOURNALS:
        if re.search(pattern, sample, re.I):
            return abbrev

    return 'unknown'


def get_pdf_text(pdf_path, pages=3):
    doc = fitz.open(str(pdf_path))
    text = ''
    for i in range(min(pages, doc.page_count)):
        text += doc[i].get_text()
    doc.close()
    return normalize(text)


def desired_name(pdf_path):
    text = get_pdf_text(pdf_path)
    author  = extract_lead_author(text)
    year    = extract_year(text, pdf_path)
    journal = extract_journal(text)
    return f"{author}-{year}-{journal}"


def convert_and_rename():
    pdfs = sorted(PDF_DIR.glob("*.pdf"))
    if not pdfs:
        print("No PDFs found in ./artefacts/pdf")
        sys.exit(0)

    for pdf in pdfs:
        name = desired_name(pdf)
        out  = MD_DIR / f"{name}.md"

        old = MD_DIR / pdf.with_suffix(".md").name
        if old.exists() and old != out:
            print(f"rename  {old.name} → {out.name}")
            old.rename(out)

        if out.exists():
            print(f"skip    {pdf.name} → {out.name}")
            continue

        print(f"convert {pdf.name} → {out.name} ...", end=" ", flush=True)
        md = pymupdf4llm.to_markdown(str(pdf))
        out.write_text(md, encoding="utf-8")
        print("done")


if __name__ == "__main__":
    convert_and_rename()
