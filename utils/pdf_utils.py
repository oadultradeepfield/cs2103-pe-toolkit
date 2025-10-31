"""Utility functions for handling PDF files."""

from typing import List

import requests
from PyPDF2 import PdfReader


def extract_links(pdf_path: str) -> List[str]:
    reader = PdfReader(pdf_path)
    links = []

    for page in reader.pages:
        for annot in page.get("/Annots", []):
            obj = annot.get_object()
            if "/A" in obj and "/URI" in obj["/A"]:
                links.append(obj["/A"]["/URI"])

    return links


def check_broken_links(links: List[str]) -> List[str]:
    broken = []

    for url in links:
        try:
            resp = requests.head(url, timeout=5)
            if resp.status_code >= 400:
                broken.append(url)
        except requests.RequestException:
            broken.append(url)

    return broken
