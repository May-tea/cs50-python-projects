def calculate(number1, number2, operator):
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


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number.")


def get_numbers():
    first_number = get_number("Enter your first number: ")
    second_number = get_number("Enter your second number: ")

    return first_number, second_number


def main():
    while True:
        number1, number2 = get_numbers()

        while True:
            operator = input("Enter an operator (+, -, *, /): ")

            result = calculate(number1, number2, operator)

            if result == "division_error":
                print("Cannot divide by zero.")
                continue

            if result == "operator_error":
                print("Invalid operator.")
                continue

            print(f"{number1:g} {operator} {number2:g} = {result:g}")
            break

        while True:
            continue_calculation = input("Do you want to continue? (y/n): ").lower()

            if continue_calculation in ("y", "n"):
                break

            print("Invalid input. Please enter 'y' or 'n'.")

        if continue_calculation == "n":
            print("Goodbye!")
            break


main()
