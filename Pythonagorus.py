# Imports libraries
from math import * # imports the math library

#Declares variables
repeat = "yes"
sure = "no"
mode = 0

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
def bool_validation(validation_state):
    if validation_state == True:
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
    elif type == "bool":
        while True:
            variable = (input(question))
            check = bool_validation(variable)
            if check == "yes":
                variable = bool(variable)
                return variable
                break
            else:
                continue

#Title Screen
print("Welcome to Pythonagorus")#title
print("Press enter to continue")
input()#makes the user click enter to continue

#Main Code

while repeat == "yes":
    print("""===============================
|| What do you want to find? ||
|| 1: The Interior angle     ||
|| 2: The Opposite side      ||
|| 3: The Hypotenuse         ||
|| 4: The Adjacent side      ||
===============================""")
    find = validation("int","What do you want to find? ")
    knowone = validation("str","Do you know the interior angle?(True or False) ")
    knowtwo = validation("str","Do you know the opposite side?(True or False) ")
    knowthree = validation("str","Do you know the Hypotenuse?(True or False) ")
    knowfour = validation("str","Do you know the adjacent side?(True or False) ")

    #Tan
    if knowtwo == "true"  and knowfour == "true" and find == 1:#Don't know interior angle
        opposite = validation("float", "What is the opposite? ")
        adjacent = validation("float", "What is the adjacent? ")
        answer = degrees(atan(opposite / adjacent))#InverseTan
    elif knowone == "true" and knowfour == "true" and find == 2:#Don't know opposite side
        interiorAngle = validation("float", "What is the interior angle? ")
        adjacent = validation("float", "What is the adjacent? ")
        answer = degrees(tan(interiorAngle) * adjacent)#Tan
    elif knowone == "true" and knowtwo == "true" and find == 4:#Don't know adjacent side
        interiorAngle = validation("float", "What is the interior angle? ")
        opposite = validation("float", "What is the opposite? ")
        answer = degrees(opposite / tan(interiorAngle))#Tan
    
    #Sine
    elif knowtwo == "true" and knowthree == "true" and find == 1:#Don't know interior angle
        opposite = validation("float", "What is the opposite? ")
        hypotenuse = validation("float", "What is the hypotenuse? ")
        answer = degrees(sinh(opposite / hypotenuse))#InverseSine
    elif knowone == "true" and knowthree == "true" and find == 2:
        interiorAngle = validation("float", "What is the interior angle? ")
        hypotenuse = validation("float", "What is the hypotenuse? ")
        answer = degrees(sin(interiorAngle) * hypotenuse)#Sine
    elif knowone == "true" and knowtwo == "true" and find == 3:
        interiorAngle = validation("float", "What is the interior angle? ")
        opposite = validation("float", "What is the opposite? ")
        answer = opposite / sin(interiorAngle)#Sine
    
    #Cosine
    elif knowfour == "true" and knowthree == "true" and find == 1:
        adjacent = validation("float", "What is the adjacent? ")
        hypotenuse = validation("float", "What is the hypotenuse? ")
        answer = degrees(cosh(adjacent / hypotenuse))#InverseCosine
    elif knowone == "true" and knowfour == "true" and find == 3:
        interiorAngle = validation("float", "What is the interior angle? ")
        adjacent = validation("float", "What is the adjacent? ")
        answer = adjacent / cos(interiorAngle)#Cosine
    elif knowone == "true" and knowthree == "true" and find == 4:
        interiorAngle = validation("float","What is the interior angle? ")
        hypotenuse = validation("float", "What is the hypotenuse? ")
        answer = hypotenuse * cos(interiorAngle)#Cosine

    elif knowone == "true" and knowtwo == "true" and find == 4:
        otherlength = validation("float","What is the other length? ")
        hypotenuse = validation("float", "What is the hypotenuse? ")
        answer = sqrt((pow(hypotenuse, 2)-pow(otherlength,2)))
    elif knowthree == "true" and knowfour == "true" and find == 2:
        hypotenuse = validation("float", "What is the hypotenuse? ")
        adjacent = validation("float", "What is the adjacent? ")
        answer = sqrt((pow(adjacent, 2)-pow(hypotenuse,2)))
    elif knowone == "true" and knowtwo == "true" and find == 3:
        otherlengthone = validation("float", "Please enter one of the other lengths: ")
        otherlengthtwo = validation("float","Please enter the other length: ")
        answer = sqrt((pow(otherlengthone, 2) + pow(otherlengthtwo, 2)))

    print("The missing side is", answer)
    roundamount = validation("int", "How many decimal places do you want to round the answer to? ")
    print("The missing side is", round_answer(roundamount,answer))#rounds the answer
    repeat = validation("str", "Do you wish to continue?(yes/no) ")#Ends loop