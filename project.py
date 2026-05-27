"""Math Tools — CS50P Final Project
CLI calculator with multiple mathematical utilities.
"""

import math
import statistics
import sys


def convert_temperature(value: float, from_scale: str, to_scale: str) -> float:
    """Convert temperature between Celsius, Fahrenheit, and Kelvin.

    Args:
        value: Temperature value to convert.
        from_scale: Source scale ('C', 'F', or 'K').
        to_scale: Target scale ('C', 'F', or 'K').

    Returns:
        Converted temperature as float.

    Raises:
        ValueError: If scales are invalid or Kelvin result is below absolute zero.
    """
    scales = {"C", "F", "K"}
    from_scale = from_scale.upper().strip()
    to_scale = to_scale.upper().strip()

    if from_scale not in scales or to_scale not in scales:
        raise ValueError(f"Escala inválida. Use: C, F ou K.")

    # Convert to Celsius first
    if from_scale == "C":
        celsius = value
    elif from_scale == "F":
        celsius = (value - 32) * 5 / 9
    else:  # K
        celsius = value - 273.15

    if celsius < -273.15:
        raise ValueError("Temperatura abaixo do zero absoluto (-273.15°C).")

    # Convert from Celsius to target
    if to_scale == "C":
        return round(celsius, 4)
    elif to_scale == "F":
        return round(celsius * 9 / 5 + 32, 4)
    else:  # K
        return round(celsius + 273.15, 4)


def calculate_bmi(weight_kg: float, height_m: float) -> tuple[float, str]:
    """Calculate BMI and return classification.

    Args:
        weight_kg: Weight in kilograms.
        height_m: Height in meters.

    Returns:
        Tuple of (bmi_value, classification_string).

    Raises:
        ValueError: If weight or height are non-positive.
    """
    if weight_kg <= 0:
        raise ValueError("Peso deve ser maior que zero.")
    if height_m <= 0:
        raise ValueError("Altura deve ser maior que zero.")
    if height_m > 3.0:
        raise ValueError("Altura inválida. Informe em metros (ex: 1.75).")

    bmi = weight_kg / (height_m ** 2)
    bmi = round(bmi, 2)

    if bmi < 18.5:
        classification = "Abaixo do peso"
    elif bmi < 25.0:
        classification = "Peso normal"
    elif bmi < 30.0:
        classification = "Sobrepeso"
    elif bmi < 35.0:
        classification = "Obesidade grau I"
    elif bmi < 40.0:
        classification = "Obesidade grau II"
    else:
        classification = "Obesidade grau III"

    return bmi, classification


def convert_base(number: str, from_base: int, to_base: int) -> str:
    """Convert a number between bases 2, 8, 10, and 16.

    Args:
        number: Number as string (e.g. '1010', 'FF', '255').
        from_base: Source base (2, 8, 10, or 16).
        to_base: Target base (2, 8, 10, or 16).

    Returns:
        Converted number as string (uppercase for hex).

    Raises:
        ValueError: If base is unsupported or number is invalid for given base.
    """
    valid_bases = {2, 8, 10, 16}
    if from_base not in valid_bases or to_base not in valid_bases:
        raise ValueError("Base inválida. Use: 2, 8, 10 ou 16.")

    try:
        decimal = int(number.strip(), from_base)
    except ValueError:
        raise ValueError(f"Número '{number}' inválido para base {from_base}.")

    if decimal < 0:
        raise ValueError("Apenas números não-negativos são suportados.")

    if to_base == 2:
        return bin(decimal)[2:]
    elif to_base == 8:
        return oct(decimal)[2:]
    elif to_base == 10:
        return str(decimal)
    else:  # 16
        return hex(decimal)[2:].upper()


