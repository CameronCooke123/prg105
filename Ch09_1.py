"""

    A program that is essentially a database for holding peoples' names and email addresses.
    When the program is running, the user can look up email addresses if they have the name, add a new name & email,
    edit email addresses, and delete names & email addresses.
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
            try:
                email_address = editable_dict[user_input]
                print(email_address)
            except:
                print("That name does not exist in this database.")

        elif user_input == "2":
            new_name = input("Enter the name: ")
            new_address = input("Enter the email address: ")

            editable_dict[new_name] = new_address

        elif user_input == "3":
            existing_name = input("Enter the name: ")
            new_email = input("Enter the new email address: ");

            editable_dict[existing_name] = new_email

        elif user_input == "4":
            name_to_delete = input("Enter the name to delete: ")

            del editable_dict[name_to_delete]

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
    ()


main()
