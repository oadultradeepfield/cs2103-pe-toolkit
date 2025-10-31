"""Utility functions for pretty-printing messages to the console using the click library."""

import click


def print_info(msg):
    click.secho(f"[INFO] {msg}", fg="cyan")


def print_success(msg):
    click.secho(f"[SUCCESS] {msg}", fg="green")


def print_warning(msg):
    click.secho(f"[WARNING] {msg}", fg="yellow")


def print_error(msg):
    click.secho(f"[ERROR] {msg}", fg="red", err=True)
