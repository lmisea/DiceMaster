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
	while True:                                                         # Breaks when user types 'q'.
		user_input: str = input(
		    "What do you want to roll? (Type 'q' to Quit, 'h' for Help): "
		).lower()

		if (user_input == "q") or (user_input == "quit"):
			utilities.quit_program()
		elif (user_input == "h") or (user_input == "help"):
			menu.display_instructions()
			utilities.clear_terminal()
			continue
		else:
			request: utilities.Request = utilities.process_input(user_input)

		print(request)

		# # Setting singular or plural.
		# if (dice_quantity == 1):
		# 	die_dice, sum_message = " die", "Result"
		# elif (dice_quantity <= 100000):
		# 	die_dice, sum_message = " dice", "Total sum"
		# else:
		# 	error_reason = "Rolling more than one hundred thousand dice? Isn't that too much?"
		# 	raise ValueError

		# list_input = list(user_input)
		# d_idx = user_input.index("d") + 1
		# final_char = len(list_input)
		# mod_to_do, mod_value, bonus, penalty = "", "", "", ""

		# # Part after the 'd' in user's input.
		# for character in range(d_idx, final_char):

		# 	# Setting number of faces that the dice will have.
		# 	if (list_input[character].isdigit()):
		# 		dice_faces += str(list_input[character])

		# 	# User added a bonus.
		# 	elif (list_input[character] == "+"):
		# 		mod_idx = user_input.index("+") + 1
		# 		mod_to_do, mod_type, mod_value = True, "bonus", 0
		# 		break

		# 	# User added a penalty.
		# 	elif (list_input[character] == "-"):
		# 		mod_idx = user_input.index("-") + 1
		# 		mod_to_do, mod_type, mod_value = True, "penalty", 0
		# 		break

		# # If there's one modifier that the program hasn't determinate its value.
		# while (mod_to_do == True):

		# 	# If it's the last modifier this won't run again.
		# 	mod_to_do, original_mod_idx = False, mod_idx

		# 	# Checking what comes after the modifier.
		# 	for character in range(mod_idx, final_char):

		# 		# A number comes next.
		# 		if (list_input[character].isdigit()):
		# 			if (mod_type == "bonus"):
		# 				bonus += str(list_input[character])
		# 			elif (mod_type == "penalty"):
		# 				penalty += str(list_input[character])

		# 		# A bonus comes next
		# 		elif (list_input[character] == "+"):
		# 			if (bonus != ""):
		# 				mod_value += int(bonus)
		# 			elif (penalty != ""):
		# 				mod_value -= int(penalty)
		# 			bonus, penalty, mod_to_do, mod_type = "", "", True, "bonus"
		# 			mod_idx = user_input.index("+", original_mod_idx,
		# 			                           final_char) + 1
		# 			break

		# 		# A penalty comes next
		# 		elif (list_input[character] == "-"):
		# 			if (bonus != ""):
		# 				mod_value += int(bonus)
		# 			elif (penalty != ""):
		# 				mod_value -= int(penalty)
		# 			bonus, penalty, mod_to_do, mod_type = "", "", True, "penalty"
		# 			mod_idx = user_input.index("-", original_mod_idx,
		# 			                           final_char) + 1
		# 			break

		# 		# If it were found another modifier, repeat the process.
		# 		if (mod_idx != original_mod_idx):
		# 			continue

		# # If no new modifiers were found after the last one checked
		# if (bonus != ""):
		# 	mod_value += int(bonus)
		# elif (penalty != ""):
		# 	mod_value -= int(penalty)

		# # There's no number after the 'd'.
		# if (dice_faces == ""):
		# 	error_reason = "After the 'd', specify the number of faces that the dice have."
		# 	raise ValueError

		# dice_faces = int(dice_faces)

		# # Rolling dice of 0 faces.
		# if (dice_faces == 0):
		# 	error_reason = "It's impossible to roll dice of 0 faces."
		# 	raise ValueError

		# # Setting singular or plural.
		# elif (dice_faces == 1):
		# 	face_faces = " face"
		# else:
		# 	face_faces = " faces"

		# # For organized result output.
		# if (dice_faces <= 99):
		# 	list_width = 20
		# elif (dice_faces <= 999):
		# 	list_width = 16
		# elif (dice_faces <= 9999):
		# 	list_width = 13
		# elif (dice_faces <= 99999):
		# 	list_width = 11
		# elif (dice_faces <= 1000000):
		# 	list_width = 8
		# else:
		# 	error_reason = "Dice of more than one million faces? Isn't that too much?"
		# 	raise ValueError

		# # There's no error in the input if we get to this part.
		# error, error_reason = False, ""
		# row_to_do = True # Used to display each dice result.
		# print("")

		# # Used to justify each dice result.
		# dice_faces_digits = len(str(dice_faces))

		# # Rolling and displaying each dice result
		# for die in range(dice_quantity):

		# 	result = random.randint(1, dice_faces)
		# 	result_list.append(result)
		# 	summation += result

		# 	if (die % list_width != list_width - 1) and (die !=
		# 	                                             dice_quantity - 1):
		# 		print(repr(result).rjust(dice_faces_digits), end="  ")

		# 	elif (die == dice_quantity - 1):
		# 		print(repr(result).rjust(dice_faces_digits), end="")

		# 	else:
		# 		print(repr(result).rjust(dice_faces_digits), end="\n")

		# print("", end="\n")

		# # Roll result message (with modifier(s)).
		# if (mod_value != ""):
		# 	summation += mod_value
		# 	if (mod_value > 0):
		# 		modifier = " plus " + str(abs(mod_value))
		# 		mod_message = " plus bonus: "
		# 	elif (mod_value < 0):
		# 		modifier = " minus " + str(abs(mod_value))
		# 		mod_message = " minus penalty: "
		# 	else:
		# 		modifier = " (modifiers cancelled themselves)"
		# 		mod_message = " (modifiers cancelled themselves): "
		# 	print("\nDone. Rolled " + str(dice_quantity) + die_dice + " of " +
		# 	      str(dice_faces) + face_faces + modifier + ".\n" +
		# 	      sum_message + mod_message + str(summation) + ".")

		# # Roll result message (no modifier(s)).
		# else:
		# 	print("\nDone. Rolled " + str(dice_quantity) + die_dice + " of " +
		# 	      str(dice_faces) + face_faces + ".\n" + sum_message + ": " +
		# 	      str(summation) + ".")

		# # Showing highest die only if more than 1 die was rolled.
		# if (dice_quantity != 1):
		# 	print("Highest die: " + str(max(result_list)) + ".")

		# # Error message with its reason.
		# print("\nSorry, unable to roll.\nReason: " + error_reason)
