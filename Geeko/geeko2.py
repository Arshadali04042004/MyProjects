import webbrowser
import time

# links for the meetings----
Chem = "https://meet.google.com/qde-eydm-drm"   # 12:00 - 12:45
Physics= "https://meet.google.com/sdn-varx-hec" # 11:00 - 11:45
Maths = "https://meet.google.com/nod-dzqs-oud"  #8:00 - 8:45
CS = "https://meet.google.com/eqv-edpa-fou"     # 9:00 - 9:45
english = "https://meet.google.com/zcy-ojoo-gfj"

userkeyMaths = ["maths", "mathematics", "m", "M", "Maths"]
userkeyPhysivs = ["physics", "Physics", "P", "p"]
userkeyChem = ["chem", "chemistry", "C", "c"]
userkeyCS = ["CS", "Computer", "Cs", "cs"]
userkeyEng = ["ENGLISH", "english", "eng", "e"]



while True:
    userInput = input("which subject to start Metting :")
    if userInput in userkeyMaths:
        webbrowser.open(Maths)
        time.sleep(5)
        print("Starting Maths class ...")
    elif userInput in userkeyPhysivs:
        webbrowser.open(Physics)
        print("Starting Physics class ...")
        time.sleep(5)
    elif userInput in userkeyEng:
        webbrowser.open(english)
        print("Starting English class ...")
        time.sleep(5)
    elif userInput in userkeyChem:
        webbrowser.open(Chem)
        print("Starting Chemistry class ...")
        time.sleep(5)
    elif userInput in userkeyCS:
        webbrowser.open(CS)
        print("Starting CS class ...")
        time.sleep(5)
    else:
        print("Error in keyword please type a correct keyword to start meeting...")
