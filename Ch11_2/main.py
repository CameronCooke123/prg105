"""

	A program that gets employee information from the user,
	then creates an object with the employee's information,
	then displays that information using the objects get methods

"""

import employee


def main():
	# get info from user
	name = input("Enter the employee's name: ")
	number = input("Enter the employee's ID number: ")
	shift = int(input("Enter the shift the employee works on: "))
	hourly_pay = float(input("Enter the employee's hourly pay: "))

	# assign info to ProductionWorker object
	worker = employee.ProductionWorker(name, number, shift, hourly_pay)

	# display the worker's info
	print("\nThe employee's name is " + worker.get_name())
	print("The employee's ID number is " + worker.get_number())
	print("The employee works on shift #" + str(worker.get_shift()))
	print("The employee's hourly pay is " + format(worker.get_hourly_pay(), '.2f'))


main()
