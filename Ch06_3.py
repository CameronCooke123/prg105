"""

    a program that checks for bad input

"""


def main():
    filename = "numbers.txt"
    try:
        input_file = open(filename, "r")

        total = 0
        number_of_numbers = 0

        current_number = input_file.readline()
        current_number = current_number.rstrip("\n")

        try:
            current_number = int(current_number)
        except ValueError:
            print("This item is not a number: " + current_number)
            return

        while current_number != "":
            try:
                current_number = int(current_number)
            except ValueError:
                print("This item is not a number: " + current_number)
                return

            total += current_number
            number_of_numbers += 1

            current_number = input_file.readline()
            current_number = current_number.rstrip("\n")

        average = total / number_of_numbers

        print("There are " + str(number_of_numbers) + " numbers in the file.")
        print("The average of the numbers is: " + format(average, ",.2f"))
    except IOError:
        print("Could not find file: " + filename)
        return


main()
