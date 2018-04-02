class OfficeFurniture:

	def __init__(self, category, material, length, width, height, price):
		self.__category = category
		self.__material = material
		self.__length = length
		self.__width = width
		self.__height = height
		self.__price = price

	def set_category(self, new_category):
		self.__category = new_category

	def set_material(self, new_material):
		self.__material = new_material

	def set_length(self, new_length):
		self.__length = new_length

	def set_width(self, new_width):
		self.__width = new_width

	def set_height(self, new_height):
		self.__height = new_height

	def set_price(self, new_price):
		self.__price = new_price

	def get_category(self):
		return self.__category

	def get_material(self):
		return self.__material

	def get_length(self):
		return self.__length

	def get_width(self):
		return self.__width

	def get_height(self):
		return self.__height

	def get_price(self):
		return self.__price

	def __str__(self):
		print_line = "Category: " + self.__category + "\n Material: " + self.__material + "\n Dimensions: "\
					+ self.__length + " x " + self.__width + " x " + self.__height + "\n Price: " + self.__price

		return print_line


class Desk(OfficeFurniture):

	def __init__(self, category, material, length, width, height, price, location_of_drawers, number_of_drawers):
		OfficeFurniture.__init__(self, category, material, length, width, height, price)
		self.__location_of_drawers = location_of_drawers
		self.__number_of_drawers = number_of_drawers

	def set_location_of_drawers(self, new_location):
		self.__location_of_drawers = new_location

	def set_number_of_drawers(self, new_number):
		self.__number_of_drawers = new_number

	def get_location_of_drawers(self):
		return self.__location_of_drawers

	def get_number_of_drawers(self):
		return self.__number_of_drawers

	def __str__(self):
		print_line = "Category: " + self.get_category() + "\n Material: " + self.get_material() + "\n Dimensions: "\
					+ self.get_length() + " x " + self.get_width() + " x " + self.get_height() + "\n Price: " + \
					self.get_price() + "\n Location of Drawers: " + self.__location_of_drawers +\
					"\n Number of Drawers: " + self.__number_of_drawers
		return print_line
