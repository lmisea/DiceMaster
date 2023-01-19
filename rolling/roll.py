# For the dice rolling I'm moving from random module to secrets module
# because random module is less trusted than secrets module, who produces stronger random numbers.
# More info here - https://docs.python.org/3/library/secrets.html

import secrets
from typing import TypedDict


class Result(TypedDict):
	results: list[int]
	total: int
	highest: int


def roll_dice(dice_quantity: int, num_faces: int, modifier: int) -> Result:
	result: Result = {'results': [], 'total': 0, 'highest': 0}

	for die in range(dice_quantity):
		result["results"].append(secrets.randbelow(num_faces) + 1)

	result["total"] = sum(result["results"]) + modifier
	result["highest"] = max(result["results"])

	return result


def show_results() -> None:
	pass
