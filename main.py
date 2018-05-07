"""




	# WHERE I LEARNED HOW TO IMPORT IMAGES:

"""


from tkinter import *
from tkinter import filedialog


class MainWindow:
	def __init__(self):
		self.main_window = Tk()

		self.search_button = Button(self.main_window, text="Search for word", command=self.search, width=20)
		self.add_button = Button(self.main_window, text="Add new word", command=self.add_new, width=20)
		self.delete_button = Button(self.main_window, text="Delete a word", command=self.delete, width=20)
		self.save_button = Button(self.main_window, text="Save", command=self.save_lists, width=20)

		self.exit_button = Button(self.main_window, text="Exit", command=quit, width=20)

		self.search_button.pack()
		self.add_button.pack()
		self.delete_button.pack()
		self.save_button.pack()
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
			print("words: ", word_list)

			image_file = open("ImageSave.sav", "rb")
			temp_list = image_file.read()

			for image in temp_list:
				image_list.append(image)

			image_file.close()
		except FileNotFoundError:
			pass

	def save_lists(self):
		word_file = open("WordSave.txt", "w+")
		if len(word_list) > 0:
			for word in word_list:
				word_file.write(word + "\n")

		word_file.close()

		image_file = open("ImageSave.sav", "w+b")
		if len(image_list) > 0:
			for image in image_list:
				image_file.write(image)

		image_file.close()


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
			print(word)
			if word == self.entry_box.get():
				i = word_list.index(word)
				self.display_image(i)
				return
		not_found = ErrorWindow("Word not found")


	def display_image(self, index):
		display = DisplayWindow(index)


class DisplayWindow:
	def __init__(self, index):
		self.disp_window = Toplevel()

		self.image = PhotoImage(file=(word_list[index] + ".gif"))
		self.panel = Label(self.disp_window, image=self.image)

		self.panel.pack()
		print("Happened")
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
		image_list.append(img)

		img_file = open(word + ".gif", "w+b")
		img_file.write(img)
		img_file.close()

		print("Words: ", word_list)
		print("Images: ", image_list)
		# the add window needs to close
		# the word needs to be saved

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
			del word_list[index]
			del image_list[index]
			print("Words: ", word_list)
			print("Images: ", image_list)
		except ValueError:
			not_found = ErrorWindow("Word not found")


class ErrorWindow:
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
image_list = []

main()
