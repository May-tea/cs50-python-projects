def main():
    while True:
        try:
            number1 = float(input("Enter your first number: "))
            number2 = float(input("Enter your second number: "))
        except ValueError:
            print("Invalid number.")
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
