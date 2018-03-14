"""

	a program that has the user enter a string,
	and tells them the letter that appears most frequently.

	the program only checks for letters, and ignore spaces, punctuation, numbers, etc.

"""


ALPHABET = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')


def main():
	most_common_character_count = [0] * 26

	user_input = input("Enter a string of characters: ")
	user_input = user_input.lower()

	letter_index = 0
	for letter in ALPHABET:
		for char in user_input:
			if char == letter:
				most_common_character_count[letter_index] += 1
		letter_index += 1

	most_common_letter_index = most_common_character_count.index(max(most_common_character_count))

	print("The most frequent letter is " + ALPHABET[most_common_letter_index])


main()
