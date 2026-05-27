"""Tests for Math Tools — CS50P Final Project."""

import pytest
from project import (
    convert_temperature,
    calculate_bmi,
    convert_base,
    compound_interest,
    basic_statistics,
)


# ── Temperature ──────────────────────────────────────────────────────────────

def test_convert_temperature_celsius_to_fahrenheit():
    assert convert_temperature(0, "C", "F") == 32.0
    assert convert_temperature(100, "C", "F") == 212.0
    assert convert_temperature(-40, "C", "F") == -40.0


def test_convert_temperature_fahrenheit_to_celsius():
    assert convert_temperature(32, "F", "C") == 0.0
    assert convert_temperature(212, "F", "C") == 100.0


def test_convert_temperature_celsius_to_kelvin():
    assert convert_temperature(0, "C", "K") == 273.15
    assert convert_temperature(-273.15, "C", "K") == 0.0


def test_convert_temperature_same_scale():
    assert convert_temperature(37, "C", "C") == 37.0


def test_convert_temperature_invalid_scale():
    with pytest.raises(ValueError):
        convert_temperature(100, "X", "C")
    with pytest.raises(ValueError):
        convert_temperature(100, "C", "Z")


def test_convert_temperature_below_absolute_zero():
    with pytest.raises(ValueError):
        convert_temperature(-300, "C", "F")


# ── BMI ──────────────────────────────────────────────────────────────────────

def test_calculate_bmi_normal_weight():
    bmi, classification = calculate_bmi(70, 1.75)
    assert bmi == pytest.approx(22.86, abs=0.01)
    assert classification == "Peso normal"


def test_calculate_bmi_underweight():
    bmi, classification = calculate_bmi(45, 1.70)
    assert classification == "Abaixo do peso"


def test_calculate_bmi_obese():
    bmi, classification = calculate_bmi(120, 1.70)
    assert classification == "Obesidade grau III"  # 120/1.70² = 41.5 → grau III (≥40)


def test_calculate_bmi_invalid_weight():
    with pytest.raises(ValueError):
        calculate_bmi(0, 1.75)
    with pytest.raises(ValueError):
        calculate_bmi(-10, 1.75)


def test_calculate_bmi_invalid_height():
    with pytest.raises(ValueError):
        calculate_bmi(70, 0)
    with pytest.raises(ValueError):
        calculate_bmi(70, -1.0)
    with pytest.raises(ValueError):
        calculate_bmi(70, 175)  # altura em cm, não metros


# ── Base conversion ───────────────────────────────────────────────────────────

def test_convert_base_decimal_to_binary():
    assert convert_base("10", 10, 2) == "1010"
    assert convert_base("0", 10, 2) == "0"
    assert convert_base("255", 10, 2) == "11111111"


def test_convert_base_binary_to_decimal():
    assert convert_base("1010", 2, 10) == "10"
    assert convert_base("11111111", 2, 10) == "255"


def test_convert_base_decimal_to_hex():
    assert convert_base("255", 10, 16) == "FF"
    assert convert_base("16", 10, 16) == "10"


def test_convert_base_hex_to_decimal():
    assert convert_base("FF", 16, 10) == "255"
    assert convert_base("ff", 16, 10) == "255"


def test_convert_base_invalid_base():
    with pytest.raises(ValueError):
        convert_base("10", 3, 10)
    with pytest.raises(ValueError):
        convert_base("10", 10, 5)


def test_convert_base_invalid_number_for_base():
    with pytest.raises(ValueError):
        convert_base("2", 2, 10)  # '2' não existe em base 2
    with pytest.raises(ValueError):
        convert_base("GG", 16, 10)  # 'G' não é hex válido


# ── Compound interest ─────────────────────────────────────────────────────────

def test_compound_interest_basic():
    result = compound_interest(1000, 10, 1)
    assert result == 1100.0


def test_compound_interest_multiple_years():
    result = compound_interest(1000, 10, 2)
    assert result == pytest.approx(1210.0, abs=0.01)


def test_compound_interest_zero_rate():
    result = compound_interest(1000, 0, 5)
    assert result == 1000.0


def test_compound_interest_invalid_principal():
    with pytest.raises(ValueError):
        compound_interest(0, 10, 1)
    with pytest.raises(ValueError):
        compound_interest(-500, 10, 1)


def test_compound_interest_invalid_time():
    with pytest.raises(ValueError):
        compound_interest(1000, 10, 0)
    with pytest.raises(ValueError):
        compound_interest(1000, 10, -1)


def test_compound_interest_negative_rate():
    with pytest.raises(ValueError):
        compound_interest(1000, -5, 1)


# ── Statistics ────────────────────────────────────────────────────────────────

def test_basic_statistics_mean():
    result = basic_statistics([1, 2, 3, 4, 5])
    assert result["mean"] == 3.0


def test_basic_statistics_median_odd():
    result = basic_statistics([1, 3, 5])
    assert result["median"] == 3.0


def test_basic_statistics_median_even():
    result = basic_statistics([1, 2, 3, 4])
    assert result["median"] == 2.5


def test_basic_statistics_stdev():
    result = basic_statistics([2, 4, 4, 4, 5, 5, 7, 9])
    assert result["stdev"] == pytest.approx(2.1381, abs=0.001)  # sample stdev, not population


def test_basic_statistics_empty_list():
    with pytest.raises(ValueError):
        basic_statistics([])


def test_basic_statistics_single_element():
    with pytest.raises(ValueError):
        basic_statistics([42])


def test_basic_statistics_negative_numbers():
    result = basic_statistics([-5, -3, -1, 0, 1, 3, 5])
    assert result["mean"] == 0.0
