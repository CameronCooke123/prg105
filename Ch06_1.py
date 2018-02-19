"""

    a program that reads names from a txt file and outputs them
    at the end it will output how many names are on the file

"""


def main():
    input_file = open("names.txt", "r")

    number_of_names = 0

    name = input_file.readline()
    name = name.rstrip("\n")
    while name != "":
        print(name)
        name = input_file.readline()
        name = name.rstrip("\n")
        number_of_names += 1

    input_file.close()
    print("Total number of names: " + str(number_of_names))


main()
