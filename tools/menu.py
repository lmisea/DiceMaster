import sshkeyboard

from . import key_functions, utilities


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

instructions_first_page: str = "INSTRUCTIONS\n\nHOW TO ROLL?\nYou can now roll any kind of die you want, as many times as you desire.\nThe standard syntax for rolling is: '[num_dice]d[num_faces]+/-[modifier]'.\nWhere '[num_dice]' is an integer who specifies how many dice to roll.\nAnd '[num_faces]' is an integer who specifies how many faces each die has.\n\nFor example:\nIf you write '2d6', this will roll 2 dice of 6 faces.\nIf you write '100 d 20', this will roll 100 dice of 20 faces.\nNote that it is okay to add a space before and/or after the 'd'.\nMORE ABOUT '[modifier]' ON THE NEXT PAGE.\n\nPress 'n' for NEXT PAGE, 's' to START ROLLING or 'q' for QUITTING."

instructions_second_page: str = "HOW TO ADD A MODIFIER?\nAfter '[num_faces]' add: '+/-[modifier]'. Where '[modifier]' is an integer.\nFor a bonus modifier use '+[modifier]' and use '-[modifier]' for a penalty modifier.\nThis will increase or decrease the total sum of the dice rolled by the '[modifier]' value.\n\nFor example:\nIf you write '1d8+2', this will roll 1 die of 8 adding a modifier of +2.\nIf you write '8d12 - 5', this will roll 8 dice of 12 faces adding a modifier of -5.\nNote that it is okay to add a space before and/or after the '+' or '-'.\n\nPress 'p' for PREVIOUS PAGE, 's' to START ROLLING or 'q' for QUITTING."
