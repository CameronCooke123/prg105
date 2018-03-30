"""

	A trivia game for two players.
	After all the questions have been answered, the program displays the winner

Sample of program output:

What is the name of the current President of the U.S.?
A: Abraham Lincoln
B: Donald Trump
C: Barock Obama
D: Richard Niouoiuoiuioxon

B

Correct!


"""

import Question


def main():
	# define questions
	question1 = Question.Question("In What year did the game Super Meat Boy release?",
	                              "A: 2009", "B: 2010", "C: 2011", "D: 2012", "B")
	question2 = Question.Question("In What year did the game StarCraft 2 release?",
	                              "A: 2007", "B: 2008", "C: 2009", "D: 2010", "D")
	question3 = Question.Question("In What year did the game Minecraft initially release?",
	                              "A: 2007", "B: 2008", "C: 2009", "D: 2010", "C")
	question4 = Question.Question("In What year did the game Overwatch release?",
	                              "A: 2016", "B: 2008", "C: 1999", "D: 2001", "A")
	question5 = Question.Question("Which of these characters is NOT in the game Halo3?",
	                              "A: Master Chief", "B: Cortana", "C: Tonnika", "D: The Arbiter", "C")
	question6 = Question.Question("Which of these characters is NOT in the game Overwatch?",
	                              "A: Pharah", "B: Nazeebo", "C: Roadhog", "D: Genji", "B")
	question7 = Question.Question("Which video game shooter franchise introduced the Iron Sight mechanic?",
	                              "A: Half-Life", "B: Team Fortress", "C: Call of Duty", "D: Halo", "C")
	question8 = Question.Question("Which video game shooter franchise did away with a health bar mechanic?",
	                              "A: Half-Life", "B: Team Fortress", "C: Call of Duty", "D: Halo", "C")
	question9 = Question.Question("What is the most sold video game of all time?",
	                              "A: TETRIS", "B: GTA V", "C: Super Mario Bros", "D: PUBG", "A")
	question10 = Question.Question("What is the second most sold video game of all time?",
	                               "A: Wii Sports", "B: Minecraft", "C: Overwatch", "D: TES V: Skyrim", "B")

	# place questions into two tuples
	set1 = [question1, question3, question5, question7, question9]
	set2 = [question2, question4, question6, question8, question10]

	# play game
	print("\nPlayer 1's turn!\n")
	player1_points = game_round(set1)
	print("\bPlayer 2's turn!\n")
	player2_points = game_round(set2)

	# print out the winner
	print("Player 1 earned " + str(player1_points) + " points!")
	print("Player 2 earned " + str(player2_points) + " points!")

	if player1_points == player2_points:
		print("The game was a tie!")
	elif player1_points > player2_points:
		print("Player 1 is the winner!")
	else:
		print("Player 2 is the winner!")


def game_round(questions):

	player_score = 0

	for question in questions:
		# print out question and options
		print(question.question)
		print(question.option1)
		print(question.option2)
		print(question.option3)
		print(question.option4)

		# get player guess
		player_guess = input("Enter the letter of your answer: ")

		# determine if the answer was correct and adjust the player points variable accordingly
		if player_guess.upper() == question.get_correct_ans():
			print("\nCorrect!\n")
			player_score += 1
		else:
			print("\nIncorrect. The answer was " + question.get_correct_ans() + "\n")

	return player_score


main()
