def get_numbers():
    while True:
        try:
            number1 = float(input("Enter your first number: "))
            number2 = float(input("Enter your second number: "))
        except ValueError:
            print("Invalid number.")
            continue
        else:
            return number1, number2

def main():
    while True:
        number1, number2 = get_numbers()

        while True:
            operator = input("Enter an operator (+, -, *, /): ")

            match operator:
                case "+":
                    result = number1 + number2
                case "-":
                    result = number1 - number2
                case "*":
                    result = number1 * number2
                case "/":
                    try:
                        result = number1 / number2
                    except ZeroDivisionError:
                        print("Cannot divide by zero.")
                        continue
                case _:
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
