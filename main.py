"""

	This is an application that allows you to save words that correspond to images.
	When the application is run, you can add words & images, delete words & images, and search for existing words
	to view their images. The words are case-sensitive.


		WHERE I LEARNED HOW TO USE IMAGES:

	There is no one place I where I learned how to import and display images.
	Tkinter is able to work with images (although only a few formats), so with just a few google searches
	it was pretty simple to figure out.

"""


from tkinter import *
from tkinter import filedialog
import os


class MainWindow:
	def __init__(self):
		self.main_window = Tk()

		self.search_button = Button(self.main_window, text="Search for word", command=self.search, width=20)
		self.add_button = Button(self.main_window, text="Add new word", command=self.add_new, width=20)
		self.delete_button = Button(self.main_window, text="Delete a word", command=self.delete, width=20)

		self.exit_button = Button(self.main_window, text="Exit", command=quit, width=20)

		self.search_button.pack()
		self.add_button.pack()
		self.delete_button.pack()
		self.exit_button.pack()

		self.initiate_lists()

		self.main_window.mainloop()

	def search(self):
		search_window = SearchWindow()

	def add_new(self):
		add_window = AddWindow()

	def delete(self):
		delete_window = DeleteWindow()

	def initiate_lists(self):
		try:
			word_file = open("WordSave.txt", "r")
			line = word_file.readline()
			line = line.strip("\n")

			while line != "":
				word_list.append(line)
				line = word_file.readline()
				line = line.strip("\n")

			word_file.close()
		except FileNotFoundError:
			pass

	def save_lists(self):
		word_file = open("WordSave.txt", "w+")
		if len(word_list) > 0:
			for word in word_list:
				word_file.write(word + "\n")

		word_file.close()


class SearchWindow:
	def __init__(self):
		self.search_window = Tk()

		self.top_frame = Frame(self.search_window)
		self.bottom_frame = Frame(self.search_window)

		self.entry_label = Label(self.top_frame, text="Enter the word to search for: ")
		self.entry_box = Entry(self.top_frame, width="20")
		self.confirm_button = Button(self.bottom_frame, text="Search", command=self.search_for_word)
		self.exit_button = Button(self.bottom_frame, text="Exit", command=self.search_window.destroy)

		self.entry_label.pack()
		self.entry_box.pack()
		self.confirm_button.pack(side="left")
		self.exit_button.pack(side="right")

		self.top_frame.pack()
		self.bottom_frame.pack()

		self.search_window.mainloop()

	def search_for_word(self):
		for word in word_list:
			if word == self.entry_box.get():
				i = word_list.index(word)
				self.display_image(i)
				return
		not_found = MessageWindow("Word not found")

	def display_image(self, index):
		self.search_window.destroy()
		display = DisplayWindow(index)


class DisplayWindow:
	def __init__(self, index):
		self.disp_window = Toplevel()

		self.image = PhotoImage(file=(word_list[index] + ".gif"))
		self.panel = Label(self.disp_window, image=self.image)

		self.panel.pack()
		self.disp_window.mainloop()


class AddWindow:
	def __init__(self):
		self.add_window = Tk()

		self.top_frame = Frame(self.add_window)
		self.bottom_frame = Frame(self.add_window)

		self.entry_label = Label(self.top_frame, text="Enter the new word: ")
		self.entry_box = Entry(self.top_frame, width="20")
		self.confirm_button = Button(self.bottom_frame, text="Add", command=self.add_new_word)
		self.exit_button = Button(self.bottom_frame, text="Exit", command=self.add_window.destroy)

		self.entry_label.pack()
		self.entry_box.pack()
		self.confirm_button.pack(side="left")
		self.exit_button.pack(side="right")

		self.top_frame.pack()
		self.bottom_frame.pack()

		self.add_window.mainloop()

	def add_new_word(self):
		word = self.entry_box.get()
		word_list.append(word)
		img = self.get_image()

		img_file = open(word + ".gif", "w+b")
		img_file.write(img)
		img_file.close()

		save_words()
		self.add_window.destroy()
		message = MessageWindow("Word successfully added")

	def get_image(self):
		file = filedialog.askopenfile(parent=self.add_window, mode="rb", title="Choose a file",
		                              filetypes=[("gif files", "*.gif")])
		if file is not None:
			data = file.read()
			file.close()
			return data


class DeleteWindow:
	def __init__(self):
		self.delete_window = Tk()

		self.top_frame = Frame(self.delete_window)
		self.bottom_frame = Frame(self.delete_window)

		self.entry_label = Label(self.top_frame, text="Enter the word to delete: ")
		self.entry_box = Entry(self.top_frame, width="20")
		self.confirm_button = Button(self.bottom_frame, text="Delete", command=self.delete_word)
		self.exit_button = Button(self.bottom_frame, text="Exit", command=self.delete_window.destroy)

		self.entry_label.pack()
		self.entry_box.pack()
		self.confirm_button.pack(side="left")
		self.exit_button.pack(side="right")

		self.top_frame.pack()
		self.bottom_frame.pack()

		self.delete_window.mainloop()

	def delete_word(self):
		try:
			index = word_list.index(self.entry_box.get())
			os.remove(word_list[index] + ".gif")
			del word_list[index]
			save_words()
			self.delete_window.destroy()
			message = MessageWindow("Word successfully deleted")
		except ValueError and FileNotFoundError:
			not_found = MessageWindow("Word not found")


class MessageWindow:
	def __init__(self, message):
		self.window = Tk()

		self.message_label = Label(self.window, text=message)
		self.message_label.pack()

		self.exit_button = Button(self.window, text="Okay", command=self.window.destroy)
		self.exit_button.pack()

		self.window.mainloop()


def main():
	main_window = MainWindow()


word_list = []


def save_words():
		word_file = open("WordSave.txt", "w+")
		if len(word_list) > 0:
			for word in word_list:
				word_file.write(word + "\n")

		word_file.close()


main()
