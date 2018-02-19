"""

    a program that reads numbers from a txt file and outputs their average

"""


def main():
    input_file = open("numbers.txt", "r")

    total = 0
    number_of_numbers = 0

    current_number = input_file.readline()
    current_number = current_number.rstrip("\n")

    while current_number != "":
        current_number = int(current_number)
        total += current_number
        number_of_numbers += 1

        current_number = input_file.readline()
        current_number = current_number.rstrip("\n")

    average = total / number_of_numbers

    print("There are " + str(number_of_numbers) + " numbers in the file.")
    print("The average of the numbers is: " + format(average, ",.2f"))


main()
