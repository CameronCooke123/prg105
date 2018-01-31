"""

    a program that asks the user which phone plan they have and how many minutes they've used.
    it then tells them the amount owed on their bill.

"""

PLAN_A_BASE_COST = 39.99
PLAN_B_BASE_COST = 59.99
PLAN_C_BASE_COST = 69.99

PLAN_A_MAX_MINS = 450
PLAN_B_MAX_MINS = 900

PLAN_A_MINS_OVER_MULT = 0.45
PLAN_B_MINS_OVER_MULT = 0.4


def convert_variable_to_float(variable):
    try:
        variable = float(variable)
        return variable
    except ValueError:
        print("Value is not a number.")
        return -1.0


def display_amount_owed():
    print("Amount owed: $" + format(amount_owed, '.2f'))


phone_plan = input("Enter which plan you have (A, B, or C): ")
amount_owed = 0

if phone_plan == "a" or phone_plan == "A":
    amount_owed += PLAN_A_BASE_COST
    minutes_used = input("Enter the amount of minutes used: ")

    minutes_used = convert_variable_to_float(minutes_used)
    if minutes_used < 0:
        print("Invalid input. 0 minutes used will be assumed.")
        minutes_used = 0.0

    if minutes_used > PLAN_A_MAX_MINS:
        minutes_over = minutes_used - PLAN_A_MAX_MINS
        amount_owed += minutes_over * PLAN_A_MINS_OVER_MULT

    display_amount_owed()

elif phone_plan == "b" or phone_plan == "B":
    amount_owed += PLAN_B_BASE_COST
    minutes_used = input("Enter the amount of minutes used: ")

    minutes_used = convert_variable_to_float(minutes_used)
    if minutes_used < 0:
        print("Invalid input. 0 minutes used will be assumed.")
        minutes_used = 0.0

    if minutes_used > PLAN_B_MAX_MINS:
        minutes_over = minutes_used - PLAN_B_MAX_MINS
        amount_owed += minutes_over * PLAN_B_MINS_OVER_MULT

    display_amount_owed()

elif phone_plan == "c" or phone_plan == "C":
    amount_owed += PLAN_C_BASE_COST
    display_amount_owed()

else:
    print("You must enter a valid answer.")
