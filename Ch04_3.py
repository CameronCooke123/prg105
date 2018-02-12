"""

    a program that calculates the total rainfall and average rainfall per month
    over a user-specified period of time

"""

import math


def convert_variable_to_int(variable):
    try:
        variable = int(variable)
        return variable
    except ValueError:
        print("Value is not a number.")
        return -math.inf


# this function will return an integer greater than or equal to value
def get_int_input_greater_equal_to_value(input_text, value):
    while True:
        variable = input(input_text)
        variable = convert_variable_to_int(variable)
        if variable < value and variable != -math.inf:
            print("Value must be greater than or equal to " + str(value) + ".")
        elif variable >= value:
            break

    return variable


months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
total_rain_fall = 0
number_of_years = get_int_input_greater_equal_to_value("How many years do you have data for?: ", 1)

for year in range(0, number_of_years):
    for month in range(0, 12):
        inches_fell_text = str("How many inches of rain fell in " + months[month] + " of year " + str(year + 1) + "?: ")
        inches_of_rain_this_month = get_int_input_greater_equal_to_value(inches_fell_text, 0)
        total_rain_fall += inches_of_rain_this_month

number_of_months = number_of_years * 12
average_rain_per_month = total_rain_fall / number_of_months  # I'm assuming this is to be a float

print("\nTotal number of months: " + format(number_of_months, '11,'))
print("Total rain fall: " + format(total_rain_fall, '18,') + " in.")
print("Average rain fall per month: " + format(average_rain_per_month, '6,.2f') + " in.")
