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

	# Creating an instance of the Counter Class allows to count really fast how many d's the input has
	input_counter: Counter = Counter(user_input)
	number_of_d: int = input_counter['d']
	if number_of_d < 1:
		request[
		    'error_reason'] = "There's no 'd', it has be typed in order to roll anything."
		return request
	elif number_of_d > 1:
		request[
		    'error_reason'] = "The letter 'd' must be typed once and only once."
		return request

	# Checking there's no invalid char in the input
	any_other_letter_than_d: str = user_input.replace('d', '')
	punctuation_set: set = set('''!"#$%&'()*,./:;<=>?@[\]^_`{|}~''')
	if any_other_letter_than_d.islower():
		request[
		    'error_reason'] = "It cannot be typed a letter that is not 'd'."
		return request
	elif any(character in punctuation_set for character in user_input):
		request[
		    'error_reason'] = "It cannot be typed a punctuation character that is not '+' or '-'."
		return request

	# Setting quantity of dice to be rolled.
	d_idx: int = user_input.index("d")
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

	# Setting quantity of faces for each die.
	bonuses: int = input_counter['+']
	penalties: int = input_counter['-']
	modifiers: int = bonuses + penalties
	d_idx += 1                                          # d_idx will be the start, adding 1 so it doesn't catch the d
	if user_input[d_idx:] == '':
		request[
		    'error_reason'] = "After the 'd', specify the number of faces that the dice have."
		return request
	elif modifiers > 0:
		if bonuses > 0 and penalties < 1:
			modifier_idx = user_input[d_idx:].index('+') + d_idx
		elif penalties > 0 and bonuses < 1:
			modifier_idx = user_input[d_idx:].index('-') + d_idx
		else:
			modifier_idx = min(user_input[d_idx:].index('+'),
			                   user_input[d_idx:].index('-')) + d_idx

		if user_input[d_idx:modifier_idx] != '':
			request['num_faces'] = int(user_input[d_idx:modifier_idx])
		else:
			request[
			    'error_reason'] = "After the 'd' and before a modifier ('+', '-'), specify the number of faces that the dice have."
			return request

		# Setting the modifier
		for modifier in range(modifiers):
			modifier_idx += 1
			if user_input[modifier_idx:] == '':
				request[
				    'error_reason'] = "After a modifier ('+' or '-'), specify its value. One of the modifiers doesn't have a value."
				return request
			elif '+' not in user_input[
			    modifier_idx:] and '-' not in user_input[modifier_idx:]:
				request['modifier'] += int(user_input[modifier_idx - 1:])
				break
			elif '+' in user_input[modifier_idx:] and '-' not in user_input[
			    modifier_idx:]:
				next_modifier = user_input[modifier_idx:].index(
				    '+') + modifier_idx
			elif '-' in user_input[modifier_idx:] and '+' not in user_input[
			    modifier_idx:]:
				next_modifier = user_input[modifier_idx:].index(
				    '-') + modifier_idx
			elif "+" in user_input[modifier_idx:] and '-' in user_input[
			    modifier_idx:]:
				next_modifier = min(
				    user_input[modifier_idx:].index('+'),
				    user_input[modifier_idx:].index('-')) + modifier_idx

			if user_input[modifier_idx:next_modifier] != '':
				modifier_idx -= 1
				request['modifier'] += int(
				    user_input[modifier_idx:next_modifier])
			else:
				request[
				    'error_reason'] = "After a modifier ('+' or '-'), specify its value. One of the modifiers doesn't have a value."
				return request
			modifier_idx = next_modifier
	else:
		request['num_faces'] = int(user_input[d_idx:])

	if request['num_faces'] == 0:
		request['error_reason'] = "It's impossible to roll dice of 0 faces."
		return request

	# If this is executed it's because there's no error in the input
	request['valid'] = True
	return request


start: bool = False
display_instructions: bool = False
