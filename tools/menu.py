import sshkeyboard
from tools import key_functions, utilities


def display_instructions() -> None:
	"""Displays instructions, for more info read instructions_press docstring."""
	utilities.clear_terminal()
	print(instructions_first_page)
	sshkeyboard.listen_keyboard(on_press=key_functions.instructions_press,
	                            until="")


def display_menu() -> None:
	"""Displays a basic Menu, with welcome message, instructions, starting and quitting."""
	utilities.clear_terminal()
	print(menu_message)
	sshkeyboard.listen_keyboard(on_press=key_functions.menu_press, until="")
	if (utilities.display_instructions == True):
		display_instructions()


instructions_page: int = 1

menu_message: str = "DiceMaster v3.4.0 - Powered by Luis M. Isea.\n\nPress 's' for STARTING.\nPress 'i' for INSTRUCTIONS.\nPress 'q' for QUITTING.\nDISCLAIMER: It's highly recommended to read the Instructions the first time.\n"

instructions_first_page: str = "INSTRUCTIONS\n\nHOW TO ROLL?\nYou can now roll any kind of die you want, just as many times you desire.\nFirst write the number of dice you want to roll, later write 'd'\nand next how many faces does that kind of dice have.\nFor example:\nIf you write '2d6', this will roll 2 dice of 6 faces.\nIf you write '100 d 20', this will roll 100 dice of 20 faces.\n\nPress 'n' for NEXT PAGE, 's' to START ROLLING or 'q' for QUITTING."

instructions_second_page: str = "HOW TO ADD A BONUS?\nAfter the standard syntax for rolling, just add '+' and then the bonus value.\nThis will increase the total sum of the dice rolled by the bonus value.\nHOW TO ADD A PENALTY?\nAfter the standard syntax for rolling, just add '-' and then the penalty value.\nThis will decrease the total sum of the dice rolled by the penalty value.\nFor example:\nIf you write '1d8+2', this will roll 1 die of 8 faces plus a 2 bonus.\nIf you write '8d12 -5', this will roll 8 dice of 12 faces minus a 5 penalty.\n\nPress 'p' for PREVIOUS PAGE, 's' to START ROLLING or 'q' for QUITTING."
