import os
import sys
from collections import Counter

if sys.version_info >= (3, 8):
	from typing import TypedDict
else:
	from typing_extensions import TypedDict


class Request(TypedDict):
	valid: bool
	dice_quantity: int
	num_faces: int
	modifier: int
	error: str


def clear_terminal() -> None:
	"""Clears the terminal."""
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")


def quit_program() -> None:
	"""Quits the program with a thank you message"""
	print("\nThank you for using DiceMaster.")
	os._exit(0)


def process_input(user_input: str) -> Request:
	"""Returns the necessary data for rolling (number of dice to be rolled, number of faces of each die, etc).
	If the input is valid request['valid'] is set to True, otherwise request['error'] explains why the request is not valid.

	Args:
		user_input (str): The user's input

	Returns:
		request (Request): {'valid': bool, 'dice_quantity': int, 'num_faces': int, 'modifier': int, 'error': str}
	"""
	request: Request = {
	    'valid': False,
	    'dice_quantity': 0,
	    'num_faces': 0,
	    'modifier': 0,
	    'error': ''
	}

	user_input = user_input.replace(' ', '') # Deletes any space in the input

	# Creating an instance of the Counter Class allows to count really fast how many times each char is repeated
	input_counter: Counter = Counter(user_input)
	number_of_d: int = input_counter['d']
	if number_of_d < 1:
		request[
		    'error'] = "There is no 'd', please use the 'd' in order to roll anything."
		return request
	elif number_of_d > 1:
		request['error'] = "Please type the letter 'd' only once."
		return request

	# Checking there's no invalid char in the input
	any_other_letter_than_d: str = user_input.replace('d', '')
	punctuation_set: set = set('''!"#$%&'()*,./:;<=>?@[\]^_`{|}~''')
	if any_other_letter_than_d.islower():
		request['error'] = "Please do not type other letter than 'd'."
		return request
	elif any(character in punctuation_set for character in user_input):
		request[
		    'error'] = "Please do not type a punctuation character that is not '+' or '-'."
		return request

	# Setting quantity of dice to be rolled.
	d_idx: int = user_input.index("d")
	if user_input[:d_idx] == '':
		request[
		    'error'] = "Before the 'd', please specify the number of dice to be rolled."
		return request
	elif '+' in user_input[:d_idx] or '-' in user_input[:d_idx]:
		request['error'] = "Please do not type '+' or '-' before the 'd'."
		return request
	else:
		request['dice_quantity'] = int(user_input[:d_idx])

	if (request['dice_quantity'] == 0):
		request['error'] = "It is impossible to roll 0 dice."
		return request

	# Setting quantity of faces for each die.
	bonuses: int = input_counter['+']
	penalties: int = input_counter['-']
	modifiers: int = bonuses + penalties
	d_idx += 1                                          # d_idx will be the start, adding 1 so it doesn't catch the d
	if user_input[d_idx:] == '':
		request[
		    'error'] = "After the 'd', please specify the number of faces that each die has."
		return request
	elif modifiers > 0:
		if bonuses > 0 and penalties < 1:
			modifier_idx: int = user_input[d_idx:].index('+') + d_idx
		elif penalties > 0 and bonuses < 1:
			modifier_idx = user_input[d_idx:].index('-') + d_idx
		else:
			modifier_idx = min(user_input[d_idx:].index('+'),
			                   user_input[d_idx:].index('-')) + d_idx

		if user_input[d_idx:modifier_idx] != '':
			request['num_faces'] = int(user_input[d_idx:modifier_idx])
		else:
			request[
			    'error'] = "After the 'd' and before a modifier ('+', '-'), please specify\nthe number of faces that each die has."
			return request

		# Setting the modifier
		for modifier in range(modifiers):
			modifier_idx += 1
			if user_input[modifier_idx:] == '':
				request[
				    'error'] = "After a modifier ('+' or '-'), please specify its value.\nOne of the modifiers doesn't have a value."
				return request
			elif '+' not in user_input[
			    modifier_idx:] and '-' not in user_input[modifier_idx:]:
				request['modifier'] += int(user_input[modifier_idx - 1:])
				break
			elif '+' in user_input[modifier_idx:] and '-' not in user_input[
			    modifier_idx:]:
				next_modifier: int = user_input[modifier_idx:].index(
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
				    'error'] = "After a modifier ('+' or '-'), please specify its value.\nOne of the modifiers doesn't have a value."
				return request
			modifier_idx = next_modifier
	else:
		request['num_faces'] = int(user_input[d_idx:])
		request['modifier'] = 0

	if request['num_faces'] == 0:
		request['error'] = "It is impossible to roll dice of 0 faces."
		return request

	# No error found
	request['valid'] = True
	return request


display_instructions: bool = False
