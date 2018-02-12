"""

    a program that asks the user for monthly costs of various vehicle expenses,
    then outputs the total monthly cost and yearly cost

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


def main():
    get_monthly_costs()


def get_monthly_costs():
    total_cost = 0

    total_cost += get_int_input_greater_equal_to_value("What is your monthly car loan payment?: ", 0)
    total_cost += get_int_input_greater_equal_to_value("What is your monthly car insurance cost?: ", 0)
    total_cost += get_int_input_greater_equal_to_value("How much do you spend on gas per month?: ", 0)
    total_cost += get_int_input_greater_equal_to_value("How much do you spend on car maintenance per month?: ", 0)

    print("\nTotal monthly cost: " + format(total_cost, '10,.2f'))

    calculate_yearly_costs(total_cost)


def calculate_yearly_costs(total_monthly_cost):
    yearly_cost = total_monthly_cost * 12
    print("Total yearly cost: " + format(yearly_cost, '11,.2f'))


main()
