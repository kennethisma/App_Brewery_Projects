def add(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

num1 = int(input("What's the first number?: "))

for k in operations:
    print(k)

operator_chosed = input("Wich operator do you want?: ")
num2 = int(input("What's the second number?: "))

function = operations[operator_chosed]

answer = function(num1, num2)

print(f"{num1} {operator_chosed} {num2} = {answer} ")
