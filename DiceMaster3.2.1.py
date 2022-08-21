#DiceMaster version 3.2.1
#Author: @LuimiDev (GitHub)

# Libraries
import os
import random

# Clearing the Terminal
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
clear()

# Displaying the Menu
starting = False
quitting = False
menu_attempts = 0
print ("Greetings, dear user. Welcome to DiceMaster powered by LuimiDev.\n\nType 's' for STARTING.\nType 'i' for INSTRUCTIONS.\nType 'q' for QUITTING.\nDISCLAIMER: It's highly recommended to read the Instructions the first time.\n\nDiceMaster v3.2.1 - August 2022\n")
menu_input = str(input ())


while (starting != True) or (quitting != True):
    
    # User types 's' - Starting from Menu
    if (menu_input == "s") or (menu_input == "S") or (menu_input == "start") or (menu_input == "Start") or (menu_input == "START"):
        starting = True
        break
    
    # User types 'q' - Quitting from Menu
    elif (menu_input == "q") or (menu_input == "Q") or (menu_input == "QUIT") or (menu_input == "quit") or (menu_input == "Quit"):
        quitting = True
        break
    
    # User types 'i' - Displaying Instructions
    elif (menu_input == "i") or (menu_input == "I") or (menu_input == "Instructions") or (menu_input == "instructions") or (menu_input == "INSTRUCTIONS"):
        
        # Setting Variables
        menu_input = ""
        instructions_attempts = 0

        clear () # Clearing Terminal
        # Instructions Message
        print ("INSTRUCTIONS\n\nHOW TO ROLL?\nYou can now roll any kind of die you want, just as many times you desire.\nIt's as simply as writing first how many dice you want to roll, later write 'd' and next how many faces does that kind of die has.\nNOTE: Please, don't press the space bar between these things.\nFor example:\nIf you write '2d6', this will roll 2 dice of 6 faces.\nIf you write '100d20', this will roll 100 dice of 20 faces.\n\nBONUS\nAdding a Bonus it's just as simply as typing ' +bonus_value' after the standard syntax for rolling in DiceMaster. This will increase the total sum of the dice rolled by the bonus_value\n\nPENALTY\nAdding a Penalty it's just as simply as typing ' -penalty_value' after the standard syntax. This will decrease the total sum of the dice rolled by the penalty_value\n\nFor example:\nIf you write '1d8 +2', this will roll 1 die of 8 faces plus a 2 bonus.\nIf you write '8d12 -5', this will roll 8 dice of 12 faces minus a 5 penalty.")
        instructions_input = str(input ("\nGot it? wanna try? Type 's' for STARTING (or type 'q' for QUITTING): "))
        
        
        while (starting != True) or (quitting != True):
            
            # User types 's'
            if (instructions_input == "s") or (instructions_input == "S") or (instructions_input == "start") or (instructions_input == "Start") or (instructions_input == "START"):
                starting = True
                break
            
            # User types 'q'
            elif (instructions_input == "q") or (instructions_input == "Q") or (instructions_input == "QUIT") or (instructions_input == "Quit") or (instructions_input == "quit"):
                quitting = True
                break
            
            # User types something else - Repeating Available Options
            else:
                instructions_input = str(input ("\nSorry, I don't understand. Type 's' for STARTING (or 'q' to QUIT): "))
                instructions_attempts += 1
                
                # Quitting from Instructions Repetition 
                if (instructions_attempts == 3):
                    print ("\nI'm afraid you are just looping too much. The program is about to quit due to exaggerated repetition. Apologizes for the inconveniences.")
                    quitting = True
                    break
                
                # Repeating While expecting a Valid Input
                continue
            
        # Starting from Instructions
        if (starting == True):
                break
            
        # Quitting from Instructions
        elif (quitting == True):
                break
            
    # User types something else than 's','q' or 'i' - Repeating Available Options 
    else:
        menu_input = str(input ("\nSorry, I don't understand. Type 's' for STARTING, 'i' for INSTRUCTIONS (or 'q' for QUITTING): "))
        menu_attempts += 1
        
        # Quitting from Menu Repetition
        if (menu_attempts == 3):
            print ("\nI'm afraid you are just looping too much. The program is about to quit due to exaggerated repetition. Apologizes for the inconveniences.")
            quitting = True
            break
        
        # Repeating While expecting a Valid Input
        continue
    
