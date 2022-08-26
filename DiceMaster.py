# DiceMaster version 3.3.3 - August 2022. Caracas, Venezuela.
# Luis Miguel Isea - @LuimiDev (GitHub).

import os
import random

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
clear()    # Clears the terminal.

starting = False    # When is set to True, the main functionality initializes.
quitting = False    # Whenever is set to True, the program is terminated.

# Displaying menu.
print ("DiceMaster v3.3.3 - Powered by LuimiDev.\n\nType 's' for STARTING.\nType 'i' for INSTRUCTIONS.\nType 'q' for QUITTING.\nDISCLAIMER: It's highly recommended to read the Instructions the first time.\n")

menu_input = str(input ())
menu_attempts = 0    # Used to avoid exaggerated repetition.

while (starting != True) or (quitting != True):
    
    # User typed 'i' - Displaying instructions.
    if (menu_input == "i") or (menu_input == "I") or (menu_input == "Instructions") or (menu_input == "instructions") or (menu_input == "INSTRUCTIONS"):
        
        menu_input = ""    # Set to blank to avoid looping.
        instructions_attempts = 0
        clear ()
        
        # Instructions message.
        print ("INSTRUCTIONS\n\nHOW TO ROLL?\nYou can now roll any kind of die you want, just as many times you desire.\nIt's as simply as writing first how many dice you want to roll, later write 'd' and next how many faces does that kind of dice have.\nNOTE: It's permitted to type a space character between these things.\nFor example:\nIf you write '2d6', this will roll 2 dice of 6 faces.\nIf you write '100 d 20', this will roll 100 dice of 20 faces.\n\nBONUS\nAdding a Bonus it's just as simply as typing '+bonus_value' after the standard syntax for rolling in DiceMaster. This will increase the total sum of the dice rolled by the bonus_value.\nPENALTY\nAdding a Penalty it's just as simply as typing '-penalty_value' after the standard syntax. This will decrease the total sum of the dice rolled by the penalty_value.\nNOTE: It's permitted to type a space character between these things.\nFor example:\nIf you write '1d8+2', this will roll 1 die of 8 faces plus a 2 bonus.\nIf you write '8d12 -5', this will roll 8 dice of 12 faces minus a 5 penalty.")
        instructions_input = str(input ("\nGot it? wanna try? Type 's' for STARTING or 'q' for QUITTING: "))
        
        while (starting != True) or (quitting != True):
            
            # User typed 's'.
            if (instructions_input == "s") or (instructions_input == "S") or (instructions_input == "start") or (instructions_input == "Start") or (instructions_input == "START"):
                starting = True
                break
            
            # User typed 'q'.
            elif (instructions_input == "q") or (instructions_input == "Q") or (instructions_input == "QUIT") or (instructions_input == "Quit") or (instructions_input == "quit"):
                quitting = True
                break
            
            # User typed something else - Repeating available options.
            else:
                instructions_input = str(input ("\nSorry, unable to understand.\nType 's' for STARTING or 'q' to QUIT: "))
                instructions_attempts += 1
                
                if (instructions_attempts < 4):
                    continue
                else:
                    print ("\nYou are looping too much. Quitting program due to exaggerated repetition. Apologizes for the inconveniences.")
                    quitting = True
                    break    # Quitting due to exaggerated repetition.
            
    # User typed 's' - Starting.
    elif (menu_input == "s") or (menu_input == "S") or (menu_input == "start") or (menu_input == "Start") or (menu_input == "START") or (starting == True):
        starting = True
        break
    
    # User typed 'q' - Quitting.
    elif (menu_input == "q") or (menu_input == "Q") or (menu_input == "QUIT") or (menu_input == "quit") or (menu_input == "Quit") or (quitting == True):
        quitting = True
        break
    
    # User typed something else than 's','q' or 'i' - Repeating available options. 
    else:
        menu_input = str(input ("\nSorry, unable to understand.\nType 's' for STARTING, 'i' for INSTRUCTIONS (or 'q' for QUITTING): "))
        menu_attempts += 1
        
        if (menu_attempts < 4):
            continue
        else:
            print ("\nYou are looping too much. Quitting program due to exaggerated repetition. Apologizes for the inconveniences.")
            quitting = True
            break    # Quitting due to exaggerated repetition.
    
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
                first_time = False
                
            # Further time roll message.
            elif (first_time == False) and (error == False):
                user_input = str(input("\nRoll something else? (Type 'q' to Quit): "))
                
            # User typed 'q'.
            if (user_input == "q") or (user_input == "Q") or (user_input =="quit") or (user_input == "Quit") or (user_input == "QUIT"):
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
            
            dice_quantity = int(dice_quantity)    # By default is a string, we need a number.
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
            mod_to_do = ""        # Used to detect bonuses or penalties in user's input.
            mod_type = ""         # Used to determinate if the modifier is a bonus or penalty.
            mod_value = ""        # Defines by what value is modified the final result.
            mod_idx = ""          # The position of the modifier in user's input.
            original_mod_idx = "" # Helps detect if more than 1 modifier were typed.
            bonus = ""            # Bonus value added to the total sum of the dice rolled.
            penalty = ""          # Penalty value removed to the total sum of the dice rolled.
            
            # Part after the 'd' in user's input.
            for character in range(d,f):
                
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
                        
                mod_to_do = False    # If it's the last modifier this won't run again.
                original_mod_idx = mod_idx
                
                # Checking what comes after the modifier.        
                for character in range(mod_idx,f):
                        
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
                        mod_idx = user_input.index("+",original_mod_idx,f) + 1
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
                        mod_idx = user_input.index("-",original_mod_idx,f) + 1
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
                        
            dice_faces = int(dice_faces)    # By default is a string, we need a number.
            
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
                
            error = False       # If we run this code, there's no error in user's input.
            row_to_do = True    # Used to display several dice result lists when necessary,
            print ("")
            
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
                
            dice_faces_digits = len(str(dice_faces))    # Used to justify each dice result.
            
            # Rolling and displaying each dice result
            for die in range(dice_quantity):
                
                result = random.randint(1,dice_faces)
                result_list.append(result)
                summation += result
                
                if (die % list_width != list_width - 1) and (die != dice_quantity -1):
                    print (repr(result).rjust(dice_faces_digits),end="  ")
                    
                elif (die == dice_quantity -1):
                    print (repr(result).rjust(dice_faces_digits),end="")
                    
                else:
                    print (repr(result).rjust(dice_faces_digits),end="\n")
            
            print("",end="\n")
                
            # Roll result message (with bonus).
            if (mod_value != "") and (mod_value > 0):
                summation += mod_value
                print ("\nDone. Rolled " + str(original_dice_quantity) + die_dice + " of " + str(dice_faces) + face_faces + " plus " + str(mod_value) + ".\n" + sum_message + " plus bonus: " + str(summation) + ".")
                
            # Roll result message (with penalty).  
            elif (mod_value != "") and (mod_value < 0):
                mod_value = abs(mod_value)
                summation -= mod_value
                print ("\nDone. Rolled " + str(original_dice_quantity) + die_dice + " of " + str(dice_faces) + face_faces + " minus " + str(mod_value) + ".\n" + sum_message + " minus penalty: " + str(summation) + ".")
                
            # Roll result message (modifiers cancelled themselves)
            elif (mod_value != "") and (mod_value == 0):
                print ("\nDone. Rolled " + str(original_dice_quantity) + die_dice + " of " + str(dice_faces) + face_faces + " (modifiers cancelled themselves).\n" + sum_message + " (the modifiers cancelled themselves): " + str(summation) + ".")
            
            # Roll result message (no bonus or penalty).    
            else:
                print ("\nDone. Rolled " + str(original_dice_quantity) + die_dice + " of " + str(dice_faces) + face_faces + ".\n" + sum_message + ": " + str(summation) + ".")
            
            # Showing highest die only if more than 1 die was rolled.   
            if (original_dice_quantity != 1):
                print("Highest die: " + str(max(result_list)) + ".")
            
        except:
            
            # Error message with its reason.
            print ("\nSorry, unable to understand.\nReason: " + error_reason)
            user_input = str(input("\nPlease, try again (Type 'q' to Quit): "))
            error = True    # It won't ask again what to roll when repeating the loop.
            continue
        
# Quitting program.
if quitting == True :
    print ("\nThanks for using DiceMaster (v3.3.3). Hope you enjoyed it.\nPowered by LuimiDev.")