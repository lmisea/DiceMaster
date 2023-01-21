import sshkeyboard

from . import menu, utilities


def menu_press(key) -> None:
	"""When 's' is pressed, starts the DiceMaster rolling functionality.\n
    When 'i' is pressed, the instructions are displayed.\n
    When 'q' is pressed, the program is terminated.\n
    When any other key is pressed, doesn't trigger anything.
    """
	if (key == "s"):
		sshkeyboard.stop_listening()
	elif (key == "i"):
		utilities.display_instructions = True
		sshkeyboard.stop_listening()
	elif (key == "q"):
		sshkeyboard.stop_listening()
		utilities.quit_program()


def instructions_press(key) -> None:
	"""When 'n' is pressed, the next instruction's page is displayed.\n
    When 'p' is pressed, the previous instruction's page is displayed.\n
    When 's' is pressed, starts the DiceMaster rolling functionality.\n
    When 'q' is pressed, the program is terminated.\n
    When any other key is pressed, doesn't trigger anything.
    """
	if (key == "n") and (menu.instructions_page == 1):
		menu.instructions_page += 1
		utilities.clear_terminal()
		print(menu.instructions_second_page)
	if (key == "p") and (menu.instructions_page == 2):
		menu.instructions_page -= 1
		utilities.clear_terminal()
		print(menu.instructions_first_page)
	elif (key == "s"):
		menu.instructions_page = 1
		sshkeyboard.stop_listening()
	elif (key == "q"):
		sshkeyboard.stop_listening()
		utilities.quit_program()
