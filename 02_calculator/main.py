def main():
    number1 = float(input("Enter your first number: "))
    number2 = float(input("Enter your second number: "))
    
    operator = input("Select an operator (+   -   *   /): ")
        
    print(
        f"First number: {number1:g}\n"
        f"Second number: {number2:g}\n"
        f"Operator: {operator}\n"
    )


main()
