"""

Question class diagram:


Question

- question: String
- option1: String
- option2: String
- option3: String
- option4: String
- correct_ans: String

+ set_question
+ set_option1
+ set_option2
+ set_option3
+ set_option4
+ set_correct_ans
+ get_question
+ get_option1
+ get_option2
+ get_option3
+ get_option4
+ get_correct_ans

"""


class Question:

	def __init__(self, question, option1, option2, option3, option4, correct_ans):
		self.question = question
		self.option1 = option1
		self.option2 = option2
		self.option3 = option3
		self.option4 = option4
		self.correct_ans = correct_ans

	def set_question(self, new_question):
		self.question = new_question

	def set_option1(self, new_option):
		self.option1 = new_option

	def set_option2(self, new_option):
		self.option2 = new_option

	def set_option3(self, new_option):
		self.option3 = new_option

	def set_option4(self, new_option):
		self.option4 = new_option

	def set_correct_ans(self, new_ans):
		self.correct_ans = new_ans

	def get_question(self):
		return self.question

	def get_option1(self):
		return self.option1

	def get_option2(self):
		return self.option2

	def get_option3(self):
		return self.option3

	def get_option4(self):
		return self.option4

	def get_correct_ans(self):
		return self.correct_ans
