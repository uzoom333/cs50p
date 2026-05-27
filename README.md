# Math Tools

**CS50P Final Project** — CLI calculator with five mathematical utilities.

## Video Demo

[Link to be added after upload]

## Description

Interactive command-line tool built in Python. No external dependencies — uses only the standard library (`math`, `statistics`, `sys`).

### Features

| # | Tool | Description |
|---|------|-------------|
| 1 | Temperature Converter | Convert between Celsius, Fahrenheit, and Kelvin |
| 2 | BMI Calculator | Calculate BMI and return WHO classification |
| 3 | Base Converter | Convert numbers between bases 2, 8, 10, and 16 |
| 4 | Compound Interest | Calculate final amount with annual compound interest |
| 5 | Basic Statistics | Mean, median, and standard deviation for a list of numbers |

## Usage

```bash
python project.py
```

Navigate the menu with number keys (`1`–`5`), `0` to quit.

### Example — Temperature

```
Valor: 100
De (C/F/K): C
Para (C/F/K): F

Resultado: 212.0°F
```

### Example — Compound Interest

```
Capital inicial (R$): 1000
Taxa anual (%): 10
Tempo (anos): 2

Montante final: R$ 1210.00
Juros gerados:  R$ 210.00
```

## Project Structure

```
math-tools-cs50p/
├── project.py          # Main program (5 functions + main())
├── test_project.py     # 30 pytest tests (6 per function)
└── requirements.txt    # No external dependencies
```

## Running Tests

```bash
# With venv
venv/bin/pytest test_project.py -v

# Or directly if pytest is installed globally
pytest test_project.py -v
```

All 30 tests pass.

## Functions

- **`convert_temperature(value, from_scale, to_scale)`** — validates scales (`C`/`F`/`K`), converts via Celsius pivot, raises `ValueError` for absolute zero violations
- **`calculate_bmi(weight_kg, height_m)`** — validates positive inputs, returns `(bmi, classification)` tuple
- **`convert_base(number, from_base, to_base)`** — supports bases `{2, 8, 10, 16}`, raises `ValueError` on invalid digit for given base
- **`compound_interest(principal, rate, time)`** — formula `P * (1 + r/100) ^ t`, returns rounded float
- **`basic_statistics(numbers)`** — requires ≥2 elements, returns `{mean, median, stdev}` dict

## Requirements

Python 3.10+ (uses `tuple[...]` and `list[...]` type hints in function signatures).
