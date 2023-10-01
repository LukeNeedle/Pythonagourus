# Imports libraries
import math

# Declare Variables
repeat = True
restart = False

# Functions
def round(roundamount,answer):
    if roundamount == 0 or roundamount > 20:
        print("You can't round to 0 or over 20")
    else:
        answer = round(answer, roundamount)
    return answer

def validation(type,question):
    if type == "str":
        variable = input(question)
        if variable.isdigit():
            variable = validation(type, question)
        
        return str(variable).lower()

    elif type == "int":
        variable = input(question)
        if not variable.isdigit():
            variable = validation(type, question)
        
        return int(variable)
    
    elif type == "bool":
        variable = input(question)
        if variable.isdigit():
            variable = validation(type, question)
        
        if variable == "True" or variable == "true" or variable == True:
            return True
        else:
            return False

    elif type == "float":
        variable = input(question)
        if not variable.isdigit():
            variable = validation(type, question)
        return str(variable).lower()

def Start_Screen():
    print("""===============================
|| 1: The Interior angle     ||
|| 2: The Opposite side      ||
|| 3: The Hypotenuse         ||
|| 4: The Adjacent side      ||
===============================""")
    
    find = validation("int","What do you want to find? ")

    known = []
    known[0] = validation("bool","Do you know the interior angle?(True or False) ")
    known[1] = validation("bool","Do you know the opposite side?(True or False) ")
    known[2] = validation("bool","Do you know the Hypotenuse?(True or False) ")
    known[3] = validation("bool","Do you know the adjacent side?(True or False) ")

    return find, known[0], known[1], known[2], known[3]

print("Welcome to Pythonagorus")#title

while repeat == True:
    known = []
    find, known[0], known[1], known[2], known[3] = Start_Screen()

    if find == 1 and not known[0]:
        pass
    elif find == 2 and not known[1]:
        pass
    elif find == 3 and not known[2]:
        pass
    elif find == 4 and not known[3]:
        pass
    else:
        #Tan
        if known[1] == True  and known[3] == True and find == 1:#Don't know interior angle
            opposite = validation("float", "What is the opposite? ")
            adjacent = validation("float", "What is the adjacent? ")
            answer = math.degrees(math.atan(opposite / adjacent))#InverseTan
        
        elif known[0] == True and known[3] == True and find == 2:#Don't know opposite side
            interiorAngle = validation("float", "What is the interior angle? ")
            adjacent = validation("float", "What is the adjacent? ")
            answer = math.degrees(math.tan(interiorAngle) * adjacent)#Tan
        
        elif known[0] == True and known[1] == True and find == 4:#Don't know adjacent side
            interiorAngle = validation("float", "What is the interior angle? ")
            opposite = validation("float", "What is the opposite? ")
            answer = math.degrees(opposite / math.tan(interiorAngle))#Tan
        
        #Sine
        elif known[1] == True and known[2] == True and find == 1:#Don't know interior angle
            opposite = validation("float", "What is the opposite? ")
            hypotenuse = validation("float", "What is the hypotenuse? ")
            answer = math.degrees(math.sinh(opposite / hypotenuse))#InverseSine
        elif known[0] == True and known[2] == True and find == 2:
            interiorAngle = validation("float", "What is the interior angle? ")
            hypotenuse = validation("float", "What is the hypotenuse? ")
            answer = math.degrees(math.sin(interiorAngle) * hypotenuse)#Sine
        elif known[0] == True and known[1] == True and find == 3:
            interiorAngle = validation("float", "What is the interior angle? ")
            opposite = validation("float", "What is the opposite? ")
            answer = math.degrees(opposite / math.sin(interiorAngle))#Sine
        
        #Cosine
        elif known[3] == True and known[2] == True and find == 1:
            adjacent = validation("float", "What is the adjacent? ")
            hypotenuse = validation("float", "What is the hypotenuse? ")
            answer = math.degrees(math.cosh(adjacent / hypotenuse))#InverseCosine
        elif known[0] == True and known[3] == True and find == 3:
            interiorAngle = validation("float", "What is the interior angle? ")
            adjacent = validation("float", "What is the adjacent? ")
            answer = math.degrees(adjacent / math.cos(interiorAngle))#Cosine
        elif known[0] == True and known[2] == True and find == 4:
            interiorAngle = validation("float","What is the interior angle? ")
            hypotenuse = validation("float", "What is the hypotenuse? ")
            answer = math.degrees(hypotenuse * math.cos(interiorAngle))#Cosine

        #Pythagoras
        elif known[0] == True and known[1] == True and find == 4:
            otherlength = validation("float","What is the other length? ")
            hypotenuse = validation("float", "What is the hypotenuse? ")
            answer = math.sqrt((math.pow(hypotenuse, 2) - math.pow(otherlength, 2)))
        elif known[2] == True and known[3] == True and find == 2:
            hypotenuse = validation("float", "What is the hypotenuse? ")
            adjacent = validation("float", "What is the adjacent? ")
            answer = math.sqrt((math.pow(adjacent, 2) - math.pow(hypotenuse, 2)))
        elif known[0] == True and known[1] == True and find == 3:
            otherlengthone = validation("float", "Please enter one of the other lengths: ")
            otherlengthtwo = validation("float","Please enter the other length: ")
            answer = math.sqrt((math.pow(otherlengthone, 2) + math.pow(otherlengthtwo, 2)))

        print("The missing side is", answer)
        roundamount = validation("int", "How many decimal places do you want to round the answer to? ")
        print("The missing side is", round(roundamount,answer))#rounds the answer

        repeat = validation("str", "Do you wish to continue?(yes/no) ")#Ends loop