"""

	A program that allows the user to enter rainfall amounts for 12 months, and assigns those amounts to a list.
	The program then outputs the total rainfall, average rainfall, and months with the most and least rainfall.

"""

MONTHS = ("January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December")


def get_int_input(input_message):
	while True:
		user_input = input(input_message)
		try:
			user_input = int(user_input)
			return user_input
		except ValueError:
			print("Input must be a number.")


def main():
	rainfall = [0] * 12
	total_rainfall = 0

	for month_number in range(0, len(rainfall)):
		rainfall[month_number] = get_int_input("How many inches of rain fell in " + MONTHS[month_number] + "?: ")
		total_rainfall += rainfall[month_number]

	average_rainfall = total_rainfall / 12
	highest_rainfall = rainfall.index(max(rainfall))
	lowest_rainfall = rainfall.index(min(rainfall))

	print("\nThe total rainfall is: " + format(total_rainfall, '6,.2f') + "in.")
	print("The average rainfall is: " + format(average_rainfall, ',.2f') + "in.")
	print("The month with the highest rainfall is " + MONTHS[highest_rainfall] + " with " + format(rainfall[highest_rainfall], ',.2f') + " in.")
	print("The month with the lowest rainfall is " + MONTHS[lowest_rainfall] + " with " + format(rainfall[lowest_rainfall], ',.2f') + " in.")


main()
