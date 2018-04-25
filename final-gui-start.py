"""
	Creating  a CRUD (Create, Read, Update, Delete) program
	with a GUI interface
"""

import tkinter
import tkinter.messagebox


class CrudGUI:
	def __init__(self):
		self.radio_var = 0
		self.main_window = tkinter.Tk()

		self.top_frame = tkinter.Frame(self.main_window)
		self.bottom_frame = tkinter.Frame(self.main_window)

		self.radio_var = tkinter.IntVar()
		self.radio_var.set(1)

		# create the radio buttons
		self.look = tkinter.Radiobutton(self.top_frame, text='Look up customer',
		                                variable=self.radio_var, value=1)
		self.add = tkinter.Radiobutton(self.top_frame, text='Add Customer',
		                               variable=self.radio_var, value=2)
		self.change = tkinter.Radiobutton(self.top_frame, text='Change customer email',
		                                  variable=self.radio_var, value=3)
		self.delete = tkinter.Radiobutton(self.top_frame, text='Delete customer',
		                                  variable=self.radio_var, value = 4)

		# pack the radio buttons
		self.look.pack()
		self.add.pack()
		self.change.pack()
		self.delete.pack()

		# create ok and quit buttons
		self.ok_button = tkinter.Button(self.bottom_frame, text='OK', command = self.open_menu)
		self.quit_button = tkinter.Button(self.bottom_frame, text='QUIT', command=self.main_window.destroy)

		# pack the buttons
		self.ok_button.pack(side='left')
		self.quit_button.pack(side='left')

		# pack the frames
		self.top_frame.pack()
		self.bottom_frame.pack()

		tkinter.mainloop()

	def open_menu(self):
		if self.radio_var.get() == 1:
			search = LookGUI()
		elif self.radio_var.get() == 2:
			add = AddGUI()
		elif self.radio_var.get() == 3:
			change = ChangeGUI()
		elif self.radio_var.get() == 4:
			delete = DeleteGUI()
		else:
			tkinter.messagebox.showinfo('Function','still under construction')


class LookGUI:
	def __init__(self):
		self.main_window = tkinter.Tk()
		self.top_frame = tkinter.Frame(self.main_window)
		self.bottom_frame = tkinter.Frame(self.main_window)

		# widgets for top frame
		self.search_label = tkinter.Label(self.top_frame, text='Enter customer name to look for: ')
		self.search_entry = tkinter.Entry(self.top_frame, width=25)

		# pack top frame
		self.search_label.pack()
		self.search_entry.pack()

		# buttons for bottom frame
		self.search_button = tkinter.Button(self.bottom_frame, text='Search', command=self.search)
		self.quit_button = tkinter.Button(self.bottom_frame, text='QUIT', command=self.main_window.destroy)

		# pack bottom frame
		self.search_button.pack(side='left')
		self.quit_button.pack(side='left')

		# pack frames
		self.top_frame.pack()
		self.bottom_frame.pack()
		
		tkinter.mainloop()

	def search(self):
		tkinter.messagebox.showinfo('Search', 'function activated')


class AddGUI:
	def __init__(self):
		self.main_window = tkinter.Tk()
		self.top_frame = tkinter.Frame(self.main_window)
		self.bottom_frame = tkinter.Frame(self.main_window)

		# widgets for top frame
		self.name_label = tkinter.Label(self.top_frame, text='Enter customer name to add: ')
		self.name_entry = tkinter.Entry(self.top_frame, width=25)

		self.email_label = tkinter.Label(self.top_frame, text="Enter customer email to add: ")
		self.email_entry = tkinter.Entry(self.top_frame, width=25)

		# pack top frame
		self.name_label.pack()
		self.name_entry.pack()

		self.email_label.pack()
		self.email_entry.pack()

		# buttons for bottom frame
		self.add_button = tkinter.Button(self.bottom_frame, text='Add', command=self.add)
		self.quit_button = tkinter.Button(self.bottom_frame, text='QUIT', command=self.main_window.destroy)

		# pack bottom frame
		self.add_button.pack(side='left')
		self.quit_button.pack(side='left')

		# pack frames
		self.top_frame.pack()
		self.bottom_frame.pack()

		tkinter.mainloop()

	def add(self):
		tkinter.messagebox.showinfo('Add new customer', 'function activated')


class ChangeGUI:
	def __init__(self):
		self.main_window = tkinter.Tk()
		self.top_frame = tkinter.Frame(self.main_window)
		self.bottom_frame = tkinter.Frame(self.main_window)

		# widgets for top frame
		self.change_label = tkinter.Label(self.top_frame, text='Enter customer name to edit: ')
		self.change_entry = tkinter.Entry(self.top_frame, width=25)

		# pack top frame
		self.change_label.pack()
		self.change_entry.pack()

		# buttons for bottom frame
		self.change_button = tkinter.Button(self.bottom_frame, text='Edit', command=self.change)
		self.quit_button = tkinter.Button(self.bottom_frame, text='QUIT', command=self.main_window.destroy)

		# pack bottom frame
		self.change_button.pack(side="left")
		self.quit_button.pack(side="left")

		# pack frames
		self.top_frame.pack()
		self.bottom_frame.pack()

		tkinter.mainloop()

	def change(self):
		tkinter.messagebox.showinfo('Change email', 'function activated')


class DeleteGUI:
	def __init__(self):
		self.main_window = tkinter.Tk()
		self.top_frame = tkinter.Frame(self.main_window)
		self.bottom_frame = tkinter.Frame(self.main_window)

		# widgets for top frame
		self.delete_label = tkinter.Label(self.top_frame, text='Enter customer name to delete: ')
		self.delete_entry = tkinter.Entry(self.top_frame, width=25)

		# pack top frame
		self.delete_label.pack()
		self.delete_entry.pack()

		# buttons for bottom frame
		self.delete_button = tkinter.Button(self.bottom_frame, text='Delete', command=self.delete)
		self.quit_button = tkinter.Button(self.bottom_frame, text='QUIT', command=self.main_window.destroy)

		# pack bottom frame
		self.delete_button.pack(side="left")
		self.quit_button.pack(side="left")

		# pack frames
		self.top_frame.pack()
		self.bottom_frame.pack()

		tkinter.mainloop()

	def delete(self):
		tkinter.messagebox.showinfo('Change email', 'function activated')


crud_gui = CrudGUI()
