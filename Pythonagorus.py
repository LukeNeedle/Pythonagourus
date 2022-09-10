import math
import time
rept = "yes"
print("Welcome to Pythonagorus")
print("Press enter to continue")
input()
while rept == "yes":
    RAT=str(input("Does your triangle have a right angle? ")).lower()
    if RAT == "yes":
        TL=str(input("Do you know 2 of the sides? ")).lower()
        if TL == "yes":
            HpnLrept = "true"
            while HpnLrept == "true":
                HpnL=str(input("Do you know the Hypotenuse?(Side opposite the right angle) ")).lower()
                if HpnL == "yes":
                    OL=str(input("Do you know the other length? ")).lower()
                    if OL == "yes":
                        Hpn=int(input("What is the Hypotenuse? "))
                        SL=int(input("What is the other length? "))
                        Hpntwo = Hpn * Hpn
                        SLtwo = SL * SL
                        Take = Hpntwo - SLtwo
                        Answer = math.sqrt(Take)
                        print("The missing side is", Answer, "!")
                        HpnLrept = "false"
                    elif OL == "no":
                        HpnLrept = "true"
                elif HpnL == "no":
                    OLOne=int(input("Please enter one of the other lengths: "))
                    OLTwo=int(input("Please enter the other length: "))
                    OLOneTwo = OLOne * OLOne
                    OLTwoTwo = OLTwo * OLTwo
                    Add = OLOneTwo + OLTwoTwo
                    Answer = math.sqrt(Add)
                    print("The length of the Hypotenuse is", Answer, "!")
                    HpnLrept = "false"
        elif TL == "no":
            print("Sorry I can't help you")
    elif RAT == "no":
        print("Sorry I can't help you")
    rept=str(input("Do you wish to continue?(yes/no) ")).lower()
print("Pythonagorus has succesfully shut down.")
time.sleep(3)
exit()
