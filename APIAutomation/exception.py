a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

try:
    result = int(a / b)
except ZeroDivisionError:
    result = 0
    print("Division by zero is permitted")
print("Result is: " + str(result))