def compound_interest(principal: float, rate: float, time: float) -> float:
    """Calculate compound interest final amount.

    Args:
        principal: Initial capital (must be positive).
        rate: Annual interest rate as percentage (e.g. 5.0 for 5%).
        time: Time in years (must be positive).

    Returns:
        Final amount after compound interest.

    Raises:
        ValueError: If any argument is invalid.
    """
    if principal <= 0:
        raise ValueError("Capital inicial deve ser maior que zero.")
    if rate < 0:
        raise ValueError("Taxa de juros não pode ser negativa.")
    if time <= 0:
        raise ValueError("Tempo deve ser maior que zero.")

    amount = principal * (1 + rate / 100) ** time
    return round(amount, 2)


def basic_statistics(numbers: list[float]) -> dict[str, float]:
    """Calculate mean, median, and standard deviation for a list of numbers.

    Args:
        numbers: Non-empty list of numeric values.

    Returns:
        Dict with keys 'mean', 'median', 'stdev'.

    Raises:
        ValueError: If list is empty or has fewer than 2 elements for stdev.
    """
    if not numbers:
        raise ValueError("Lista não pode ser vazia.")
    if len(numbers) < 2:
        raise ValueError("Informe pelo menos 2 números para calcular desvio padrão.")

    return {
        "mean": round(statistics.mean(numbers), 4),
        "median": round(statistics.median(numbers), 4),
        "stdev": round(statistics.stdev(numbers), 4),
    }


def main() -> None:
    """Interactive CLI menu for Math Tools."""
    menu = """
╔══════════════════════════════╗
║        MATH TOOLS            ║
╠══════════════════════════════╣
║  1. Conversor de temperatura ║
║  2. Calculadora de IMC       ║
║  3. Conversor de bases       ║
║  4. Juros compostos          ║
║  5. Estatística básica       ║
║  0. Sair                     ║
╚══════════════════════════════╝
"""
    while True:
        print(menu)
        choice = input("Escolha uma opção: ").strip()

        if choice == "0":
            print("Saindo. Até mais!")
            sys.exit(0)

        elif choice == "1":
            try:
                value = float(input("Valor: "))
                from_scale = input("De (C/F/K): ").strip()
                to_scale = input("Para (C/F/K): ").strip()
                result = convert_temperature(value, from_scale, to_scale)
                print(f"\nResultado: {result}°{to_scale.upper()}")
            except ValueError as e:
                print(f"\nErro: {e}")

        elif choice == "2":
            try:
                weight = float(input("Peso (kg): "))
                height = float(input("Altura (m): "))
                bmi, classification = calculate_bmi(weight, height)
                print(f"\nIMC: {bmi} — {classification}")
            except ValueError as e:
                print(f"\nErro: {e}")

        elif choice == "3":
            base_names = {"2": "binário", "8": "octal", "10": "decimal", "16": "hexadecimal"}
            try:
                number = input("Número: ").strip()
                from_base = int(input("Base de origem (2/8/10/16): "))
                to_base = int(input("Base destino (2/8/10/16): "))
                result = convert_base(number, from_base, to_base)
                print(f"\nResultado ({base_names.get(str(to_base), str(to_base))}): {result}")
            except ValueError as e:
                print(f"\nErro: {e}")

        elif choice == "4":
            try:
                principal = float(input("Capital inicial (R$): "))
                rate = float(input("Taxa anual (%): "))
                time = float(input("Tempo (anos): "))
                amount = compound_interest(principal, rate, time)
                interest = round(amount - principal, 2)
                print(f"\nMontante final: R$ {amount:.2f}")
                print(f"Juros gerados:  R$ {interest:.2f}")
            except ValueError as e:
                print(f"\nErro: {e}")

        elif choice == "5":
            try:
                raw = input("Números separados por vírgula: ")
                numbers = [float(n.strip()) for n in raw.split(",")]
                stats = basic_statistics(numbers)
                print(f"\nMédia:           {stats['mean']}")
                print(f"Mediana:         {stats['median']}")
                print(f"Desvio padrão:   {stats['stdev']}")
            except ValueError as e:
                print(f"\nErro: {e}")

        else:
            print("Opção inválida. Escolha entre 0 e 5.")

        input("\nPressione Enter para continuar...")


if __name__ == "__main__":
    main()
