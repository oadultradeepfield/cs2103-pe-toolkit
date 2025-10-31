"""CS2103T PE Toolkit: Practical Exam Helper CLI"""

import warnings

warnings.filterwarnings("ignore")

from typing import cast

import click

from pe_toolkit.commands import check_links
from pe_toolkit.commands.generate import generate


@click.group()
def cli():
    pass


cli.add_command(cast(click.Command, generate))
cli.add_command(cast(click.Command, check_links))

if __name__ == "__main__":
    cli()
