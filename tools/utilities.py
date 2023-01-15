import os
from collections import Counter
from typing import TypedDict


class Request(TypedDict):
	valid: bool
	dice_quantity: int
	num_faces: int
	modifier: int
	error_reason: str | None


def clear_terminal() -> None:
	"""Clears the terminal."""
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")


def process_input(user_input: str) -> Request:
	"""Checks if the user's input is valid and returns the data of the request (dice to be rolled, num of faces, etc).
	If the input is not valid it returns the error and its reason.

	Args:
		user_input (str): The user's input

	Returns:
		request (Request): ['valid' : bool, 'dice_quantity' : int, 'num_faces' : int, 'modifier' : int, 'error_reason' : str | None]

	valid: 'True' if the input is understandable for the program;
	'False' if there were an error in the input's syntax.

	dice_quantity: The amount of dice needed to be rolled;
	'0' if not valid input were given.

	num_faces: The number of faces each die has;
	'0' if not valid input were given.

	modifier: The number who will be added to the total sum of the dice rolled
	(if negative it will decrease the total sum). '0' by default.

	error_reason: If the input is not valid, contains a little explanation of why the input is invalid,
	allowing the user to understand what to change to make a valid request ('None' if the input is valid).
	"""
	# Assigning default values
	request: Request = {
	    'valid': False,
	    'dice_quantity': 0,
	    'num_faces': 0,
	    'modifier': 0,
	    'error_reason': None
	}

	user_input = user_input.lower()          # Turns everything to lowercase
	user_input = user_input.replace(' ', '') # Deletes any space in the input
	any_other_letter_than_d = user_input.replace('d', '')
	if any_other_letter_than_d.islower():
		request[
		    'error_reason'] = "It cannot be typed a letter that is not 'd'."
		return request

	punctuation_set: set = set('''!"#$%&'()*,./:;<=>?@[\]^_`{|}~''')
	if any(character in punctuation_set for character in user_input):
		request[
		    'error_reason'] = "It cannot be typed a punctuation character that is not '+' or '-'."

	# Creating an instance of the Counter Class allows to count really fast how many d's the input has
	input_counter = Counter(user_input)
	number_of_d = input_counter['d']
	if number_of_d < 1:
		request[
		    'error_reason'] = "There's no 'd', it has be typed in order to roll anything."
		return request
	elif number_of_d > 1:
		request[
		    'error_reason'] = "The letter 'd' must be typed once and only once."
		return request

	# Setting quantity of dice to be rolled.
	d_idx = user_input.index("d")
	if user_input[:d_idx] == '':
		request[
		    'error_reason'] = "Before the 'd', specify the number of dice to be rolled."
		return request
	elif '+' in user_input[:d_idx] or '-' in user_input[:d_idx]:
		request[
		    'error_reason'] = "It cannot be typed '+' or '-' when specifying the dice quantity to be rolled."
		return request
	else:
		request['dice_quantity'] = int(user_input[:d_idx])
	if (request['dice_quantity'] == 0):
		request['error_reason'] = "It's impossible to roll 0 dice."
		return request

	if request['error_reason'] == None:
		request['valid'] = True
	return request


starting: bool = False
display_instructions: bool = False

if __name__ == '__main__':
	hi = input('Say hi: ')
	print(process_input(hi))
