# Math Tools

Math Tools is my CS50P final project: a tested Python command-line application that brings five small mathematical utilities into one interactive menu.

## Video Demo

[Watch the project demonstration on YouTube](https://www.youtube.com/watch?v=mmBFbeNgYw4).

## Project Overview

The project focuses on clear function design, input validation, exception handling, type hints, and automated tests. The application itself uses only the Python standard library.

| Tool | Purpose |
|---|---|
| Temperature converter | Convert between Celsius, Fahrenheit, and Kelvin |
| BMI calculator | Calculate BMI and return a classification |
| Base converter | Convert nonnegative integers between bases 2, 8, 10, and 16 |
| Compound interest | Calculate a final amount using annual compounding |
| Basic statistics | Calculate mean, median, and sample standard deviation |

## Requirements

- Python 3.10 or later
- pytest, only for running the test suite

## Installation

```bash
git clone https://github.com/uzoom333/cs50p.git
cd cs50p

python3 -m venv .venv
source .venv/bin/activate
python -m pip install pytest
```

On Windows PowerShell, activate the environment with:

```powershell
.\.venv\Scripts\Activate.ps1
```

## Running the Application

```bash
python project.py
```

Choose options `1` through `5` from the interactive menu, or enter `0` to exit.

### Temperature example

```text
Valor: 100
De (C/F/K): C
Para (C/F/K): F

Resultado: 212.0°F
```

### Compound-interest example

```text
Capital inicial (R$): 1000
Taxa anual (%): 10
Tempo (anos): 2

Montante final: R$ 1210.00
Juros gerados:  R$ 210.00
```

The interface messages remain in Portuguese; the commands and mathematical behavior are language-independent.

## Public Functions

- `convert_temperature(value, from_scale, to_scale)` validates the scales and physical lower bound before converting.
- `calculate_bmi(weight_kg, height_m)` validates positive inputs and returns the BMI with its classification.
- `convert_base(number, from_base, to_base)` supports bases 2, 8, 10, and 16.
- `compound_interest(principal, rate, time)` applies annual compound interest.
- `basic_statistics(numbers)` returns the mean, median, and sample standard deviation.

## Running the Tests

```bash
python -m pytest -v
```

## Repository Structure

```text
cs50p/
├── project.py       # Application functions and interactive menu
├── test_project.py  # pytest test suite
├── requirements.txt # Runtime dependency note
└── README.md
```

## Academic Context

This repository was developed as the final project for Harvard's CS50P course. It documents a stage in my Python learning journey and emphasizes small, testable functions built with the standard library.

## Author

Renato Morais Mundim Filho

- [GitHub](https://github.com/uzoom333)
