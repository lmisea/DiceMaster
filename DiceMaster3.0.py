#Libraries
import os
import random
#Cleaning the terminal
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
clear()
#Displaying the menu
starting = False
quitting = False
menu_attempts = 0
print ("Greetings, dear user. Welcome to DiceMaster powered by Luimi.\n")
print ("Type 's' for STARTING. DISCLAIMER: It's highly recommended to read the Instructions the first time.\n")
print ("Type 'i' for INSTRUCTIONS.\n")
print ("Type 'q' for QUITTING.\n")
print ("DiceMaster v3.1 - August 2022\n")
menu_input = str(input ())
while (starting != True) or (quitting != True):
    #Starting from menu
    if (menu_input == "s") or (menu_input == "S"):
        starting = True
        break
    elif (menu_input == "i") or (menu_input == "I"):
        #Displaying Instructions
        print ("\nINSTRUCTIONS\nYou can now roll any kind of dice as many times you desire.\nIt's as simply as writing first how many dices you want to roll, later write 'd' and next how many faces does that kind of dice have. \nNOTE: Please, don't press the space bar between these things.\nFor example:\n If you write '2d6', this will roll 2 dices of 6 faces.\nIf you write '100d20', this will roll 100 dices of 20 faces. Got it?\n")
        instructions_input = str(input ("Wanna try? Type 's' for STARTING or type 'q' for quitting: "))
        instructions_attempts = 0
        while (starting != True) or (quitting != True):
            #Starting from instructions
            if (instructions_input == "s") or (instructions_input == "S"):
                starting = True
                break
            #Quitting from instructions
            elif (instructions_input == "q") or (instructions_input == "Q"):
                quitting = True
                break
            else:
                print ("Sorry, I don't understand. Type 's' for STARTING or 'q' for quitting")
                instructions_input = str(input ())
                instructions_attempts += 1
                #Quitting from instruction repetition 
                if (instructions_attempts == 5):
                    print ("I'm afraid you are just looping too much. The program is about to quit due to exaggerated repetition. Apologizes for the inconveniences.")
                    quitting = True
                    break
                continue
    #Quitting from menu
    elif (menu_input == "q") or (menu_input == "Q"):
        quitting = True
        break
    else:
        print ("Sorry, I don't understand. Type 's' for STARTING, 'i' for INSTRUCTIONS or 'q' for QUITTING")
        menu_input = str(input ())
        menu_attempts += 1
        if (menu_attempts == 5):
            print ("I'm afraid you are just looping too much. The program is about to quit due to exaggerated repetition. Apologizes for the inconveniences.")
            quitting = True
            break
        continue
# \nMany games are based on the use of dices. But unfortunately not all the dices used in games have 6 faces (d6), many have an uncommon number of faces and we don't have that specific kind of dice in home :(\nOr may be the case that a game asked to roll a huge quantity of dices, that we don't have\n\nThis is when DiceMaster comes in.")
# Starting DiceMaster
if (starting == True):
    clear()
    first_time = True
    choice = ""
    error_reason=""
    while (choice != "q") or (choice != "Q") or (choice !="quit") or (choice != "Quit") or (choice != "QUIT"):
        try:
            times = ""
            faces = ""
            bonus = ""
            penalty = ""
            if first_time == True:
                choice = str(input("If you're so kind, please write what you want to roll (Type 'q' to quit): "))
                first_time = False
            elif (first_time == False) and (error==False):
                choice = str(input("If you want, you can roll something else or type 'q' to quit: "))
            if (choice == "q") or (choice == "Q") or (choice =="quit") or (choice == "Quit") or (choice == "QUIT"):
                break
            d_times = 0
            for x in choice:
                if (x.isalpha()) and (x != "d"):
                    error_reason="There's a letter that is not d, the d is necessary"
                    raise NameError
                if (x.isalpha()) and (x == "d"):
                    d_times+=1
            if d_times != 1:
                error_reason="The letter d must be once and only once"
                raise NameError
            error = False
            for x in choice:
                if (x != "d"):
                    times+=str(x)
                else:
                    break
            if (times==""):
                error_reason="You must type a number before typing the letter d"
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
            print("The hightest dice result rolled was: " + str(max(list_value)))
        except NameError:
            print ("\nSorry, I don't understand that")
            if (error_reason != ""):
                print (error_reason)
            choice = str(input("Let's try again. What do you wanna roll (Type q to quit): "))
            error = True
            continue
#Quitting program
if quitting == True :
    print ("\nThanks for using this program. Hope you enjoyed it. Come back soon :D\nPowered by Luimi")