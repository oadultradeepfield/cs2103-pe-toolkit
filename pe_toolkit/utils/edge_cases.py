"""Utility to generate edge case test inputs for various data types."""

from datetime import datetime, timedelta
from typing import Any, Callable, Dict, List

import click


def generate_string(prefix: str, spec: Dict[str, Any]) -> None:
    min_len = spec.get("min_length", 1)
    max_len = spec.get("max_length", 10)
    cases = [
        "",  # Empty string
        "A" * 9999,  # Very long string
        "A" * min_len,  # String at minimum length
        "A" * max_len,  # String at maximum length
        "A" * (min_len - 1) if min_len > 1 else "A",  # Just below minimum length
        "A" * (max_len + 1),  # Just above maximum length
        "¢¬¡",  # Special characters
        "🦦" * 7,  # Emojis
        "!@#$%^&*()"  # Special symbols
    ]
    _emit_cases(prefix, cases)


def generate_integer(prefix: str, spec: Dict[str, Any]) -> None:
    int_min, int_max = 2147483647, -2147483648
    min_val, max_val = spec.get("min", int_min), spec.get("max", int_max)
    cases = [int_min, int_max, min_val, max_val, min_val - 1, max_val + 1, -1, 0, 1]
    _emit_cases(prefix, cases)


def generate_double(prefix: str, spec: Dict[str, Any]) -> None:
    double_max, double_min = 1.7976931348623157E308, 4.9E-324
    min_val, max_val = spec.get("min", double_min), spec.get("max", double_max)
    cases = [double_min, double_max, min_val, max_val, -1.0, 0.0, 1.0]
    _emit_cases(prefix, cases)


def generate_long(prefix: str, spec: Dict[str, Any]) -> None:
    long_max, long_min = 9223372036854775807, -9223372036854775808
    min_val, max_val = spec.get("min", long_min), spec.get("max", long_max)
    cases = [long_min, long_max, min_val, max_val, -1, 0, 1]
    _emit_cases(prefix, cases)


def generate_float(prefix: str, spec: Dict[str, Any]) -> None:
    float_max, float_min = 3.4028235E38, 1.4E-45
    min_val, max_val = spec.get("min", float_min), spec.get("max", float_max)
    cases = [float_min, float_max, min_val, max_val, -1.0, 0.0, 1.0]
    _emit_cases(prefix, cases)


def generate_date(prefix: str, spec: Dict[str, Any]) -> None:
    fmt = spec.get("format", "%Y-%m-%d")
    today = datetime.today()
    cases = [today.strftime(fmt), (today - timedelta(days=1)).strftime(fmt),
             (today + timedelta(days=1)).strftime(fmt), "0001-01-01", "9999-12-31"]
    _emit_cases(prefix, cases)


def generate_time(prefix: str, spec: Dict[str, Any]) -> None:
    fmt = spec.get("format", "%H:%M")
    now = datetime.now()
    cases = [now.strftime(fmt), (now - timedelta(minutes=1)).strftime(fmt),
             (now + timedelta(minutes=1)).strftime(fmt), "00:00", "23:59"]
    _emit_cases(prefix, cases)


def _emit_cases(prefix: str, cases: List[Any]) -> None:
    """Helper to emit cases with a given prefix."""
    for case in cases:
        click.echo(f"{prefix}{case}")


GENERATORS: Dict[str, Callable[[str, Dict[str, Any]], None]] = {
    "string": generate_string,
    "integer": generate_integer,
    "double": generate_double,
    "long": generate_long,
    "float": generate_float,
    "date": generate_date,
    "time": generate_time
}
