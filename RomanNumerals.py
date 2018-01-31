"""

    a program that prompts the user to enter a value 1 through 10.
    the roman numeral equivalent is then output.

"""

user_input = input("Enter a number 1 through 10: ")

try:
    user_input = int(user_input)
    if user_input == 1:
        print("I")
    elif user_input == 2:
        print("II")
    elif user_input == 3:
        print("III")
    elif user_input == 4:
        print("IV")
    elif user_input == 5:
        print("V")
    elif user_input == 6:
        print("VI")
    elif user_input == 7:
        print("VII")
    elif user_input == 8:
        print("VIII")
    elif user_input == 9:
        print("IX")
    elif user_input == 10:
        print("X")
    else:
        print("You must enter a value 1 through 10.")
except ValueError:
    print("You must enter a number.")
