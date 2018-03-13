"""

	a program that reads names from two txt files,
	then asks the user to input a name,
	then tells them if the name that was input is on either of the lists

"""


def main():
	boy_names, girl_names = read_files()
	user_input = input("Enter a name: ")
	find_name_in_file(user_input, boy_names, girl_names)


def read_files():
	boy_file = open("BoyNames.txt", 'r')
	girl_file = open("GirlNames.txt", 'r')

	boys_names = []

	line = boy_file.readline()
	line = line.strip("\n")
	while line != "":
		boys_names.append(line)
		line = boy_file.readline()
		line = line.strip("\n")

	girls_names = []

	line = girl_file.readline()
	line = line.strip("\n")
	while line != "":
		girls_names.append(line)
		line = girl_file.readline()
		line = line.strip("\n")

	boy_file.close()
	girl_file.close()

	return boys_names, girls_names


def find_name_in_file(user_name, boy_list, girl_list):
	if user_name in boy_list:
		print(user_name + " was found on the popular boys' names list.")
	elif user_name in girl_list:
		print(user_name + " was found on the popular girls' names list.")
	else:
		print(user_name + " was not found in the popular names lists.")


main()
