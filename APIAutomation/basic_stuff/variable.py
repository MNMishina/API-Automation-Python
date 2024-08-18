var_1 = 100  # global variable
var_2 = 20  # global variable


def summ():
    var_1 = 50  # local variable
    var_2 = 40  # local variable
    result = var_1 + var_2
    print(result)

def substr():
    var_2 = 30
    result = var_1 - var_2
    print(result)

print(var_1, var_2)
summ()
substr()
