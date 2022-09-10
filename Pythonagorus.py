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

#Title Screen
print("Welcome to Pythonagorus")#title
print("Press enter to continue")
input()#makes the user click enter to continue
#Title Menu
print("""    =============================
    ||       Modes:            ||
    || 1: Pythagourus          ||
    || 2: Debug                ||
    =============================""")#Prints the menu
mode = int(input("What mode do you want to load?(Use numbers) "))#asks the user what mode they want to load

#Main Code
if mode == 1:#runs the Pythonagourus code
    while repeat == "yes": #Repeats
        while True:
            rightangletriangle = input("Does your triangle have a right angle? ")
            check = str_validation(rightangletriangle)
            if check == "yes":
                rightangletriangle=str(rightangletriangle).lower()
                break
            else:
                continue
        twosides=str(input("Do you know 2 of the sides? ")).lower()
        if rightangletriangle == "yes" and twosides == "yes":
            Hypotenuse = str(input("Do you know the Hypotenuse?(Side opposite the right angle) ")).lower()
            otherlength = str(input("Do you know the other length? ")).lower()
            if Hypotenuse == "yes" and otherlength == "yes":
                Hypotenuse = float(input("What is the Hypotenuse? "))
                otherlength=float(input("What is the other length? "))
                answer = math.sqrt((pow(Hypotenuse, 2)-pow(otherlength,2)))
            elif Hypotenuse == "no" and otherlength == "yes":
                otherlengthone = float(input("Please enter one of the other lengths: "))
                otherlengthtwo = float(input("Please enter the other length: "))
                answer = math.sqrt((pow(otherlengthone, 2)+pow(otherlengthtwo,2)))
            else:
                answer = "error"
            if answer.isdigit():
                print("The missing side is", answer)
                roundamount = int(input("How many decimal places do you want to round the answer to? "))
                print(round_answer(roundamount,answer))
        elif rightangletriangle == "no" or twosides == "no":
            print("Sorry I can't help you")
        else:
            print("Yes or No")
        repeat = str(input("Do you wish to continue?(yes/no) ")).lower()
elif mode == 2:
    print("""    ============================
    ||       Debug menu       ||
    || version: 2.1           ||
    || libraries: math        ||
    || comments: 14            ||
    ============================""")#Prints the debug screen