#       Simple Calculator

a = int(input("Enter first number: "))
symbol = input("What do you want to do with your numbers ? (+, -, *, /): ")
b = int(input("Enter second number: "))

if symbol == "+":
    result = a + b
    print("Result is: " + str(result))
elif symbol == "-":
    result = a - b
    print("Result is: " + str(result))
elif symbol == "*":
    result = a * b
    print("Result is: " + str(result))
elif symbol == "/":
    try:
        result = (a / b)
    except ZeroDivisionError:
        result = 0
        print("Division by zero is permitted")
    print("Result is: " + str(result))
else:
    print("Wrong number (symbol), please enter correct data")
