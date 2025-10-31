"""CS2103T PE Toolkit: Practical Exam Helper CLI"""
from typing import cast

import click

from commands import generate, check_links


@click.group()
def cli():
    pass


cli.add_command(cast(click.Command, generate))
cli.add_command(cast(click.Command, check_links))

if __name__ == "__main__":
    cli()
