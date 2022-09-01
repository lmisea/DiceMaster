# DiceMaster version 3.3.5 - September 2022. Caracas, Venezuela.
# Luis Miguel Isea - @LuimiDev (GitHub).

import os
import random
import sshkeyboard


def clear():
    """Clears the terminal."""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


clear()

starting = False
display_instructions = False
instructions_page = 1

first_page_message = "INSTRUCTIONS\n\nHOW TO ROLL?\nYou can now roll any kind of die you want, just as many times you desire.\nIt's as simply as writing first how many dice you want to roll, later write 'd' and next how many faces does that kind of dice have.\nFor example:\nIf you write '2d6', this will roll 2 dice of 6 faces.\nIf you write '100 d 20', this will roll 100 dice of 20 faces.\n\nPress 'n' for NEXT PAGE, 's' to START ROLLING or 'q' for QUITTING."

second_page_message = "HOW TO ADD A BONUS?\nAfter the standard syntax for rolling, just add '+' and then the bonus value. This will increase the total sum of the dice rolled by the bonus value.\nHOW TO ADD A PENALTY?\nAfter the standard syntax for rolling, just add '-' and then the penalty value. This will decrease the total sum of the dice rolled by the penalty value.\nFor example:\nIf you write '1d8+2', this will roll 1 die of 8 faces plus a 2 bonus.\nIf you write '8d12 -5', this will roll 8 dice of 12 faces minus a 5 penalty.\n\nPress 'p' for PREVIOUS PAGE, 's' to START ROLLING or 'q' for QUITTING."


def menu_press(key):
    """
    When 's' is pressed, starts the main functionality.\n
    When 'i' is pressed, the instructions are displayed.\n
    When 'q' is pressed, the program shuts down.\n
    When any other key is pressed, doesn't trigger anything.
    """
    global starting
    global display_instructions

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
    global instructions_page
    global starting
    starting = False

    if (key == "n") and (instructions_page == 1):
        instructions_page += 1
        clear()
        print(second_page_message)
    if (key == "p") and (instructions_page == 2):
        instructions_page -= 1
        clear()
        print(first_page_message)
    elif (key == "s"):
        starting = True
        sshkeyboard.stop_listening()
        instructions_page = 1
    elif (key == "q"):
        sshkeyboard.stop_listening()


def instructions():
    """Displays Instructions, for more info read instructions_press docstring."""
    clear()
    print(first_page_message)
    sshkeyboard.listen_keyboard(on_press=instructions_press, until="")


# Displaying menu.
print("DiceMaster v3.3.5 - Powered by Luis M. Isea.\n\nPress 's' for STARTING.\nPress 'i' for INSTRUCTIONS.\nPress 'q' for QUITTING.\nDISCLAIMER: It's highly recommended to read the Instructions the first time.\n")

sshkeyboard.listen_keyboard(on_press=menu_press, until="")

# User pressed 'i' - Displaying instructions.
if (display_instructions == True):
    instructions()

