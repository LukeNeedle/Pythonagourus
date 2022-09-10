import math
import time

rept = "yes"
print("Welcome to Pythonagorus")
print("Press enter to continue")
input()

while rept == "yes":
    rat=str(input("Does your triangle have a right angle? ")).lower()
    if rat == "yes":
        tl=str(input("Do you know 2 of the sides? ")).lower()
        if tl == "yes":
            hpnlrept = "true"
            while hpnlrept == "true":
                hpnl=str(input("Do you know the Hypotenuse?(Side opposite the right angle) ")).lower()
                if hpnl == "yes":
                    ol=str(input("Do you know the other length? ")).lower()
                    if ol == "yes":
                        hpn=float(input("What is the Hypotenuse? "))
                        sl=float(input("What is the other length? "))
                        hpntwo = hpn * hpn
                        sltwo = sl * sl
                        take = hpntwo - sltwo
                        answer = math.sqrt(take)
                        print("The missing side is {0:.2f}".format(answer))
                        hpnlrept = "false"
                    elif ol == "no":
                        hpnlrept = "true"
                elif hpnl == "no":
                    olone=float(input("Please enter one of the other lengths: "))
                    oltwo=float(input("Please enter the other length: "))
                    olonetwo = olone * olone
                    oltwotwo = oltwo * oltwo
                    add = olonetwo + oltwotwo
                    answer = math.sqrt(add)
                    print("The missing side is {0:.2f}".format(answer))
                    hpnlrept = "false"
        elif tl == "no":
            print("Sorry I can't help you")
    elif rat == "no":
        print("Sorry I can't help you")
    rept=str(input("Do you wish to continue?(yes/no) ")).lower()
print("Pythonagorus has succesfully shut down.")
time.sleep(2)
exit()
