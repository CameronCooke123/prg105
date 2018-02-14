# this is a guessing game that will use hot, warm, and cold to give hints to the user

# import statements will go at the top
# import the random number function

import random

# random numbers are based on a "seed"

# global constants
HOT = 5
WARM = 10
COLD = 15


def main():
    flag = False
    answer = random.randint(1, 100)  # generate random number
    print("hint: " + str(answer))
    while not flag:
        guess = int(input("Please enter a number between 1 and 100:  "))

        result, flag = test(answer, guess)
        print(result)


def test(correct_answer, user_guess):
    if correct_answer == user_guess:
        # flag = True
        return "You Win!", True
    else:
        # absolute value https://docs.python.org/3/library/functions.html
        delta = abs(correct_answer - user_guess)
        if delta <= HOT:
            return "Hot!", False
        elif delta <= WARM:
            return "Warm!", False
        elif delta <= COLD:
            return "Cold!", False
        else:
            return "Freezing!", False


main()
