"""Generate edge case inputs from a JSON spec file."""

import json

import click

from utils import print_info, print_warning
from utils.edge_cases import GENERATORS


@click.command()
@click.argument("spec_file", type=click.Path(exists=True))
def generate(spec_file: str) -> None:
    print_info(f"Reading JSON spec: {spec_file}")
    with open(spec_file) as f:
        specs = json.load(f)

    for spec in specs:
        var = spec.get("variable")
        typ = spec.get("type")
        prefix = spec.get("prefix", "")

        print_info(f"Generating edge cases for {var} ({typ})")
        func = GENERATORS.get(typ)

        if func:
            func(prefix, spec)
        else:
            print_warning(f"Unknown type: {typ}")
