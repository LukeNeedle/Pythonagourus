# Imports libraries
import math

# Declare Variables
answer = None

# Functions
def round_function(roundamount:int, answer:float):
    """
    Validates the user's roundamount and then rounds the answer if it is valid.

    Args:
        roundamount (int): The amount to round by.
        answer (float): The value to round.

    Returns:
        float: The rounded value if roundamount is valid, otherwise it is the original answer.
    """
    if roundamount == 0 or roundamount > 20:
        print("You can't round to 0 or over 20")
    else:
        answer = round(answer, roundamount)
    return answer

def validation(type:str,question:str):
    """
    Validates use input.

    Args:
        type (str): The type the value should be.
        question (str): The prompt to display to the user.

    Returns:
        *varies*: The validated response in the correct type that was asked for.
    """
    if type == "str":
        variable = input(question)
        if variable.isdigit():
            variable = validation(type, question)
        elif variable == "" or variable == " ":
            variable = validation(type, question)
            
        
        return str(variable).lower()

    elif type == "int":
        variable = input(question)
        if not variable.isdigit():
            variable = validation(type, question)
        elif variable == "" or variable == " ":
            variable = validation(type, question)
            
        return int(variable)
    
    elif type == "bool":
        variable = input(question)
        if variable.isdigit():
            variable = validation(type, question)
        elif variable == "" or variable == " ":
            variable = validation(type, question)
        
        if variable == "True" or variable == "true" or variable == True:
            return True
        else:
            return False

    elif type == "float":
        variable = input(question)
        if not variable.isdigit():
            variable = validation(type, question)
        elif variable == "" or variable == " ":
            variable = validation(type, question)
            
        return float(variable)

def Start_Screen():
    """
    Asks the user what they want to find and what values that they know.

    Returns:
        int: The integer value that corresponds to the thing that the user wants to find.
        bool: List of Boolean values.
    """
    print("=============================")
    print("|| 1: The Interior angle   ||")
    print("|| 2: The Opposite side    ||")
    print("|| 3: The Hypotenuse       ||")
    print("|| 4: The Adjacent side    ||")
    print("=============================")
    
    toFind = validation("int","What do you want to find? ")

    known = [None, None, None, None]
    known[0] = validation("bool","Do you know the interior angle?(True or False) ")
    known[1] = validation("bool","Do you know the opposite side?(True or False) ")
    known[2] = validation("bool","Do you know the Hypotenuse?(True or False) ")
    known[3] = validation("bool","Do you know the adjacent side?(True or False) ")

    return toFind, known

# Main Program
print("Welcome to Pythonagorus")

while True:
    """
    Calculates the side/angle.
    """
    toFind, known = Start_Screen()

    if toFind == 1 and known[0]:
        pass
    elif toFind == 2 and known[1]:
        pass
    elif toFind == 3 and known[2]:
        pass
    elif toFind == 4 and known[3]:
        pass
    else:
        if known[0]:
            interiorAngle = validation("float", "What is the interior angle? ")
        if known[1]:
            opposite = validation("float", "What is the opposite? ")
        if known[2]:
            hypotenuse = validation("float", "What is the hypotenuse? ")
        if known[3]:
            adjacent = validation("float", "What is the adjacent? ")
        
        #Tan
        if known[1] and known[3] and toFind == 1: # Find Interior Angle
            answer = math.degrees(math.atan(opposite / adjacent))
        
        elif known[0] and known[3] and toFind == 2: # Find Opposite Side
            answer = math.degrees(math.tan(interiorAngle) * adjacent)
        
        elif known[0] and known[1] and toFind == 4: # Find Adjacent Side
            answer = math.degrees(opposite / math.tan(interiorAngle))
        
        #Sine
        elif known[1] and known[2] and toFind == 1: # Find Interior Angle
            answer = math.degrees(math.sinh(opposite / hypotenuse))
        elif known[0] and known[2] and toFind == 2: # Find Opposite Side
            answer = math.degrees(math.sin(interiorAngle) * hypotenuse)
        elif known[0] and known[1] and toFind == 3: # Find Hypotenuse
            answer = math.degrees(opposite / math.sin(interiorAngle))
        
        #Cosine
        elif known[3] and known[2] and toFind == 1: # Find Interior angle
            answer = math.degrees(math.cosh(adjacent / hypotenuse))
        elif known[0] and known[3] and toFind == 3: # Find Hypotenuse
            answer = math.degrees(adjacent / math.cos(interiorAngle))
        elif known[0] and known[2] and toFind == 4: # Find Adjacent Side
            answer = math.degrees(hypotenuse * math.cos(interiorAngle))

        #Pythagoras
        elif known[2] and known[1] and toFind == 4: # Find Adjacent Side
            answer = math.sqrt((math.pow(hypotenuse, 2) - math.pow(opposite, 2)))
        elif known[2] and known[3] and toFind == 2: # Find Opposite Side
            answer = math.sqrt((math.pow(adjacent, 2) - math.pow(hypotenuse, 2)))
        elif known[1] and known[3] and toFind == 3: # Find Hypotenuse
            answer = math.sqrt((math.pow(adjacent, 2) + math.pow(opposite, 2)))

        if answer != None:
            if known[0]:
                answerType = "side"
            else:
                answerType = "angle"
            print(f"The missing {answerType} is: {answer}")
            roundamount = validation("int", "How many decimal places do you want to round the answer to? ")
            print(f"The missing {answerType} is: {round_function(roundamount, answer)}")

    if not validation("bool", "Do you wish to continue?(True/False) "):
        break