# Starting DiceMaster
if (starting == True):
    clear() # Cleaning Terminal
    first_time = True
    error_reason = ""
    
    
    while (quitting != True):
        try:
            
            # Setting Variables
            times = ""
            faces = ""
            bonus = ""
            penalty = ""
            d_times = 0
            
            # First Time Roll Message
            if first_time == True:
                choice = str(input("If you're so kind, please write what you want to roll (Type 'q' to quit): "))
                first_time = False
                
            # Further Time Roll Message
            elif (first_time == False) and (error == False):
                choice = str(input("\nIf you want, you can roll something else or type 'q' to quit: "))
                
            # User types 'q'
            if (choice == "q") or (choice == "Q") or (choice =="quit") or (choice == "Quit") or (choice == "QUIT"):
                quitting = True
                break
            
            # User types something else than 'q' 
            for x in choice:
                if (x.isalpha()) and (x != "d"):
                    error_reason = "There's a letter that is not d, the d is necessary"
                    raise NameError
                if (x.isalpha()) and (x == "d"):
                    d_times += 1
            if d_times != 1:
                error_reason = "The letter d must be once and only once"
                raise NameError
            error = False
            for x in choice:
                if (x != "d"):
                    times += str(x)
                else:
                    break
            if (times==""):
                error_reason = "You must type a number before typing the letter d"
                raise NameError
            times = int(times)
            list_choice = list(choice)
            d = choice.index("d") + 1
            f = len(list_choice)
            for x in range(d,f):
                if (list_choice[x].isdigit()):
                    faces += str(list_choice[x])
                elif (list_choice[x] == "+"):
                    break
                elif (list_choice[x] == "-"):
                    break
            if ("+" in list_choice):
                plus = choice.index("+") + 1
                for x in range(plus,f):
                    if (list_choice[x].isdigit()):
                        bonus += str(list_choice[x])
            if ("-" in list_choice):
                less = choice.index("-") + 1
                for x in range(less,f):
                    if (list_choice[x].isdigit()):
                        penalty += str(list_choice[x])
            faces = int(faces)
            if (bonus != ""):
                bonus = int(bonus)
            if (penalty != ""): 
                penalty = int(penalty)
            result = 0
            list_value = []
            for x in range(times):
                value = random.randint(1,faces)
                print (value)
                list_value.append(value)
                result += value
            if (bonus != ""):
                result += bonus
                print("Just as you wanted. You just rolled " + str(times) + " dice(s) of " + str(faces) + " face(s) plus a bonus of " + str(bonus) + "\nThe total sum of rolled dice(s) plus the bonus is: " + str(result))
            elif (penalty != ""):
                result -= penalty
                print("Just as you wanted. You just rolled " + str(times) + " dice(s) of " + str(faces) + " face(s) minus a penalty of " + str(penalty) + "\nThe total sum of rolled dice(s) minus the penalty is: " + str(result))
            else:
                print("Just as you wanted. You just rolled " + str(times) + " dice(s) of " + str(faces) + " face(s)\nThe total sum of rolled dice(s) is: " + str(result))
            print("The highest die result rolled was: " + str(max(list_value)))
        except NameError:
            print ("\nSorry, I don't understand that")
            if (error_reason != ""):
                print (error_reason)
            choice = str(input("\nLet's try again. What do you wanna roll? (Type 'q' to quit): "))
            error = True
            continue
        
# Quitting Program
if quitting == True :
    print ("\nThanks for using DiceMaster (v3.2.1). Hope you enjoyed it. Come back soon :D\nPowered by LuimiDev")