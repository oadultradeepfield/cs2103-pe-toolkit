"""Command to check hyperlinks in a PDF file."""

import click

from utils import print_info, print_warning
from utils.pdf_utils import extract_links, check_broken_links
from utils.pretty_print import print_success


@click.command()
@click.argument("pdf_path", type=click.Path(exists=True))
def check_links(pdf_path: str) -> None:
    links = extract_links(pdf_path)
    if not links:
        print_info("No hyperlinks found in PDF.")
        return

    broken = check_broken_links(links)
    if broken:
        print_warning("Broken links found:")
        for b in broken:
            name_part = f" ({b['name']})" if b['name'] else ""
            click.echo(f" - Page {b['page']}: {b['url']}{name_part}")
    else:
        print_success("All links are valid!")
