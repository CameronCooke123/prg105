"""

    a program that asks the user to input 5 grades, calculates the average of those grades,
    and outputs the corresponding letter grade.

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
def get_int_input_between_values(input_text, min_value, max_value):
    while True:
        variable = input(input_text)
        variable = convert_variable_to_int(variable)
        if (variable < min_value or variable > max_value) and variable != -math.inf:
            print("Value must be between " + str(min_value) + " and " + str(max_value) + ".")
        elif min_value <= variable <= max_value:
            break

    return variable


def main():
    # get five test scores from the user
    score1 = get_int_input_between_values("Enter your first test score: ", 0, 100)
    score2 = get_int_input_between_values("Enter your second test score: ", 0, 100)
    score3 = get_int_input_between_values("Enter your third test score: ", 0, 100)
    score4 = get_int_input_between_values("Enter your fourth test score: ", 0, 100)
    score5 = get_int_input_between_values("Enter your fifth test score: ", 0, 100)
    # calculate the average
    average = calc_average(score1, score2, score3, score4, score5)
    # determine the letter grade
    final_letter_grade = determine_grade(average)
    # print the average score and letter grade
    print("Your average score is: " + format(average, '.1f'))
    print("Your final letter grade is: " + final_letter_grade)


# calculates the average of five scores
def calc_average(first_score, second_score, third_score, fourth_score, fifth_score):
    return (first_score + second_score + third_score + fourth_score + fifth_score) // 5


# determines the final letter grade
def determine_grade(average_score):
    if average_score >= 90:
        return "A"
    elif average_score >= 80:
        return "B"
    elif average_score >= 70:
        return "C"
    elif average_score >= 60:
        return "D"
    else:
        return "F"


main()
