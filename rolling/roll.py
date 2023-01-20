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


def roll_dice(dice_quantity: int, num_faces: int, modifier: int) -> Result:
	"""Rolls the user's request and saves the individual die results, the total sum of them and the highest die rolled.

	Args:
		dice_quantity (int): How many dice will be roll
		num_faces (int): How many faces each die has
		modifier (int): By what number modify the total sum of the dice rolled

	Returns:
		result (Result): {'results': list[int], 'total': int, 'highest': int}
	"""
	result: Result = {'results': [], 'total': 0, 'highest': 0}

	for die in range(dice_quantity):
		result["results"].append(secrets.randbelow(num_faces) + 1)

	result["total"] = sum(result["results"]) + modifier
	result["highest"] = max(result["results"])

	return result


def display_results(result: Result, request: Request) -> None:
	print('Eczelente\n')
