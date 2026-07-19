def main():
    while True:
        while True:
            try:
                number1 = float(input("Enter your first number: "))
                number2 = float(input("Enter your second number: "))

                number1 / number2
            except ValueError:
                print("Invalid number.")
                continue
            except ZeroDivisionError:
                print("Cannot divide by zero.")
                continue
            else:
                break

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
                    result = number1 / number2
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
