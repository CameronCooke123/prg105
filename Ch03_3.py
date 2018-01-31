"""

    a program that asks the user their age.
    it then tells them if they are an infant, child, teenager, or adult

"""

user_input = input("Enter your age in years: ")

try:
    user_input = float(user_input)
    if user_input < 0:
        print("You haven't been born yet!")
    elif user_input < 1:
        print("You are an infant.")
    elif user_input < 13:
        print("You are a child.")
    elif user_input < 20:
        print("You are a teenager.")
    else:
        print("You are an adult.")
except ValueError:
    print("You must enter a number.")
