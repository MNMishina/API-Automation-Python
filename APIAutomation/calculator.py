#       Simple Calculator

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("What do you want to do with your numbers ? (+, -, *, /)")
simbol = input()

if simbol == "+":
    result = a + b
    print("Result is: " + str(result))
elif simbol == "-":
    result = a - b
    print("Result is: " + str(result))
elif simbol == "*":
    result = a * b
    print("Result is: " + str(result))
elif simbol == "/":
    try:
        result = (a / b)
    except ZeroDivisionError:
        result = 0
        print("Division by zero is permitted")
    print("Result is: " + str(result))
else:
    print("Wrong number (symbol), please enter correct data")
