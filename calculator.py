import os
from art import calculator_art

def add(number1, number2):
    return number1 + number2


def substract(number1, number2):
    return number1 - number2


def multiply(number1, number2):
    return number1 * number2


def divide(number1, number2):
    return number1 / number2


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

def get_input_number_from_user(text):
    number = input(f"{text}: ")
    while not number.isnumeric():
        print(f"{number} is not a valid number. Try again")
        number = input(f"{text}: ")
    return float(number)


def get_operation_from_user():
    operation = input("Pick an operation: ")
    while operation not in ['+', '-', '*', '/']:
        print("Please pick a valid operation: + or - or * or/")
        operation = input("Pick an operation: ")
    return operation


def calculator():
    end_program = False
    start_new_calc = True
    number1, number2, result = 0, 0, 0
    while not end_program:
        number1 = result
        if start_new_calc:
            os.system('clear')
            print(calculator_art)
            number1 = get_input_number_from_user("What is the first number?")
        print("+\n-\n*\n/\n")
        action = get_operation_from_user()
        number2 = get_input_number_from_user("What is the next number?")
        result = round(operations[action](number1, number2), 2)
        print(f"\n\n{number1:.1f} {action} {number2:.1f} = {result}\n")
        print(f"Type 'y' to keep calculating with {result},")
        print(f"Type 'n' to start a new calculation,")
        print(f"Type any other character to exit.")
        choice = input("Your choice?: ").lower()
        start_new_calc = choice == 'n'
        end_program = choice not in ['y', 'n']


if __name__ == "__main__":
    calculator()
