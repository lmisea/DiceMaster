# DiceMaster version 3.3.9 - Caracas, Venezuela.
# Copyright (C) <2022> <Luis Miguel Isea - @lmisea (GitHub)>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

import random
import re

import sshkeyboard
from rolling import roll

if __name__ == "__main__":
    roll.clear_terminal()

    starting, display_instructions, instructions_page = False, False, 1

    first_page_message = "INSTRUCTIONS\n\nHOW TO ROLL?\nYou can now roll any kind of die you want, just as many times you desire.\nFirst write the number of dice you want to roll, later write 'd'\nand next how many faces does that kind of dice have.\nFor example:\nIf you write '2d6', this will roll 2 dice of 6 faces.\nIf you write '100 d 20', this will roll 100 dice of 20 faces.\n\nPress 'n' for NEXT PAGE, 's' to START ROLLING or 'q' for QUITTING."

    second_page_message = "HOW TO ADD A BONUS?\nAfter the standard syntax for rolling, just add '+' and then the bonus value.\nThis will increase the total sum of the dice rolled by the bonus value.\nHOW TO ADD A PENALTY?\nAfter the standard syntax for rolling, just add '-' and then the penalty value.\nThis will decrease the total sum of the dice rolled by the penalty value.\nFor example:\nIf you write '1d8+2', this will roll 1 die of 8 faces plus a 2 bonus.\nIf you write '8d12 -5', this will roll 8 dice of 12 faces minus a 5 penalty.\n\nPress 'p' for PREVIOUS PAGE, 's' to START ROLLING or 'q' for QUITTING."

    def menu_press(key):
        """
        When 's' is pressed, starts the main functionality.\n
        When 'i' is pressed, the instructions are displayed.\n
        When 'q' is pressed, the program shuts down.\n
        When any other key is pressed, doesn't trigger anything.
        """
        global starting, display_instructions

        if (key == "s"):
            sshkeyboard.stop_listening()
            starting = True
        elif (key == "i"):
            sshkeyboard.stop_listening()
            display_instructions = True
        elif (key == "q"):
            sshkeyboard.stop_listening()

    def instructions_press(key):
        """
        When 'n' is pressed, the next instructions page is displayed.\n
        When 'p' is pressed, the previous instructions page is displayed.\n
        When 's' is pressed, starts the main functionality.\n
        When 'q' is pressed, the program shuts down.\n
        When any other key is pressed, doesn't trigger anything.
        """
        global instructions_page, starting
        starting = False

        if (key == "n") and (instructions_page == 1):
            instructions_page += 1
            roll.clear_terminal()
            print(second_page_message)
        if (key == "p") and (instructions_page == 2):
            instructions_page -= 1
            roll.clear_terminal()
            print(first_page_message)
        elif (key == "s"):
            starting = True
            sshkeyboard.stop_listening()
            instructions_page = 1
        elif (key == "q"):
            sshkeyboard.stop_listening()

    def show_instructions():
        """Displays Instructions, for more info read instructions_press docstring."""
        roll.clear_terminal()
        print(first_page_message)
        sshkeyboard.listen_keyboard(on_press=instructions_press, until="")

    # Displaying menu.
    print(
        "DiceMaster v3.3.9 - Powered by Luis M. Isea.\n\nPress 's' for STARTING.\nPress 'i' for INSTRUCTIONS.\nPress 'q' for QUITTING.\nDISCLAIMER: It's highly recommended to read the Instructions the first time.\n"
    )

    sshkeyboard.listen_keyboard(on_press=menu_press, until="")

    # User pressed 'i' - Displaying instructions.
    if (display_instructions == True):
        show_instructions()

    # Starting DiceMaster.
    if (starting == True):
        roll.clear_terminal()
        first_time, error_reason = True, ""

        while True:  # Breaks when user types 'q'.

            try:
                dice_quantity, dice_faces, summation = "", "", 0
                d_times, result_list = 0, []

                # First time roll message.
                if (first_time == True):
                    user_input = str(
                        input(
                            "What do you want to roll? (Type 'q' to Quit, 'h' for Help): "
                        )).lower()
                    first_time = False

                # Further time roll message.
                elif (first_time == False) and (error == False):
                    user_input = str(
                        input("\nRoll something else? (Type 'q' to Quit): ")
                    ).lower()

                # User typed 'q'.
                if (user_input == "q") or (user_input == "quit"):
                    break

                # User typed 'h'.
                if (user_input == "h") or (user_input == "help"):
                    show_instructions()
                    if (starting == True):
                        roll.clear_terminal()
                        first_time = True
                        continue
                    else:
                        break

                # Removing space characters from user's input.
                while (" " in user_input):
                    user_input = re.sub(" ", "", user_input)

                # Checking if the user's input is valid.
                for character in user_input:

                    # User typed a different letter than 'd'.
                    if (character.isalpha()) and (character != "d"):
                        error_reason = "It cannot be typed a letter that is not 'd'."
                        raise ValueError

                    # User typed a punctuation character that is not "+" or "-".
                    if (character.isdigit()
                            == False) and (character != "d") and (
                                character != "+") and (character != "-"):
                        error_reason = "It cannot be typed a punctuation character that is not '+' or '-'."
                        raise ValueError

                    # Counting letters 'd' in user's input.
                    if (character.isalpha()) and (character == "d"):
                        d_times += 1

                # User did not type the letter 'd'.
                if (d_times == 0):
                    error_reason = "There's no 'd', it has be typed in order to roll anything."
                    raise ValueError

                # User typed more than 1 'd'.
                if (d_times > 1):
                    error_reason = "The letter 'd' must be typed once and only once."
                    raise ValueError

                # Setting quantity of dice to be rolled.
                d_idx = user_input.index("d")
                dice_quantity = user_input[:d_idx]

                # Modifier(s) inside the dice_quantity
                if ("+" in dice_quantity) or ("-" in dice_quantity):
                    error_reason = "It cannot be typed '+' or '-' when specifying the dice quantity to be rolled."
                    raise ValueError

                # There's no number before the 'd'.
                if (dice_quantity == ""):
                    error_reason = "Before the 'd', specify the number of dice to be rolled."
                    raise ValueError

                dice_quantity = int(dice_quantity)

                # Rolling 0 dice.
                if (dice_quantity == 0):
                    error_reason = "It's impossible to roll 0 dice."
                    raise ValueError

                # Setting singular or plural.
                if (dice_quantity == 1):
                    die_dice, sum_message = " die", "Result"
                elif (dice_quantity <= 100000):
                    die_dice, sum_message = " dice", "Total sum"
                else:
                    error_reason = "Rolling more than one hundred thousand dice? Isn't that too much?"
                    raise ValueError

                list_input = list(user_input)
                d_idx = user_input.index("d") + 1
                final_char = len(list_input)
                mod_to_do, mod_value, bonus, penalty = "", "", "", ""

                # Part after the 'd' in user's input.
                for character in range(d_idx, final_char):

                    # Setting number of faces that the dice will have.
                    if (list_input[character].isdigit()):
                        dice_faces += str(list_input[character])

                    # User added a bonus.
                    elif (list_input[character] == "+"):
                        mod_idx = user_input.index("+") + 1
                        mod_to_do, mod_type, mod_value = True, "bonus", 0
                        break

                    # User added a penalty.
                    elif (list_input[character] == "-"):
                        mod_idx = user_input.index("-") + 1
                        mod_to_do, mod_type, mod_value = True, "penalty", 0
                        break

                # If there's one modifier that the program hasn't determinate its value.
                while (mod_to_do == True):

                    # If it's the last modifier this won't run again.
                    mod_to_do, original_mod_idx = False, mod_idx

                    # Checking what comes after the modifier.
                    for character in range(mod_idx, final_char):

                        # A number comes next.
                        if (list_input[character].isdigit()):
                            if (mod_type == "bonus"):
                                bonus += str(list_input[character])
                            elif (mod_type == "penalty"):
                                penalty += str(list_input[character])

                        # A bonus comes next
                        elif (list_input[character] == "+"):
                            if (bonus != ""):
                                mod_value += int(bonus)
                            elif (penalty != ""):
                                mod_value -= int(penalty)
                            bonus, penalty, mod_to_do, mod_type = "", "", True, "bonus"
                            mod_idx = user_input.index("+", original_mod_idx,
                                                       final_char) + 1
                            break

                        # A penalty comes next
                        elif (list_input[character] == "-"):
                            if (bonus != ""):
                                mod_value += int(bonus)
                            elif (penalty != ""):
                                mod_value -= int(penalty)
                            bonus, penalty, mod_to_do, mod_type = "", "", True, "penalty"
                            mod_idx = user_input.index("-", original_mod_idx,
                                                       final_char) + 1
                            break

                        # If it were found another modifier, repeat the process.
                        if (mod_idx != original_mod_idx):
                            continue

                # If no new modifiers were found after the last one checked
                if (bonus != ""):
                    mod_value += int(bonus)
                elif (penalty != ""):
                    mod_value -= int(penalty)

                # There's no number after the 'd'.
                if (dice_faces == ""):
                    error_reason = "After the 'd', specify the number of faces that the dice have."
                    raise ValueError

                dice_faces = int(dice_faces)

                # Rolling dice of 0 faces.
                if (dice_faces == 0):
                    error_reason = "It's impossible to roll dice of 0 faces."
                    raise ValueError

                # Setting singular or plural.
                elif (dice_faces == 1):
                    face_faces = " face"
                else:
                    face_faces = " faces"

                # For organized result output.
                if (dice_faces <= 99):
                    list_width = 20
                elif (dice_faces <= 999):
                    list_width = 16
                elif (dice_faces <= 9999):
                    list_width = 13
                elif (dice_faces <= 99999):
                    list_width = 11
                elif (dice_faces <= 1000000):
                    list_width = 8
                else:
                    error_reason = "Dice of more than one million faces? Isn't that too much?"
                    raise ValueError

                # There's no error in the input if we get to this part.
                error, error_reason = False, ""
                row_to_do = True  # Used to display each dice result.
                print("")

                # Used to justify each dice result.
                dice_faces_digits = len(str(dice_faces))

                # Rolling and displaying each dice result
                for die in range(dice_quantity):

                    result = random.randint(1, dice_faces)
                    result_list.append(result)
                    summation += result

                    if (die % list_width !=
                            list_width - 1) and (die != dice_quantity - 1):
                        print(repr(result).rjust(dice_faces_digits), end="  ")

                    elif (die == dice_quantity - 1):
                        print(repr(result).rjust(dice_faces_digits), end="")

                    else:
                        print(repr(result).rjust(dice_faces_digits), end="\n")

                print("", end="\n")

                # Roll result message (with modifier(s)).
                if (mod_value != ""):
                    summation += mod_value
                    if (mod_value > 0):
                        modifier = " plus " + str(abs(mod_value))
                        mod_message = " plus bonus: "
                    elif (mod_value < 0):
                        modifier = " minus " + str(abs(mod_value))
                        mod_message = " minus penalty: "
                    else:
                        modifier = " (modifiers cancelled themselves)"
                        mod_message = " (modifiers cancelled themselves): "
                    print("\nDone. Rolled " + str(dice_quantity) + die_dice +
                          " of " + str(dice_faces) + face_faces + modifier +
                          ".\n" + sum_message + mod_message + str(summation) +
                          ".")

                # Roll result message (no modifier(s)).
                else:
                    print("\nDone. Rolled " + str(dice_quantity) + die_dice +
                          " of " + str(dice_faces) + face_faces + ".\n" +
                          sum_message + ": " + str(summation) + ".")

                # Showing highest die only if more than 1 die was rolled.
                if (dice_quantity != 1):
                    print("Highest die: " + str(max(result_list)) + ".")

            except:

                # Error message with its reason.
                print("\nSorry, unable to roll.\nReason: " + error_reason)
                user_input = str(
                    input(
                        "\nPlease, try again (Type 'q' to Quit, 'h' for Help): "
                    )).lower()
                error = True
                continue

    # Quitting program.
    print(
        "\nThanks for using DiceMaster (v3.3.9). Hope you enjoyed it.\nPowered by Luis M. Isea."
    )
