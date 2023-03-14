# Calculator
from replit import clear
from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)
    another_operation = True
    num1 = float(input("What's the first number?: "))
    for sign in operations:
        print(sign)
    while another_operation:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        should_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")
        if should_continue == "y":
            num1 = answer
        else:
            another_operation = False
            clear()
            calculator()


calculator()
