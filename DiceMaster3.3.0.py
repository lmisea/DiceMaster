# DiceMaster version 3.3.0 - August 2022. Caracas, Venezuela.
# Luis Miguel Isea - @LuimiDev (GitHub).

import os
import random

# Clearing Terminal.
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
clear()

starting = False    # When is set to True, the main functionality initializes.
quitting = False    # Whenever is set to True, the program is terminated.

# Displaying Menu.
print ("Greetings, dear user. Welcome to DiceMaster powered by LuimiDev.\n\nType 's' for STARTING.\nType 'i' for INSTRUCTIONS.\nType 'q' for QUITTING.\nDISCLAIMER: It's highly recommended to read the Instructions the first time.\n\nDiceMaster v3.3.0 - August 2022\n")

menu_input = str(input ())
menu_attempts = 0    # Used to avoid exaggerated repetition.
while (starting != True) or (quitting != True):
    
    # User typed 'i' - Displaying Instructions.
    if (menu_input == "i") or (menu_input == "I") or (menu_input == "Instructions") or (menu_input == "instructions") or (menu_input == "INSTRUCTIONS"):
        
        menu_input = ""    # Set to blank to avoid looping.
        instructions_attempts = 0
        clear ()
        
        # Instructions Message.
        print ("INSTRUCTIONS\n\nHOW TO ROLL?\nYou can now roll any kind of die you want, just as many times you desire.\nIt's as simply as writing first how many dice you want to roll, later write 'd' and next how many faces does that kind of dice have.\nNOTE: It's permitted to type a space character between these things.\nFor example:\nIf you write '2d6', this will roll 2 dice of 6 faces.\nIf you write '100 d 20', this will roll 100 dice of 20 faces.\n\nBONUS\nAdding a Bonus it's just as simply as typing '+bonus_value' after the standard syntax for rolling in DiceMaster. This will increase the total sum of the dice rolled by the bonus_value.\nPENALTY\nAdding a Penalty it's just as simply as typing '-penalty_value' after the standard syntax. This will decrease the total sum of the dice rolled by the penalty_value.\nNOTE: It's permitted to type a space character between these things.\nFor example:\nIf you write '1d8+2', this will roll 1 die of 8 faces plus a 2 bonus.\nIf you write '8d12 -5', this will roll 8 dice of 12 faces minus a 5 penalty.")
        instructions_input = str(input ("\nGot it? wanna try? Type 's' for STARTING (or type 'q' for QUITTING): "))
        
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
                instructions_input = str(input ("\nSorry, I don't understand. Type 's' for STARTING (or 'q' to QUIT): "))
                instructions_attempts += 1
                
                if (instructions_attempts < 4):
                    continue
                else:
                    print ("\nI'm afraid you are just looping too much. The program is about to quit due to exaggerated repetition. Apologizes for the inconveniences.")
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
        menu_input = str(input ("\nSorry, I don't understand. Type 's' for STARTING, 'i' for INSTRUCTIONS (or 'q' for QUITTING): "))
        menu_attempts += 1
        
        if (menu_attempts < 4):
            continue
        else:
            print ("\nI'm afraid you are just looping too much. The program is about to quit due to exaggerated repetition. Apologizes for the inconveniences.")
            quitting = True
            break    # Quitting due to exaggerated repetition.
    
