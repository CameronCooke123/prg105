"""

	A program that is essentially a database for holding peoples' names and email addresses.
	When the program is running, the user can look up email addresses if they have the name, add a new name & email,
	edit existing email addresses, and delete names & email addresses.
	The data is saved within a dictionary while the program is running, and is saved to a file when it's not running.

"""


def main():
	# read data from file
	dictionary = read_data_from_file()
	# go into menu loop
	dictionary = main_menu_loop(dictionary)
	# save and exit
	save_data_to_file(dictionary)


def main_menu_loop(editable_dict):
	while True:
		print("\nSelect an option: ")
		print("1: Look up email address by name")
		print("2: Add new name & email")
		print("3: Edit existing email address")
		print("4: Delete email address by name")
		print("5: Save and exit")
		user_input = input()

		if user_input == "1":
			name = get_name("Enter the name: ")

			if name in editable_dict:
				print("\nName found. Email address is: " + editable_dict[name])
			else:
				print("\nName not found in database.")

		elif user_input == "2":
			new_name = get_name("Enter the name: ")
			if new_name in editable_dict:
				print("\nName already found in database.")
			else:
				new_address = input("Enter the email address: ")
				editable_dict[new_name] = new_address

				print("\nName & email address successfully added.")

		elif user_input == "3":
			existing_name = get_name("Enter the name: ")
			if existing_name in editable_dict:
				new_email = input("Enter the new email address: ")
				editable_dict[existing_name] = new_email

				print("\nEmail address successfully updated.")
			else:
				print("\nName not found in database.")

		elif user_input == "4":
			name_to_delete = get_name("Enter the name to delete: ")
			if name_to_delete in editable_dict:
				del editable_dict[name_to_delete]

				print("\nName & email address successfully deleted.")
			else:
				print("\nName not found in database.")

		else:
			break

	return editable_dict


def read_data_from_file():
	temp_dictionary = {}

	try:
		file = open("SaveFile.txt", "r")

		line = file.readline()
		line = line.strip("\n")

		while line != "":
			# separate the name from the email address
			words = line.split()

			name = words[0]
			address = words[1]

			temp_dictionary[name] = address

			line = file.readline()
			line = line.strip("\n")

		file.close()
		return temp_dictionary

	except FileNotFoundError:
		return temp_dictionary


def save_data_to_file(final_dictionary):
	# open the file, create it if it doesn't exist
	file = open("SaveFile.txt", "w+")

	# write the date to the file
	for key, value in final_dictionary.items():
		file.write(key + " " + value)

	file.close()


def get_name(text):
	entered_name = input(text)

	# remove any spaces from the name and make all the letters lowercase
	entered_name = entered_name.replace(" ", "")
	entered_name = entered_name.lower()

	return entered_name


main()
