"""

	a program that creates a list of 20 random integers between 1 and 100.
	it then gets a number from the user between 1 and 100 .
	the program then displays all the numbers in the list that are greater than the user's number.
	if there aren't any, a special message displays.

"""
import random


def main():
	numbers = create_list()
	guess = get_number_from_user()
	calc_disp_output(numbers, guess)


def create_list():
	list_of_numbers = [0] * 100
	index = 0
	while index < len(list_of_numbers):
		list_of_numbers[index] = random.randint(1, 100)
		index += 1
	return list_of_numbers


def get_number_from_user():
	while True:
		user_input = input("Input a number between 1 and 100: ")
		try:
			user_input = int(user_input)
			if 1 <= user_input <= 100:
				break
			else:
				print("Value must be between 1 and 100.")
		except ValueError:
			print("Value must be numerical.")
	return user_input


def calc_disp_output(number_list, user_guess):
	number_list.sort()
	index = 0
	while index < len(number_list):
		if number_list[index] > user_guess:
			break
		index += 1

	if index >= len(number_list) - 1:
		print("No numbers in the list are greater than your input.")
	else:
		sliced_list = number_list[index:]
		print(sliced_list)


main()
