def calculate(number1: float, number2: float, operator: str) -> float | str:
    match operator:
        case "+":
            return number1 + number2
        case "-":
            return number1 - number2
        case "*":
            return number1 * number2
        case "/":
            if number2 == 0:
                return "division_error"

            return number1 / number2
        case _:
            return "operator_error"


def get_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number.")


def get_numbers() -> tuple[float, float]:
    first_number: float = get_number("Enter your first number: ")
    second_number: float = get_number("Enter your second number: ")

    return first_number, second_number


def main() -> None:
    while True:
        number1, number2 = get_numbers()

        while True:
            operator: str = input("Enter an operator (+, -, *, /): ")

            result: float | str = calculate(number1, number2, operator)

            if result == "division_error":
                print("Cannot divide by zero.")
                continue

            if result == "operator_error":
                print("Invalid operator.")
                continue

            print(f"{number1:g} {operator} {number2:g} = {result:g}")
            break

        while True:
            continue_calculation: str = input(
                "Do you want to continue? (y/n): "
            ).lower()

            if continue_calculation in ("y", "n"):
                break

            print("Invalid input. Please enter 'y' or 'n'.")

        if continue_calculation == "n":
            print("Goodbye!")
            break


main()
