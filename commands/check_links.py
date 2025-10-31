"""Command to check hyperlinks in a PDF file."""

import click

from utils.pdf_utils import extract_links, check_broken_links


@click.command()
@click.argument("pdf_path", type=click.Path(exists=True))
def check_links(pdf_path: str) -> None:
    links = extract_links(pdf_path)
    if not links:
        click.echo("[INFO] No hyperlinks found in PDF.")
        return

    broken = check_broken_links(links)
    if broken:
        click.echo("[WARNING] Broken links found:")
        for b in broken:
            click.echo(f" - {b}")
    else:
        click.echo("[SUCCESS] All links are valid!")
