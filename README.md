# Calculator CLI

This repository contains a simple command-line calculator written in Python. It supports basic operations such as addition, subtraction, multiplication, and division.

## Requirements

- Python 3.x
- `pytest` for running the unit tests (optional)

## Running the Calculator

From the project directory run:

```bash
python calculator.py <number1> <operation> <number2>
```

Replace `<number1>` and `<number2>` with numbers and `<operation>` with one of `+`, `-`, `*`, or `/`.

Example:

```bash
python calculator.py 2 + 3
```

This will output:

```
Result: 5.0
```
## Running the GUI

To start the graphical interface run:

```bash
python calculator_gui.py
```


## Running Tests

To run the test suite use:

```bash
pytest -q
```

## For Kids 🧒

Think of this calculator like a helper that does math for you. You tell it two numbers and what kind of math you want to do:

- `+` means add the numbers together.
- `-` means take one number away from the other.
- `*` means multiply (like repeated adding).
- `/` means divide (split into parts).

Try typing `python calculator.py 4 + 5` and it will tell you the answer (`Result: 9.0`).

Have fun practicing your math!
You can also open a small window by running `python calculator_gui.py` and clicking the buttons to do math!
