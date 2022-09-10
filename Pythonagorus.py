# Imports libraries
import math # imports the math library

#Declares variables
repeat = "yes"
sure = "no"
mode = 0
rightangletriangle = "rr"

#Functions
def round_answer(roundamount,answer):
    if roundamount == 0 or roundamount > 20:
        print("You can't round to 0 or over 20")
    else:
        answer = round(answer, roundamount)
    return answer
def str_validation(validation_word):
    if validation_word.isdigit():
        return "no"
    else:
        return "yes"
def intorfloat_validation(validation_number):
    if validation_number.isdigit():
        return "yes"
    else:
        return "no"
def validation(type,question):
    if type == "str":
        while True:
            variable = (input(question))
            check = str_validation(variable)
            if check == "yes":
                variable = str(variable).lower()
                return variable
                break
            else:
                continue
    elif type == "int":
        while True:
            variable = (input(question))
            check = intorfloat_validation(variable)
            if check == "yes":
                variable = int(variable)
                return variable
                break
            else:
                continue
    elif type == "float":
        while True:
            variable = (input(question))
            check = intorfloat_validation(variable)
            if check == "yes":
                variable = float(variable)
                return variable
                break
            else:
                continue

#Title Screen
print("Welcome to Pythonagorus")#title
print("Press enter to continue")
input()#makes the user click enter to continue
#Title Menu
print("""
    =============================
    ||       Modes:            ||
    || 1: Pythagourus          ||
    || 2: Debug                ||
    =============================""")#Prints the menu
mode = int(input("What mode do you want to load?(Use numbers) "))#asks the user what mode they want to load

#Main Code
if mode == 1:#runs the Pythonagourus code
    while repeat == "yes": #Repeats
        rightangletriangle = validation("str","Does your triangle have a right angle? ")
        twosides = validation("str","Do you know 2 of the sides? ")
        if rightangletriangle == "yes" and twosides == "yes":
            Hypotenuse = validation("str","Do you know the Hypotenuse?(Side opposite the right angle) ")
            otherlength = validation("str","Do you know the other length? ")
            if Hypotenuse == "yes" and otherlength == "yes":
                Hypotenuse = validation("float", "What is the Hypotenuse? ")
                otherlength = validation("float", "What is the other length? ")
                answer = math.sqrt((pow(Hypotenuse, 2)-pow(otherlength,2)))
            elif Hypotenuse == "no" and otherlength == "yes":
                otherlengthone = validation("float", "Please enter one of the other lengths: ")
                otherlengthtwo = validation("float","Please enter the other length: ")
                answer = math.sqrt((pow(otherlengthone, 2)+pow(otherlengthtwo,2)))
            else:
                answer = "Sorry I can't help you"
            if answer == "Sorry I can't help you":
                print(answer)
            else:
                print("The missing side is", answer)
                roundamount = validation("int", "How many decimal places do you want to round the answer to? ")
                print(round_answer(roundamount,answer))#rounds the answer
        elif rightangletriangle == "no" or twosides == "no":
            print("Sorry I can't help you")
        else:
            print("Yes or No")
        repeat = ("str", "Do you wish to continue?(yes/no) ")#Ends loop
elif mode == 2:
    print("""
    ============================
    ||       Debug menu       ||
    || version: 2.1           ||
    || libraries: math        ||
    || comments: 16           ||
    ============================""")#Prints the debug screen