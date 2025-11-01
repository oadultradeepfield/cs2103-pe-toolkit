"""Utility functions for handling PDF files."""

from typing import Dict, List

import requests
from PyPDF2 import PdfReader


def extract_links(pdf_path: str) -> List[Dict[str, str]]:
    reader = PdfReader(pdf_path)
    links = []

    for page_num, page in enumerate(reader.pages):
        for annot in page.get("/Annots", []):
            obj = annot.get_object()
            if "/A" in obj and "/URI" in obj["/A"]:
                link_name = obj.get("/Contents", "").strip() if "/Contents" in obj else ""
                links.append({
                    "url": obj["/A"]["/URI"],
                    "page": str(page_num + 1),
                    "name": link_name
                })

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
