"""

	A program that calculates miles per gallon.
	It has the user enter the number of gallons of gas the car's tank can hold,
	and enter the number of miles the car can be driven on a full tank.
	It then displays the miles per gallon.

"""


import tkinter


class Window:

	def __init__(self):
		self.main_window = tkinter.Tk()

		# entry section:

		# tank capacity label & entry
		self.tank_capacity_frame = tkinter.Frame(self.main_window)

		self.tank_capacity_label = tkinter.Label(self.tank_capacity_frame, text="Tank capacity (gallons):")
		self.tank_capacity_entry = tkinter.Entry(self.tank_capacity_frame, width=5)

		self.tank_capacity_label.pack(side="left")
		self.tank_capacity_entry.pack(side="right")

		# miles label & entry
		self.miles_frame = tkinter.Frame(self.main_window)

		self.miles_label = tkinter.Label(self.miles_frame, text="Miles that can be driven on a full tank:")
		self.miles_entry = tkinter.Entry(self.miles_frame, width=5)

		self.miles_label.pack(side="left")
		self.miles_entry.pack(side="right")

		# buttons section:
		self.buttons_frame = tkinter.Frame(self.main_window)

		self.calculate_button = tkinter.Button(self.buttons_frame, text="Calculate MPG", command=self.calculate)
		self.calculate_button.pack(side="left")

		self.quit_button = tkinter.Button(self.buttons_frame, text="Quit", command=self.main_window.destroy)
		self.quit_button.pack(side="right")

		# final display section:
		self.display_frame = tkinter.Frame(self.main_window)

		self.final_display = tkinter.StringVar(value="")
		self.display_label = tkinter.Label(self.display_frame, textvariable=self.final_display)

		self.display_label.pack()

		# pack all the frames
		self.tank_capacity_frame.pack()
		self.miles_frame.pack()
		self.buttons_frame.pack()
		self.display_frame.pack()

		self.main_window.mainloop()

	def calculate(self):
		capacity = float(self.tank_capacity_entry.get())
		miles = float(self.miles_entry.get())

		efficiency = miles / capacity
		output = format(efficiency, '.2f') + " MPG"

		self.final_display.set(output)


window = Window()
