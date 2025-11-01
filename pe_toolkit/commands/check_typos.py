"""Command to check for potential typos in a PDF file."""

import click

from pe_toolkit.utils.pdf_utils import detect_typos
from pe_toolkit.utils.pretty_print import print_info, print_warning


@click.command()
@click.argument("pdf_path", type=click.Path(exists=True))
def check_typos(pdf_path: str) -> None:
    typos = detect_typos(pdf_path)
    if not typos:
        print_info("No typos found in PDF.")
        return

    print_warning("Potential typos found:")
    for typo in typos:
        suggestions = ", ".join(typo["suggestions"]) if typo["suggestions"] else "None"
        click.echo(
            f" - Page {typo['page']}: '{typo['word']}' (suggestions: {suggestions})"
        )
