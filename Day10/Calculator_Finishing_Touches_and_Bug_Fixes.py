from art import logo

print(logo)


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


def calculator():

    num1 = int(float(input("What's the first number?: ")))
    wants_continue = True

    while wants_continue:
        for k in operations:
            print(k)

        operator_chosed = input("Wich operator do you want?: ")
        num2 = int(float(input("What's the next the number?: ")))
        function = operations[operator_chosed]
        answer = function(num1, num2)

        print(f"{num1} {operator_chosed} {num2} = {answer} ")

        keep_calculating = input(
            f"Type 'y' to continue calculating with {answer},'n'  to start a new calculation: ")

        if keep_calculating == 'y':
            num1 = answer
        elif keep_calculating == 'n':
            wants_continue = False
            calculator()
        else:
            break


calculator()