# Starting DiceMaster.
if (starting == True):
    clear()
    first_time = True
    error_reason = ""

    while True:  # Breaks when user types 'q'.

        try:
            dice_quantity = ""
            dice_faces = ""
            d_times = 0
            summation = 0
            result_list = []

            # First time roll message.
            if (first_time == True):
                user_input = str(
                    input("Please, write what you want to roll ('q' to Quit, 'h' for Help): ")).lower()
                first_time = False

            # Further time roll message.
            elif (first_time == False) and (error == False):
                user_input = str(
                    input("\nRoll something else? (Type 'q' to Quit): ")).lower()

            # User typed 'q'.
            if (user_input == "q") or (user_input == "quit"):
                break

            # User typed 'h'.
            if (user_input == "h") or (user_input == "help"):
                instructions()
                if (starting == True):
                    clear()
                    first_time = True
                    continue
                else:
                    break

            # Checking if the user's input is valid.
            for character in user_input:

                # User typed a different letter than 'd'.
                if (character.isalpha()) and (character != "d"):
                    error_reason = "It cannot be typed a letter that is not 'd'."
                    raise ValueError

                # User typed a punctuation character that is not "+" or "-".
                if (character.isdigit() == False) and (character.isspace() == False) and (character != "d") and (character != "+") and (character != "-"):
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
            for character in user_input:

                if (character != "d"):
                    dice_quantity += str(character)
                    # If we use '+= int(character)', we could not handle numbers of two or more digits. E.g.: '24' would become 6.
                else:
                    break

            # There's no number before the 'd'.
            if (dice_quantity == ""):
                error_reason = "Before the letter 'd', it must be typed the number of dice to be rolled."
                raise ValueError

            dice_quantity = int(dice_quantity)
            original_dice_quantity = dice_quantity

            # Rolling 0 dice.
            if (dice_quantity == 0):
                error_reason = "It's impossible to roll 0 dice."
                raise ValueError

            # Setting singular or plural.
            if (dice_quantity == 1):
                die_dice = " die"
                sum_message = "Result"
            else:
                die_dice = " dice"
                sum_message = "Total sum"

            list_input = list(user_input)
            d_idx = user_input.index("d") + 1
            final_char = len(list_input)
            mod_to_do = ""
            mod_value = ""
            bonus = ""
            penalty = ""

            # Part after the 'd' in user's input.
            for character in range(d_idx, final_char):

                # Setting number of faces that the dice will have.
                if (list_input[character].isdigit()):
                    dice_faces += str(list_input[character])

                # User added a bonus.
                elif (list_input[character] == "+"):
                    mod_idx = user_input.index("+") + 1
                    mod_to_do = True
                    mod_type = "bonus"
                    mod_value = 0
                    break

                # User added a penalty.
                elif (list_input[character] == "-"):
                    mod_idx = user_input.index("-") + 1
                    mod_to_do = True
                    mod_type = "penalty"
                    mod_value = 0
                    break

            # If there's one modifier that the program hasn't determinate its value.
            while (mod_to_do == True):

                # If it's the last modifier this won't run again.
                mod_to_do = False
                original_mod_idx = mod_idx

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
                        bonus = ""
                        penalty = ""
                        mod_to_do = True
                        mod_type = "bonus"
                        mod_idx = user_input.index(
                            "+", original_mod_idx, final_char) + 1
                        break

                    # A penalty comes next
                    elif (list_input[character] == "-"):
                        if (bonus != ""):
                            mod_value += int(bonus)
                        elif (penalty != ""):
                            mod_value -= int(penalty)
                        bonus = ""
                        penalty = ""
                        mod_to_do = True
                        mod_type = "penalty"
                        mod_idx = user_input.index(
                            "-", original_mod_idx, final_char) + 1
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
                error_reason = "After the letter 'd', it must be typed the number of faces that the dice will have."
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

            # If we run this code, there's no error in user's input.
            error = False

            row_to_do = True  # Used to display each dice result.
            print("")

            # For organized result output.
            if (dice_faces <= 99):
                list_width = 25
            elif (dice_faces <= 999):
                list_width = 22
            elif (dice_faces <= 9999):
                list_width = 18
            elif (dice_faces <= 99999):
                list_width = 16
            else:
                list_width = 12

            # Used to justify each dice result.
            dice_faces_digits = len(str(dice_faces))

            # Rolling and displaying each dice result
            for die in range(dice_quantity):

                result = random.randint(1, dice_faces)
                result_list.append(result)
                summation += result

                if (die % list_width != list_width - 1) and (die != dice_quantity - 1):
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
                print("\nDone. Rolled " + str(original_dice_quantity) + die_dice + " of " + str(dice_faces) +
                      face_faces + modifier + ".\n" + sum_message + mod_message + str(summation) + ".")

            # Roll result message (no modifier(s)).
            else:
                print("\nDone. Rolled " + str(original_dice_quantity) + die_dice + " of " + str(
                    dice_faces) + face_faces + ".\n" + sum_message + ": " + str(summation) + ".")

            # Showing highest die only if more than 1 die was rolled.
            if (original_dice_quantity != 1):
                print("Highest die: " + str(max(result_list)) + ".")

        except:

            # Error message with its reason.
            print("\nSorry, unable to understand.\nReason: " + error_reason)
            user_input = str(
                input("\nPlease, try again ('q' to Quit, 'h' for Help): ")).lower()
            error = True
            continue

# Quitting program.
print("\nThanks for using DiceMaster (v3.3.5). Hope you enjoyed it.\nPowered by Luis M. Isea.")
