"""

	A program that creates 3 instances of a class and displays their data.
	The class holds the following personal data: name, address, age, and phone number.

"""


class User:

	def __init__(self, name, address, age, phone_num):
		self.name = name
		self.address = address
		self.age = age
		self.phone_num = phone_num

	# setters
	def set_name(self, new_name):
		self.name = new_name

	def set_address(self, new_address):
		self.address = new_address

	def set_age(self, new_age):
		self.age = new_age

	def set_phone_num(self, new_num):
		self.phone_num = new_num

	# getters
	def get_name(self):
		return self.name

	def get_address(self):
		return self.address

	def get_age(self):
		return self.age

	def get_phone_num(self):
		return self.phone_num


def main():
	person1 = User("Cameron Cooke", "123 Hello Street", 20, "123-987-4657")
	person2 = User("Brad Cooke", "123 Hello Street", 24, "453-813-6872")
	person3 = User("Mike Cooke", "123 Hello Street", 51, "645-963-1593")

	print(person1.name + "\n" + person1.address + "\nage: " + str(person1.age) + "\nphone number: " + person1.phone_num)
	print("\n\n" + person2.name + "\n" + person2.address + "\nage: " + str(person2.age) + "\nphone number: " + person2.phone_num)
	print("\n\n" + person3.name + "\n" + person3.address + "\nage: " + str(person3.age) + "\nphone number: " + person3.phone_num)


main()
