"""

	a program that asks the user to enter a phone number.
	it then converts any letters into their numerical equivalents.

	A, B, C = 2

	D, E, F = 3

	G, H, I = 4

	J, K, L = 5

	M, N, O = 6

	P, Q, R, S = 7

	T,U, V, = 8

	W, X, Y, Z = 9
"""


number_codes_2 = {"a", "b", "c"}
number_codes_3 = {"d", "e", "f"}
number_codes_4 = {"g", "h", "i"}
number_codes_5 = {"j", "k", "l"}
number_codes_6 = {"m", "n", "o"}
number_codes_7 = {"p", "q", "r", "s"}
number_codes_8 = {"t", "u", "v"}
number_codes_9 = {"w", "x", "y", "z"}


def main():
	original_phone_number = input("Enter a phone number with letters: ")
	original_phone_number = original_phone_number.lower()

	converted_phone_number = str()

	for char in original_phone_number:
		if char.isalpha():
			char = convert_to_number(char)
		converted_phone_number += char

	print(converted_phone_number)


def convert_to_number(letter):
	if number_codes_2.__contains__(letter):
		return "2"
	elif number_codes_3.__contains__(letter):
		return "3"
	elif number_codes_4.__contains__(letter):
		return "4"
	elif number_codes_5.__contains__(letter):
		return "5"
	elif number_codes_6.__contains__(letter):
		return "6"
	elif number_codes_7.__contains__(letter):
		return "7"
	elif number_codes_8.__contains__(letter):
		return "8"
	elif number_codes_9.__contains__(letter):
		return "9"


main()
