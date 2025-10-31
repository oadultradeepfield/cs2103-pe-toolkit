"""Generate edge case inputs from a JSON spec file."""

import json

import click

from utils.edge_cases import GENERATORS


@click.command()
@click.argument("spec_file", type=click.Path(exists=True))
def generate(spec_file: str) -> None:
    click.echo(f"[INFO] Reading JSON spec: {spec_file}")
    with open(spec_file) as f:
        specs = json.load(f)

    for spec in specs:
        var = spec.get("variable")
        typ = spec.get("type")
        prefix = spec.get("prefix", "")

        click.echo(f"\n[INFO] Generating edge cases for {var} ({typ})")
        func = GENERATORS.get(typ)

        if func:
            func(prefix, spec)
        else:
            click.echo(f"[WARNING] Unknown type: {typ}")
