import os
from collections import Counter
from typing import Any


def clear_terminal() -> None:
	"""Clears the terminal."""
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")


def process_input(user_input: str) -> dict[str, Any]:
	"""Checks if the user's input is valid and returns the data of the request (dice to be rolled, num of faces, etc).
	If the input is not valid it returns the error and its reason.

	Args:
		user_input (str): The user's input

	Returns:
		request (dict): ['valid' : bool, 'dice_quantity' : int, 'num_faces' : int, 'modifier' : int, 'error_reason' : str]

	valid: 'True' if the input is understandable for the program;
	'False' if there were an error in the input's syntax.

	dice_quantity: The amount of dice needed to be rolled;
	'0' if not valid input were given.

	num_faces: The number of faces each die has;
	'0' if not valid input were given.

	modifier: The number who will be added to the total sum of the dice rolled
	(if negative it will decrease the total sum). '0' by default.

	error_reason: If the input is not valid, contains a little explanation of why the input is invalid,
	allowing the user to understand what to change to make a valid request ('' if the input is valid).
	"""
	# Declaring variables and giving them default values
	request: dict
	valid: bool
	dice_quantity: int
	num_faces: int
	modifier: int
	error_reason: str
	dice_quantity = num_faces = modifier = 0
	valid = True
	error_reason = ''

	user_input = user_input.lower()          # Turns everything to lowercase
	user_input = user_input.replace(' ', '') # Deletes any space in the input

	# Creating an instance of the Counter Class allows to count really fast how many d's the input has
	input_counter = Counter(user_input)
	number_of_d = input_counter['d']
	if number_of_d < 1:
		valid = False
		error_reason = "There's no 'd', it has be typed in order to roll anything."
		request = {
		    'valid': valid,
		    'dice_quantity': dice_quantity,
		    'num_faces': num_faces,
		    'modifier': modifier,
		    'error_reason': error_reason
		}
		return request
	elif number_of_d > 1:
		valid = False
		error_reason = "The letter 'd' must be typed once and only once."
		request = [valid, dice_quantity, num_faces, modifier, error_reason]
		return request

	# Setting quantity of dice to be rolled.
	d_idx = user_input.index("d")
	if user_input[:d_idx].islower(): # False if there's a letter before 'd'
		valid = False
		error_reason = "It cannot be typed a letter that is not 'd'."
		request = [valid, dice_quantity, num_faces, modifier, error_reason]
		return request
	else:
		dice_quantity = int(user_input[:d_idx])
	request = [valid, dice_quantity, num_faces, modifier, error_reason]
	return request


starting: bool = False
display_instructions: bool = False

hi = input('Say hi: ')
print(process_input(hi))
