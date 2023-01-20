# For the dice rolling I'm moving from random module to secrets module
# because random module is less trusted than secrets module, who produces stronger random numbers.
# More info here - https://docs.python.org/3/library/secrets.html

import secrets
from typing import TypedDict

from tools.utilities import Request


class Result(TypedDict):
	results: list[int]
	total: int
	highest: int


def roll_dice(request: Request) -> Result:
	"""Rolls the user's request and saves the individual die results, the total sum of them and the highest die rolled.

	Args:
		request (Request): {'dice_quantity': int, 'num_faces': int, 'modifier': int, 'error': str | None}.
		A Request object can be obtained from utilities.process_input()

	Returns:
		result (Result): {'results': list[int], 'total': int, 'highest': int}. A Result object can be obtained from roll.roll_dice()
	"""
	result: Result = {'results': [], 'total': 0, 'highest': 0}

	for die in range(request['dice_quantity']):
		result['results'].append(secrets.randbelow(request['num_faces']) + 1)

	result['total'] = sum(result['results']) + request['modifier']
	result['highest'] = max(result['results'])

	return result


def display_results(result: Result, request: Request) -> None:
	"""Displays all the results as a matrix with a nice formatting to improve readability.
	It also displays basic information of the roll just made as a confirmation that the correct roll were made (the correct amount of dice, etc).

	Args:
		result (Result): {'results': list[int], 'total': int, 'highest': int}

		request (Request): {'dice_quantity': int, 'num_faces': int, 'modifier': int, 'error': str | None}
	"""
	print('')
	num_faces_digits: int = len(str(request['num_faces']))
	# 80 is the max num of char that I want to display per line, but the
	# last die result doesn't have 2 spaces at the end, so I add 2 to the max
	width: int = 82 // (num_faces_digits+2) # with the // the floor is returned
	dice_number: int = 1
	for die in result['results']:
		if dice_number % width != 0 and dice_number != request['dice_quantity']:
			print('%*d' % (num_faces_digits, die), end='  ')
		else:
			print('%*d' % (num_faces_digits, die), end='\n')
		dice_number += 1
	print('\nEczelente\n')
