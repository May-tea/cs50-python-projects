def main():
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

    operator = input("Select an operator (+   -   *   /): ")
        
    print(
        f"First number: {number1:g}\n"
        f"Second number: {number2:g}\n"
        f"Operator: {operator}\n"
    )


main()