# Starting DiceMaster.
if (starting == True):
    clear()
    first_time = True    # Allows unique First Time Roll Message.
    error_reason = ""    # Used to explain the user what went wrong.
    
    while (quitting != True):
        
        try:
            dice_quantity = ""    # How many dice are going to be roll.
            dice_faces = ""       # How many faces does that kind of dice have.
            bonus = ""            # Bonus value added to the total sum of the dice rolled.
            penalty = ""          # Penalty value removed to the total sum of the dice rolled.
            d_times = 0           # How many 'd' are in the user's input.
            plus_times = 0        # How many '+' are in the user's input.
            minus_times = 0       # How many '-' are in the user's input.
            die_dice = ""         # Specifies singular or plural in the Roll Result Message.
            face_faces = ""       # Specifies singular or plural in the Roll Result Message.
            sum_message = ""      # Allows different Roll Result Message when rolling 1 die.
            summation = 0         # The sum of all the results of rolled dice.
            result_list = []      # The record of all the individual results of rolled dice.
            
            # First Time Roll Message.
            if first_time == True:
                user_input = str(input("If you're so kind, please write what you want to roll (Type 'q' to quit): "))
                first_time = False
                
            # Further Time Roll Message.
            elif (first_time == False) and (error == False):
                user_input = str(input("\nDo you wanna roll something else? (type 'q' to quit): "))
                
            # User typed 'q'.
            if (user_input == "q") or (user_input == "Q") or (user_input =="quit") or (user_input == "Quit") or (user_input == "QUIT"):
                quitting = True
                break
            
            # User typed something else than 'q'.
            for character in user_input:
                
                # User typed a different letter than 'd'.
                if (character.isalpha()) and (character != "d"):
                    error_reason = "It cannot be typed a letter that is not 'd'."
                    # It's not defined any function involving other letter than 'd'.
                    raise ValueError
                
                # Counting how many times does 'd' appear in the user's input.
                if (character.isalpha()) and (character == "d"):
                    d_times += 1
            
            # User did not type the letter 'd'.
            if d_times == 0:
                error_reason = "There's no 'd', it has be typed in order to roll anything."
                # If there's no 'd', the program can't set what to roll.
                raise ValueError
                    
            # User typed more than 1 'd'.
            if d_times != 1:
                error_reason = "The letter 'd' must be typed once and only once."
                # If there's more than 1 'd', the program can't set what to roll.
                raise ValueError
            
            # User typed only numbers and 1 'd': a valid input.
            for character in user_input:
                
                # Part Before the 'd' in the user's input.
                if (character != "d"):
                    dice_quantity += str(character)
                    # If we use '+= int(character)', we could not handle numbers of two or more digits. E.g.: '24' would become 6.
                else:
                    break 
            
            # There's no number before the 'd'.
            if (dice_quantity == ""):
                    error_reason = "Before the letter 'd', it must be typed the number of dice to be rolled."
                    # The program cannot roll a non existent quantity of dice.
                    raise ValueError
            
            dice_quantity = int(dice_quantity)    # By default is a string, we need a number.
            
            # Rolling 0 Dice.
            if (dice_quantity == 0):
                error_reason = "It's impossible to roll 0 dice."
                raise ValueError
            
            # Rolling 1 Die.
            if (dice_quantity == 1):
                die_dice = " die"
                sum_message = "The result of the rolled die"
                
            # Rolling more than 1 Die.
            else:
                die_dice = " dice"
                sum_message = "The total sum of the rolled dice"
            
            list_input = list(user_input)    # Converting user's input into a list.
            d = user_input.index("d") + 1    # The position of the 'd' in the user's input.
            f = len(list_input)              # How many characters does the user's input have.
            
            # Part After the 'd' in the user's input.
            for character in range(d,f):
                
                # Number of Faces that the dice will have. 
                if (list_input[character].isdigit()):
                    dice_faces += str(list_input[character])
                
                # User added a Bonus.    
                elif (list_input[character] == "+"):
                    plus = user_input.index("+") + 1
                    
                    for character in range(plus,f):
                        if (list_input[character].isdigit()):
                            bonus += str(list_input[character])
                            
                    bonus = int(bonus)
                    break
                
                # User added a Penalty. 
                elif (list_input[character] == "-"):
                    less = user_input.index("-") + 1
                    
                    for character in range(less,f):
                        if (list_input[character].isdigit()):
                            penalty += str(list_input[character])
                            
                    penalty = int(penalty)
                    break
                    
            # There's no number after the 'd'.
            if (dice_faces == ""):
                error_reason = "After the letter 'd', it must be typed the number of faces that the dice will have."
                # The program cannot roll dice with a non existent quantity of faces.
                raise ValueError
                        
            dice_faces = int(dice_faces)    # By default is a string, we need a number.
            
            # Rolling dice of 0 Faces.
            if (dice_faces == 0):
                error_reason = "It's impossible to roll dice of 0 faces."
                raise ValueError
            
            # Rolling dice of 1 Face.
            elif (dice_faces == 1):
                face_faces = " face"
                
            # Rolling dice of More than 1 Face.
            else:
                face_faces = " faces"
                
            error = False    # If we run this code, there's no error in the user's input.
            
            # Rolling dice.
            for die in range(dice_quantity):
                result = random.randint(1,dice_faces)
                result_list.append(result)
                summation += result
            
            # Displaying each dice result.    
            print ("\n")
            print (result_list)
            print ("\n")
                
            # Roll Result Message (With Bonus).
            if (bonus != ""):
                summation += bonus
                print("Just as you wanted. You just rolled " + str(dice_quantity) + die_dice + " of " + str(dice_faces) + face_faces + " plus a bonus of " + str(bonus) + ".\n" + sum_message + " plus the bonus is: " + str(summation) + ".")
                
            # Roll Result Message (With Penalty).  
            elif (penalty != ""):
                summation -= penalty
                print("Just as you wanted. You just rolled " + str(dice_quantity) + die_dice + " of " + str(dice_faces) + face_faces + " minus a penalty of " + str(penalty) + ".\n" + sum_message + " minus the penalty is: " + str(summation) + ".")
            
            # Roll Result Message (No Bonus or Penalty).    
            else:
                print("Just as you wanted. You just rolled " + str(dice_quantity) + die_dice + " of " + str(dice_faces) + face_faces + ".\n" + sum_message + " is: " + str(result) + ".")
                
            print("The highest die result rolled was: " + str(max(result_list)) + ".")
            
        except:
            
            # Error Message with its Reason.
            print ("\nSorry, I don't understand that.\nReason: " + error_reason)
            user_input = str(input("\nLet's try again. What do you wanna roll? (Type 'q' to quit): "))
            error = True    # It won't ask again what to roll when repeating the loop.
            continue
        
# Quitting Program.
if quitting == True :
    print ("\nThanks for using DiceMaster (v3.3.0). Hope you enjoyed it.\nPowered by LuimiDev.")