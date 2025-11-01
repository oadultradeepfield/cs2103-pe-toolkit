"""Utility functions for handling PDF files."""

from typing import Dict, List, Union

import requests
from PyPDF2 import PdfReader
from spellchecker import SpellChecker


def extract_links(pdf_path: str) -> List[Dict[str, str]]:
    reader = PdfReader(pdf_path)
    links = []

    for page_num, page in enumerate(reader.pages):
        for annot in page.get("/Annots", []):
            obj = annot.get_object()
            if "/A" in obj and "/URI" in obj["/A"]:
                link_name = (
                    obj.get("/Contents", "").strip() if "/Contents" in obj else ""
                )
                links.append(
                    {
                        "url": obj["/A"]["/URI"],
                        "page": str(page_num + 1),
                        "name": link_name,
                    }
                )

    return links


def check_broken_links(links: List[Dict[str, str]]) -> List[Dict[str, str]]:
    broken = []

    for link in links:
        try:
            resp = requests.head(link["url"], timeout=5)
            if resp.status_code >= 400:
                broken.append(link)
        except requests.RequestException:
            broken.append(link)

    return broken


def detect_typos(pdf_path: str) -> List[Dict[str, Union[str, set[str], None]]]:
    """Detect potential typos in the PDF text using spell checking."""
    reader = PdfReader(pdf_path)
    spell = SpellChecker()
    typos = []

    for page_num, page in enumerate(reader.pages):
        text = page.extract_text()
        words = text.split()
        misspelled = spell.unknown(words)
        for word in misspelled:
            typos.append(
                {
                    "word": word,
                    "page": str(page_num + 1),
                    "suggestions": spell.candidates(word),
                }
            )

    return typos
