"""Command to check hyperlinks in a PDF file."""

import click

from pe_toolkit.utils.pdf_utils import check_broken_links, extract_links
from pe_toolkit.utils.pretty_print import print_info, print_success, print_warning


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
            name_part = f" ({b['name']})" if b["name"] else ""
            click.echo(f" - Page {b['page']}: {b['url']}{name_part}")
    else:
        print_success("All links are valid!")
