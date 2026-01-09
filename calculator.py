#Python Simple Calculator
while True:
    operator = input("Enter an operator (+ - * /) or q to quit: ")

    if operator == "q":
        print("Goodbye!")
        break

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if operator == "+":
        print(round(num1 + num2))
    elif operator == "-":
        print(round(num1 - num2))
    elif operator == "*":
        print(round(num1 * num2))
    elif operator == "/":
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            print(round(num1 / num2, 2))
    else:
        print("Invalid operator")
