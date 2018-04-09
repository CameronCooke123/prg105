"""

	A program that has the user enter a number,
	then prints out all positive integers up to that number

"""


def main():
	final_number = int(input("Enter the number you want to count up to: "))
	count_up(final_number, 1)


def count_up(end_num, temp_num):
	print(temp_num)
	temp_num += 1
	if temp_num <= end_num:
		count_up(end_num, temp_num)


main()
