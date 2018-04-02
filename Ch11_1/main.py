import office_furniture


def main():
	furniture = office_furniture.OfficeFurniture("Chair", "Metal", "2.5ft", "2.5ft", "3.5ft", "$150.00")
	desk = office_furniture.Desk("Desk", "Wood", "4ft", "8ft", "3ft", "$200.00", "Left", "3")

	print("First Item (parent class):\n", furniture)
	print("Second Item (child class):\n", desk)


main()
