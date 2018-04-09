class Employee:
	def __init__(self, name, number):
		self.__name = name
		self.__number = number

	def set_name(self, new_name):
		self.__name = new_name

	def set_number(self, new_number):
		self.__number = new_number

	def get_name(self):
		return self.__name

	def get_number(self):
		return self.__number

	def __str__(self):
		print_line = " Name: " + self.get_name() + "\n ID Number: " + self.get_number()
		return print_line


class ProductionWorker(Employee):
	def __init__(self, name, number, shift, hourly_pay):
		Employee.__init__(self, name, number)
		self.__shift = shift
		self.__hourly_pay = hourly_pay

	def set_shift(self, new_shift):
		self.__shift = new_shift

	def set_hourly_pay(self, new_pay):
		self.__hourly_pay = new_pay

	def get_shift(self):
		return self.__shift

	def get_hourly_pay(self):
		return self.__hourly_pay

	def __str__(self):
		print_line = Employee.__str__(self)
		print_line += "\n Shift: " + str(self.get_shift()) + "\n Hourly Pay: " + self.get_hourly_pay()
		return print_line
