"""
This is the main menu for the application.

name:<Ruijin Zhang>
semester:<2023 spring>
"""
from enum import Enum
import sys
import csv
from typing import Tuple
from string import punctuation


class Options(Enum):
    """ The options for the menu. """
    EXIT = 1
    LIST = 2
    ADD = 3
    UNKNOWN = 4


def print_welcome() -> None:
    """ Print the welcome message """
    print('Welcome to the Expenses Tracking Application')
    print('This will help you to keep track of what you spend on specific categories. ')
    print()


def print_goodbye() -> None:
    """ Print the goodbye message """
    print('Goodbye')


def print_error(message: str) -> None:
    """ Print an error message
    Args:
        message (str): error message to print
    """
    print(f'Error: {message}', file=sys.stderr)  # file=sys.stderr means to store errors in the file


def get_areas() -> str:
    """
    Ask the user to type the areas they spend on

    Return: the specific category the user spend on
    """
    area = input(f'What is the category you spend on? (Such as: food, travel, cloth, others, new) ')
    return area.strip()  # return the area the client spend on as a string


def get_money(area) -> tuple:
    """
    Ask the user to type the money they expensed
    If the user type the money and the description:  3(money), milk(description)
    If the user only type the money: 3.  food (it will default to the description, if the user type the food first)

    Return: tuple (money, description)
    """
    while True:
        try:
            inp = input(f'How much money did you spend on {area.strip()}? (Money, Description) ')
            if ',' in inp:
                money, area = inp.split(',')
                return int(money.strip()), area.strip()
            else:
                return int(inp.strip()), area.strip()  # return the money and items the client spend on as a tuple
        except ValueError:
            print(f'The money have to be an integer, please type again. ')


def get_list_area() -> str:
    """
    Ask the user what category they want to add.

    Returns: str
    """
    listing = input(f'What category do you want to list? (total or others) ')
    return listing.strip()


def new_category(category):
    """
        Create a new category storing expenses.

        Args:
            category: file name.
    """
    with open(f'{category}.csv', 'w') as file:
        csv.writer(file)


def exist_file(filename):
    """
    Check if there exist this file
    Args:
        filename: to check if it exists
    Return: booleans. True: there exists this file. otherwise, FileNotFoundError.
    """
    try:
        with open(f'{filename}.csv', 'r'):
            return True
    except FileNotFoundError:
        print(f'There is no {filename} category, please type again. or you can type new to create a new category. ')


def list_expenses(category):
    """
    Open the category file and print them out.
    Args:
        category: The user want to list

    Returns: A list of expenses and total sums
    """
    sums = 0
    try:
        with open(f'{category}.csv', 'r') as file:
            contents = csv.reader(file)
            for row in contents:
                money, description = row
                print(f'{description}: ${money}')
                sums += int(money)
            print(f'The {category} expenses is ${sums} in this month. ')
    except FileNotFoundError:
        print(f'There is no {category} category or there are no expenses in {category}, please type again')


def add_expenses(category, money_and_notes):
    """
    Open the category file and add expenses to it

    Args:
        category: Where The user want to add expenses to
        money_and_notes: The expenses the user spend
    """
    try:
        with open(f'{category}.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow(money_and_notes)
    except Exception as e:
        print(f'Error: Failed to save list to file. {str(e)}')


def get_command() -> Options:
    """
    Get the command from the user

    Returns:
    str: command
    """
    command = input('What would you like to do? (add, list, exit) ').strip()
    command = command.lower()
    if command == 'exit':
        return Options.EXIT
    elif command == 'list':
        return Options.LIST
    elif command == 'add':
        return Options.ADD
    else:
        return Options.UNKNOWN
