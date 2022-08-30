# DiceMaster version 3.3.4 - August 2022. Caracas, Venezuela.
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

starting = False                # When is set to True, the main functionality initializes.
quitting = False                # Whenever is set to True, the program is terminated.
display_instructions = False    # When is set to True, the instructions are displayed.
# menu_attempts = 0              # Used to avoid exaggerated repetition.
# instructions_attempts = 0      # Used to avoid exaggerated repetition.
instructions_page = 1           # Used to display different instructions for every page.

first_page_message = "INSTRUCTIONS\n\nHOW TO ROLL?\nYou can now roll any kind of die you want, just as many times you desire.\nIt's as simply as writing first how many dice you want to roll, later write 'd' and next how many faces does that kind of dice have.\nFor example:\nIf you write '2d6', this will roll 2 dice of 6 faces.\nIf you write '100 d 20', this will roll 100 dice of 20 faces.\n\nPress 'n' for NEXT PAGE, 's' for STARTING or 'q' for QUITTING."

second_page_message = "HOW TO ADD A BONUS?\nAfter the standard syntax for rolling, just add '+' and then the bonus value. This will increase the total sum of the dice rolled by the bonus value.\nHOW TO ADD A PENALTY?\nAfter the standard syntax for rolling, just add '-' and then the penalty value. This will decrease the total sum of the dice rolled by the penalty value.\nFor example:\nIf you write '1d8+2', this will roll 1 die of 8 faces plus a 2 bonus.\nIf you write '8d12 -5', this will roll 8 dice of 12 faces minus a 5 penalty.\n\nPress 'p' for PREVIOUS PAGE, 's' for STARTING or 'q' for QUITTING."


def menu_press(key):
    """
    When 's' is pressed, starts the main functionality.\n
    When 'i' is pressed, the instructions are displayed.\n
    When 'q' is pressed, the program shuts down.\n
    When any other key is pressed, doesn't trigger anything.
    """
    # global menu_attempts
    global starting
    global display_instructions
    global quitting

    if (key == "s"):
        sshkeyboard.stop_listening()
        starting = True
        return
    elif (key == "i"):
        sshkeyboard.stop_listening()
        display_instructions = True
        return
    elif (key == "q"):
        sshkeyboard.stop_listening()
        quitting = True
        return
    # else:
    #     if (menu_attempts < 4):
    #         menu_attempts += 1
    #         print("\nSorry, unable to understand.\nPress 's' for STARTING, 'i' for INSTRUCTIONS or 'q' for QUITTING.")
    #     elif (menu_attempts == 4):
    #         print("\nYou are looping too much. Quitting program due to exaggerated repetition. Apologizes for the inconveniences.")
    #         sshkeyboard.stop_listening()
    #         quitting = True
    #         return


def instructions_press(key):
    """
    When 'n' is pressed, the next instructions page is displayed.
    When 'p' is pressed, the previous instructions page is displayed.
    When 's' is pressed, starts the main functionality.
    When 'q' is pressed, the program shuts down.
    When any other key is pressed, doesn't trigger anything.
    """
    # global instructions_attempts
    global instructions_page
    global starting
    global quitting

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
        return
    elif (key == "q"):
        quitting = True
        sshkeyboard.stop_listening()
        return
    # else:
    #     if (instructions_page == 1) and (instructions_attempts < 4):
    #         instructions_attempts += 1
    #         print(
    #             "\nSorry, unable to understand.\nPress 'n' for NEXT PAGE, 's' for STARTING or 'q' for QUITTING.")
    #     elif (instructions_page == 2) and (instructions_attempts < 4):
    #         instructions_attempts += 1
    #         print("\nSorry, unable to understand.\nPress 'p' for PREVIOUS PAGE, 's' for STARTING or 'q' for QUITTING.")
    #     else:
    #         print("\nYou are looping too much. Quitting program due to exaggerated repetition. Apologizes for the inconveniences.")
    #         quitting = True
    #         sshkeyboard.stop_listening()
    #         return


def rolling_press(key):
    """
    When 'i' is pressed, the instructions are displayed.\n
    When 'q' is pressed, the program shuts down.\n
    When any other key is pressed, doesn't trigger anything.
    """

    global display_instructions
    global quitting

    if (key == "i"):
        sshkeyboard.stop_listening()
        display_instructions = True
        return
    elif (key == "q"):
        sshkeyboard.stop_listening()
        quitting = True
        return

# Displaying menu.
print("DiceMaster v3.3.4 - Powered by LuimiDev.\n\nPress 's' for STARTING.\nPress 'i' for INSTRUCTIONS.\nPress 'q' for QUITTING.\nDISCLAIMER: It's highly recommended to read the Instructions the first time.\n")

sshkeyboard.listen_keyboard(on_press=menu_press, until="")

# User pressed 'i' - Displaying instructions.
if (display_instructions == True):
    clear()
    print(first_page_message)    # Instructions message.
    sshkeyboard.listen_keyboard(on_press=instructions_press, until="")

