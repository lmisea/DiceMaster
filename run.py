# DiceMaster version 3.4.0 - Caracas, Venezuela.
# Copyright (C) 2023 Luis Miguel Isea - @lmisea (GitHub)

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

from rolling import roll
from tools import menu, utilities

if __name__ == "__main__":
	menu.display_menu()

	# User pressed 's': Starting
	utilities.clear_terminal()
	while True:               # Breaks when user types 'q'.
		user_input: str = input(
		    "What do you want to roll? ('q' to Quit, 'h' for Help): ").lower()

		if (user_input == "q") or (user_input == "quit"):
			utilities.quit_program()
		elif (user_input == "h") or (user_input == "help"):
			menu.display_instructions()
			utilities.clear_terminal()
			continue
		else:
			request: utilities.Request = utilities.process_input(user_input)

		# Check and catch any error in the input
		if request.get('error') is not None:
			print(f"\nSorry, unable to roll.\nReason: {request['error']}\n")
			continue

		# Rolling the user's request
		result: roll.Result = roll.roll_dice(request)
		roll.display_results(result, request)
