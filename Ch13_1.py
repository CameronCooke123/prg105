"""

	A program that has the user press a button, then displays an address

"""


import tkinter


class Window:
	def __init__(self):
		self.main_window = tkinter.Tk()

		self.top_frame = tkinter.Frame(self.main_window)

		self.address = tkinter.StringVar(value="\n\n")
		self.address_label = tkinter.Label(self.top_frame, textvariable=self.address)
		self.address_label.pack()

		self.top_frame.pack()

		self.bottom_frame = tkinter.Frame(self.main_window)

		self.show_info_button = tkinter.Button(self.bottom_frame, text="Show Info", command=self.show_info)
		self.show_info_button.pack(side="left")

		self.quit_button = tkinter.Button(self.bottom_frame, text="Quit", command=quit)
		self.quit_button.pack(side="left")

		self.bottom_frame.pack()

		self.main_window.mainloop()

	def show_info(self):
		self.address.set("Cameron Cooke\n1234 Street Road\nSpring Grove, IL, 60081")


window_instance = Window()
