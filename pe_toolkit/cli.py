"""CS2103T PE Toolkit: Practical Exam Helper CLI"""

import warnings

warnings.filterwarnings("ignore")

from typing import cast  # noqa: E402

import click  # noqa: E402

from pe_toolkit.commands.check_links import check_links  # noqa: E402
from pe_toolkit.commands.generate import generate  # noqa: E402


@click.group()
def cli():
    pass


cli.add_command(cast(click.Command, generate))
cli.add_command(cast(click.Command, check_links))

if __name__ == "__main__":
    cli()
