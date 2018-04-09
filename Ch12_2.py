"""

	A program that calls a function, sending it a list as its only argument.
	It then calculates and displays the sum of all the numbers in the list

"""


def main():
	add_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


def add_list(num_list):
	# add the first and second numbers
	temp_sum = num_list[0] + num_list[1]
	# assign the sum to the first place
	num_list[0] = temp_sum
	# remove the second place
	num_list.remove(num_list[1])
	# if the list has more than one value in it, call this function again
	if len(num_list) > 1:
		add_list(num_list)
	# if it doesn't, print the result
	else:
		print("Sum: " + str(temp_sum))


main()
