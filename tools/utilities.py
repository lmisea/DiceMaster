import os
from collections import Counter
from typing import TypedDict


class Request(TypedDict):
	dice_quantity: int
	num_faces: int
	modifier: int
	error: None | str


def clear_terminal() -> None:
	"""Clears the terminal."""
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")


def quit_program() -> None:
	"""Quits the program with thank you message"""
	print("\nThank you for using DiceMaster.")
	os._exit(0)


def process_input(user_input: str) -> Request:
	"""Returns the necessary data for rolling (number of dice to be rolled, number of faces of each die, etc).
	If the input is valid request['error] is set to None, otherwise request['error'] explains why the request is not valid.

	Args:
		user_input (str): The user's input

	Returns:
		request (Request): {'dice_quantity' : int, 'num_faces' : int, 'modifier' : int, 'error' : str | None}
	"""
	request: Request = {
	    'dice_quantity': 0,
	    'num_faces': 0,
	    'modifier': 0,
	    'error': None
	}

	user_input = user_input.replace(' ', '') # Deletes any space in the input

	# Creating an instance of the Counter Class allows to count really fast how many times each char is repeated
	input_counter: Counter = Counter(user_input)
	number_of_d: int = input_counter['d']
	if number_of_d < 1:
		request[
		    'error'] = "There's no 'd', it has be typed in order to roll anything."
		return request
	elif number_of_d > 1:
		request['error'] = "The letter 'd' must be typed once and only once."
		return request

	# Checking there's no invalid char in the input
	any_other_letter_than_d: str = user_input.replace('d', '')
	punctuation_set: set = set('''!"#$%&'()*,./:;<=>?@[\]^_`{|}~''')
	if any_other_letter_than_d.islower():
		request['error'] = "It cannot be typed a letter that is not 'd'."
		return request
	elif any(character in punctuation_set for character in user_input):
		request[
		    'error'] = "It cannot be typed a punctuation character that is not '+' or '-'."
		return request

	# Setting quantity of dice to be rolled.
	d_idx: int = user_input.index("d")
	if user_input[:d_idx] == '':
		request[
		    'error'] = "Before the 'd', specify the number of dice to be rolled."
		return request
	elif '+' in user_input[:d_idx] or '-' in user_input[:d_idx]:
		request[
		    'error'] = "It cannot be typed '+' or '-' when specifying the dice quantity to be rolled."
		return request
	else:
		request['dice_quantity'] = int(user_input[:d_idx])

	if (request['dice_quantity'] == 0):
		request['error'] = "It's impossible to roll 0 dice."
		return request

	# Setting quantity of faces for each die.
	bonuses: int = input_counter['+']
	penalties: int = input_counter['-']
	modifiers: int = bonuses + penalties
	d_idx += 1                                          # d_idx will be the start, adding 1 so it doesn't catch the d
	if user_input[d_idx:] == '':
		request[
		    'error'] = "After the 'd', specify the number of faces that the dice have."
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
			    'error'] = "After the 'd' and before a modifier ('+', '-'), specify the number of faces that the dice have."
			return request

		# Setting the modifier
		for modifier in range(modifiers):
			modifier_idx += 1
			if user_input[modifier_idx:] == '':
				request[
				    'error'] = "After a modifier ('+' or '-'), specify its value. One of the modifiers doesn't have a value."
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
				    'error'] = "After a modifier ('+' or '-'), specify its value. One of the modifiers doesn't have a value."
				return request
			modifier_idx = next_modifier
	else:
		request['num_faces'] = int(user_input[d_idx:])
		request['modifier'] = 0

	if request['num_faces'] == 0:
		request['error'] = "It's impossible to roll dice of 0 faces."
		return request

	return request


display_instructions: bool = False
