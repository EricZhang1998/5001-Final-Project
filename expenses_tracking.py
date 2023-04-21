"""
Expenses Tracking Apllication

name:<Ruijin Zhang>
semester:<2023 spring>
"""
import menu
from typing import Union


def handle_list():
    """
        Get listing area from the user.
    """
    area = menu.get_list_area()
    if area == 'total':
        menu.list_expenses('total')
    else:
        menu.list_expenses(area)


def handle_add():
    """
    Get adding area from the user.
    Get the expenses and adding them to specific category
    """
    area = menu.get_areas()
    if area != 'new':
        if area == 'food' or area == 'travel' or area == 'cloth' or area == 'others':
            money_and_note = menu.get_money(area)
            menu.add_expenses(area, money_and_note)
            menu.add_expenses('total', money_and_note)
        else:
            if menu.exist_file(area):
                money_and_note = menu.get_money(area)
                menu.add_expenses(area, money_and_note)
                menu.add_expenses('total', money_and_note)
    else:  # new means to creat a new list or category to store expenses
        new_category = input(f'What category do you want to add? ')
        menu.new_category(new_category)
        print(f'{new_category} category is created. you can add expenses to {new_category} now. ')


def main():
    """
    This is the main entry point for the application.
    """
    menu.print_welcome()
    command = menu.get_command()
    while command != menu.Options.EXIT:
        if command == menu.Options.LIST:
            handle_list()
        elif command == menu.Options.ADD:
            handle_add()
        elif command != menu.Options.UNKNOWN and command != menu.Options.EXIT:
            menu.print_error("Make sure to type correct operation.")
        command = menu.get_command()
    menu.print_goodbye()


if __name__ == "__main__":
    main()