# Starting DiceMaster.
if (starting == True):
    clear()
    first_time = True    # Allows unique first time roll message.
    error_reason = ""    # Explains the user what went wrong.

    while (quitting != True):

        try:
            dice_quantity = ""    # How many dice are going to be roll.
            dice_faces = ""       # How many faces does that kind of dice have.
            d_times = 0           # How many 'd' are in user's input.
            die_dice = ""         # Specifies singular or plural in the roll result message.
            face_faces = ""       # Specifies singular or plural in the roll result message.
            sum_message = ""      # Allows different roll result message when rolling 1 die.
            summation = 0         # The sum of all the results of rolled dice.
            result_list = []      # The record of each dice result.

            # First time roll message.
            if (first_time == True):
                user_input = str(input("Please, write what you want to roll (Type 'q' to Quit): "))
                # sshkeyboard.listen_keyboard(on_press=rolling_press, until="")
                first_time = False

            # Further time roll message.
            elif (first_time == False) and (error == False):
                user_input = str(input("\nRoll something else? (Type 'q' to Quit): "))
                # sshkeyboard.listen_keyboard(on_press=rolling_press, until="")

            # User typed 'q'.
            if (user_input == "q") or (user_input == "Q") or (user_input == "quit") or (user_input == "QUIT") or (user_input == "quit"):
                quitting = True
                break

            # User typed something else than 'q'.
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

            # User typed only numbers and 1 'd': a valid input.
            for character in user_input:

                # Setting quantity of dice to be rolled.
                if (character != "d"):
                    dice_quantity += str(character)
                    # If we use '+= int(character)', we could not handle numbers of two or more digits. E.g.: '24' would become 6.
                else:
                    break

            # There's no number before the 'd'.
            if (dice_quantity == ""):
                error_reason = "Before the letter 'd', it must be typed the number of dice to be rolled."
                raise ValueError

            # By default is a string, we need a number.
            dice_quantity = int(dice_quantity)
            original_dice_quantity = dice_quantity

            # Rolling 0 dice.
            if (dice_quantity == 0):
                error_reason = "It's impossible to roll 0 dice."
                raise ValueError

            # Rolling 1 die.
            if (dice_quantity == 1):
                die_dice = " die"
                sum_message = "Result"

            # Rolling more than 1 die.
            else:
                die_dice = " dice"
                sum_message = "Total sum"

            list_input = list(user_input)    # Converting user's input into a list.
            d = user_input.index("d") + 1    # The position of the 'd' in user's input.
            f = len(list_input)              # How many characters does user's input have.
            original_mod_idx = ""    # Helps detect if more than 1 modifier were typed.
            mod_to_do = ""        # Used to detect bonuses or penalties in user's input.
            mod_type = ""         # Used to determinate if the modifier is a bonus or penalty.
            mod_value = ""        # Defines by what value is modified the final result.
            mod_idx = ""          # The position of the modifier in user's input.
            bonus = ""            # Bonus value added to the total sum of the dice rolled.
            penalty = ""          # Penalty value removed to the total sum of the dice rolled.

            # Part after the 'd' in user's input.
            for character in range(d, f):

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
                for character in range(mod_idx, f):

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
                        mod_idx = user_input.index("+", original_mod_idx, f) + 1
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
                        mod_idx = user_input.index("-", original_mod_idx, f) + 1
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

            # By default is a string, we need a number.
            dice_faces = int(dice_faces)

            # Rolling dice of 0 faces.
            if (dice_faces == 0):
                error_reason = "It's impossible to roll dice of 0 faces."
                raise ValueError

            # Rolling dice of 1 face.
            elif (dice_faces == 1):
                face_faces = " face"

            # Rolling dice of more than 1 face.
            else:
                face_faces = " faces"

            # If we run this code, there's no error in user's input.
            error = False
            
            # Used to display several dice result lists when necessary.
            row_to_do = True
            print("")

            # Setting each dice result list width.
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

            # Roll result message (with bonus).
            if (mod_value != "") and (mod_value > 0):
                summation += mod_value
                print("\nDone. Rolled " + str(original_dice_quantity) + die_dice + " of " + str(dice_faces) + face_faces + " plus " + str(mod_value) + ".\n" + sum_message + " plus bonus: " + str(summation) + ".")

            # Roll result message (with penalty).
            elif (mod_value != "") and (mod_value < 0):
                mod_value = abs(mod_value)
                summation -= mod_value
                print("\nDone. Rolled " + str(original_dice_quantity) + die_dice + " of " + str(dice_faces) + face_faces + " minus " + str(mod_value) + ".\n" + sum_message + " minus penalty: " + str(summation) + ".")

            # Roll result message (modifiers cancelled themselves)
            elif (mod_value != "") and (mod_value == 0):
                print("\nDone. Rolled " + str(original_dice_quantity) + die_dice + " of " + str(dice_faces) + face_faces + " (modifiers cancelled themselves).\n" + sum_message + " (the modifiers cancelled themselves): " + str(summation) + ".")

            # Roll result message (no bonus or penalty).
            else:
                print("\nDone. Rolled " + str(original_dice_quantity) + die_dice + " of " + str(dice_faces) + face_faces + ".\n" + sum_message + ": " + str(summation) + ".")

            # Showing highest die only if more than 1 die was rolled.
            if (original_dice_quantity != 1):
                print("Highest die: " + str(max(result_list)) + ".")

        except:

            # Error message with its reason.
            print("\nSorry, unable to understand.\nReason: " + error_reason)
            user_input = str(input("\nPlease, try again (Type 'q' to Quit): "))
            # It won't ask again what to roll when repeating the loop.
            error = True
            continue

# Quitting program.
if (quitting == True):
    print("\nThanks for using DiceMaster (v3.3.4). Hope you enjoyed it.\nPowered by LuimiDev.")