"""

    a program that asks the user for the amonut of fat, carbs, and protein they ate for the day and
    tells them how many calories they consumed that day.

"""

import math


# this is called by get_int_input_greater_equal_to_value
def convert_variable_to_int(variable):
    try:
        variable = int(variable)
        return variable
    except ValueError:
        print("Value is not a number.")
        return -math.inf


# this function returns input that is an integer greater than or equal to value.
def get_int_input_greater_equal_to_value(input_text, value):
    while True:
        variable = input(input_text)
        variable = convert_variable_to_int(variable)
        if variable < value and variable != -math.inf:
            print("Value must be greater than or equal to " + str(value) + ".")
        elif variable >= value:
            break

    return variable


total_calories = 0


def get_fat():
    global total_calories
    total_calories += 9 * get_int_input_greater_equal_to_value("How many grams of fat did you eat today?: ", 0)


def get_carbs():
    global total_calories
    total_calories += 4 * get_int_input_greater_equal_to_value("How many grams of carbs did you eat today?: ", 0)


def get_protein():
    global total_calories
    total_calories += 4 * get_int_input_greater_equal_to_value("How many grams of protein did you eat today?: ", 0)


def display_total_calories():
    print("\nTotal calories consumed today: ", total_calories)


def main():
    get_fat()
    get_carbs()
    get_protein()
    display_total_calories()


main()
