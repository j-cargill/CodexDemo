"""Simple calculator app with basic operations."""

from dataclasses import dataclass
from typing import Callable, Dict, Iterable
import argparse

@dataclass
class Operation:
    symbol: str
    func: Callable[[float, float], float]


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


OPERATIONS: Dict[str, Operation] = {
    '+': Operation('+', add),
    '-': Operation('-', subtract),
    '*': Operation('*', multiply),
    '/': Operation('/', divide),
}


def calculate(a: float, op_symbol: str, b: float) -> float:
    if op_symbol not in OPERATIONS:
        raise ValueError(f"Unsupported operation: {op_symbol}")
    operation = OPERATIONS[op_symbol]
    return operation.func(a, b)


def main(args: Iterable[str] | None = None) -> None:
    """Entry point for the CLI calculator."""

    parser = argparse.ArgumentParser(description="Simple Calculator")
    parser.add_argument("a", type=float, help="First number")
    parser.add_argument(
        "operation",
        choices=list(OPERATIONS.keys()),
        help="Operation to perform",
    )
    parser.add_argument("b", type=float, help="Second number")

    parsed = parser.parse_args(list(args) if args is not None else None)

    try:
        result = calculate(parsed.a, parsed.operation, parsed.b)
    except Exception as e:  # pragma: no cover - user input errors
        print(f"Error: {e}")
        return

    print(f"Result: {result}")


if __name__ == "__main__":
    main()

