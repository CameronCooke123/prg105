"""

    a program that asks the user for a number of days, and tells them how much money they would earn if
    they earned one penny on the first day, two pennies on the second day, four pennies on the third day, etc.

"""


def convert_variable_to_int(variable):
    try:
        variable = int(variable)
        return variable
    except ValueError:
        print("Value is not a number.")
        return -1
        # it's not ideal to have this return -1,
        # but I'm not sure what else I could return here that would cover all my bases.


number_of_days = 0

while number_of_days <= 0:
    number_of_days = input("\nHow many days will you work for pennies a day?: ")
    number_of_days = convert_variable_to_int(number_of_days)
    if number_of_days <= 0:
        print("Value must be greater than zero.")

print("\nDays worked | Amount earned that day\n")

total_amount_earned = 0

for current_day in range(0, number_of_days, 1):
    # calculate the amount earned on that day
    amount_earned_this_day = 0.01 * (2 ** current_day)
    total_amount_earned += amount_earned_this_day
    # display the data
    print(format(current_day + 1, '11') + " | $" + format(amount_earned_this_day, '15,.2f'))

print("\nTotal amount earned: " + format(total_amount_earned, ',.2f'))
