# Imports libraries
import math as m

# Declare Variables
repeat = "yes"
restart = "no"

# Functions
def round(roundamount,answer):
    if roundamount == 0 or roundamount > 20:
        print("You can't round to 0 or over 20")
    else:
        answer = round(answer, roundamount)
    return answer
def validation(type,question):
    if type == "str":
        while True:
            variable = (input(question))
            if variable.isdigit():
                continue
            else:
                variable = str(variable).lower()
                return variable
                break
    elif type == "int":
        while True:
            variable = (input(question))
            if variable.isdigit():
                variable = str(variable).lower()
                return variable
                break
            else:
                continue
    elif type == "float":
        while True:
            variable = (input(question))
            if variable.isdigit():
                variable = str(variable).lower()
                return variable
                break
            else:
                continue
def Start_Screen():
    print("""===============================
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

#Title Screen
print("Welcome to Pythonagorus")#title
print("Press enter to continue")
input()#makes the user click enter to continue

#Main Code

while repeat == "yes":
    print("""===============================
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
    if find == 1 and knowone == "true":
        restart = "yes"
    elif find == 2 and knowtwo == "true":
        restart = "yes"
    elif find == 3 and knowthree == "true":
        restart = "yes"
    elif find == 4 and knowfour == "true":
        restart = "yes"

    if restart == "no":
        #Tan
        if knowtwo == "true"  and knowfour == "true" and find == 1:#Don't know interior angle
            opposite = validation("float", "What is the opposite? ")
            adjacent = validation("float", "What is the adjacent? ")
            answer = m.degrees(m.atan(opposite / adjacent))#InverseTan
        elif knowone == "true" and knowfour == "true" and find == 2:#Don't know opposite side
            interiorAngle = validation("float", "What is the interior angle? ")
            adjacent = validation("float", "What is the adjacent? ")
            answer = m.degrees(m.tan(interiorAngle) * adjacent)#Tan
        elif knowone == "true" and knowtwo == "true" and find == 4:#Don't know adjacent side
            interiorAngle = validation("float", "What is the interior angle? ")
            opposite = validation("float", "What is the opposite? ")
            answer = m.degrees(opposite / m.tan(interiorAngle))#Tan
        
        #Sine
        elif knowtwo == "true" and knowthree == "true" and find == 1:#Don't know interior angle
            opposite = validation("float", "What is the opposite? ")
            hypotenuse = validation("float", "What is the hypotenuse? ")
            answer = m.degrees(m.sinh(opposite / hypotenuse))#InverseSine
        elif knowone == "true" and knowthree == "true" and find == 2:
            interiorAngle = validation("float", "What is the interior angle? ")
            hypotenuse = validation("float", "What is the hypotenuse? ")
            answer = m.degrees(m.sin(interiorAngle) * hypotenuse)#Sine
        elif knowone == "true" and knowtwo == "true" and find == 3:
            interiorAngle = validation("float", "What is the interior angle? ")
            opposite = validation("float", "What is the opposite? ")
            answer = m.degrees(opposite / m.sin(interiorAngle))#Sine
        
        #Cosine
        elif knowfour == "true" and knowthree == "true" and find == 1:
            adjacent = validation("float", "What is the adjacent? ")
            hypotenuse = validation("float", "What is the hypotenuse? ")
            answer = m.degrees(m.cosh(adjacent / hypotenuse))#InverseCosine
        elif knowone == "true" and knowfour == "true" and find == 3:
            interiorAngle = validation("float", "What is the interior angle? ")
            adjacent = validation("float", "What is the adjacent? ")
            answer = m.degrees(adjacent / m.cos(interiorAngle))#Cosine
        elif knowone == "true" and knowthree == "true" and find == 4:
            interiorAngle = validation("float","What is the interior angle? ")
            hypotenuse = validation("float", "What is the hypotenuse? ")
            answer = m.degrees(hypotenuse * m.cos(interiorAngle))#Cosine

        elif knowone == "true" and knowtwo == "true" and find == 4:
            otherlength = validation("float","What is the other length? ")
            hypotenuse = validation("float", "What is the hypotenuse? ")
            answer = m.sqrt((m.pow(hypotenuse, 2) - m.pow(otherlength, 2)))
        elif knowthree == "true" and knowfour == "true" and find == 2:
            hypotenuse = validation("float", "What is the hypotenuse? ")
            adjacent = validation("float", "What is the adjacent? ")
            answer = m.sqrt((m.pow(adjacent, 2) - m.pow(hypotenuse, 2)))
        elif knowone == "true" and knowtwo == "true" and find == 3:
            otherlengthone = validation("float", "Please enter one of the other lengths: ")
            otherlengthtwo = validation("float","Please enter the other length: ")
            answer = m.sqrt((m.pow(otherlengthone, 2) + m.pow(otherlengthtwo, 2)))

        print("The missing side is", answer)
        roundamount = validation("int", "How many decimal places do you want to round the answer to? ")
        print("The missing side is", round(roundamount,answer))#rounds the answer
        repeat = validation("str", "Do you wish to continue?(yes/no) ")#Ends loop
    else:
        print("""If you know a side then why do you want to find it?
""")