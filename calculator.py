#ask about the operator then calculate the two variables
while True :
    operator = str(input("Please enter your operator (addition/subtraction/multiplication/division): "))
    if operator not in ["addition", "subtraction", "multiplication", "division"]:
        print("Please enter a valid operator")
        continue
    a = float(input("Please enter your first number: "))
    b = float(input("Please enter your second number: "))
    if operator == "addition":
        result = a + b
        print(f"The addition of {a} and {b} is {result}")
        break
    elif operator == "subtraction":
        result = a - b
        print(f"The subtraction of {a} and {b} is {result}")
        break
    elif operator == "multiplication":
        result = a * b
        print(f"The multiplication of {a} and {b} is {result}")
        break
    elif operator == "division":
        result = a / b
        print(f"The division of {a} and {b} is {result}")
        break