"""

	A program that raises one number to the power of another

"""


def main():
	# display what the program does
	print("This program will raise a base number to the power of an exponent.")
	# get the base number from the user
	base_num = int(input("Enter the base number: "))
	# get the power from the user
	exponent_num = int(input("Enter the exponent: "))
	# call the function
	power(base_num, exponent_num, base_num)


def power(base, exponent, temp):
	# multiply the running value(temp) by the base
	# (temp needs to be the same as base when the function is initially called)
	temp *= base
	# exponent is acting as a counter here
	exponent -= 1

	if exponent > 1:
		power(base, exponent, temp)
	else:
		print("The result is: " + str(temp))


main()
