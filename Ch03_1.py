"""

    a program that asks the user for a number in the range of 1 through 7. The program should display the corresponding day
    of the week, where 1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday. The
    program should display an error message if the user enters a number that is outside the range of 1 through 7.

"""

user_input = input("Enter a number 1 through 7: ")

try:
    user_input = int(user_input)
    if user_input == 1:
        print("Monday")
    elif user_input == 2:
        print("Tuesday")
    elif user_input == 3:
        print("Wednesday")
    elif user_input == 4:
        print("Thursday")
    elif user_input == 5:
        print("Friday")
    elif user_input == 6:
        print("Saturday")
    elif user_input == 7:
        print("Sunday")
    else:
        print("You must enter a value 1 through 7.")
except ValueError:
    print("You must enter a number.")
