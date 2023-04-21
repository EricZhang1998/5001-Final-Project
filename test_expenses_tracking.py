"""
This is the test_expenses_tracking program.

name:<Ruijin Zhang>
semester:<2023 spring>
"""
import csv
import os
from menu import get_money, list_expenses, add_expenses


def test_list_expenses():
    # create a sample csv file for testing
    with open('test.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['10', 'Groceries'])
        writer.writerow(['20', 'Gas'])
        writer.writerow(['30', 'Entertainment'])

    # test the function with the sample csv file
    list_expenses('test')

    # delete the sample csv file
    os.remove('test.csv')


def test_add_expenses():
    # create a sample csv file for testing
    with open('test.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['10', 'Groceries'])

    # test the function by adding an expense to the sample csv file
    add_expenses('test', ['20', 'Gas'])

    # read the csv file to check if the expense was added
    with open('test.csv', 'r') as file:
        contents = csv.reader(file)
        rows = list(contents)
        assert rows == [['10', 'Groceries'], ['20', 'Gas']]

    # delete the sample csv file
    os.remove('test.csv')


# run the test functions
test_list_expenses()
test_add_expenses()
