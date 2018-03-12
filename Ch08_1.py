"""

	a program that gets a user's first, middle, and last names,
	then outputs their initials

"""


def main():

	while True:
		first_name = input("Input your first name: ")
		if first_name.isalpha():
			break
		else:
			print("Your input must contain only letters.")
	while True:
		middle_name = input("Input your middle name: ")
		if middle_name.isalpha():
			break
		else:
			print("Your input must contain only letters.")
	while True:
		last_name = input("Input your last name: ")
		if last_name.isalpha():
			break
		else:
			print("Your input must contain only letters.")

	initials = first_name[0].upper() + "." + middle_name[0].upper() + "." + last_name[0].upper() + "."

	print("Your initials are: " + initials)


main()
