import webbrowser
import pyautogui
import time
from time import  ctime
def automeet():
    time.sleep(60)
    pyautogui.click(x=1150,y=470) #1920 x 1080   # join now
    time.sleep(10)
    pyautogui.click(x=850,y=800)  # camaera turned off
    # time.sleep(10)
    # pyautogui.click(x=1400,y=100)  #chatbot opened
    # time.sleep(2)
    # pyautogui.typewrite("ArshadAli")
    # pyautogui.keyDown('enter')
    time.sleep(5)
    pyautogui.click(x=800,y=800)  #exit
Chem = "https://meet.google.com/qde-eydm-drm"   # 12:00 - 12:45
Physics= "https://meet.google.com/sdn-varx-hec" # 11:00 - 11:45
Maths = "https://meet.google.com/nod-dzqs-oud"  #8:00 - 8:45
CS = "https://meet.google.com/eqv-edpa-fou"     # 9:00 - 9:45
systemTime1 = ctime()
systemTime = systemTime1[12:20]
# For maths class
webbrowser.open(Maths)
automeet()
time.sleep(900)
# For cs class
webbrowser.open(CS)
automeet()
time.sleep(900)
# for english class 
# webbrowser.open(Eng)
# automeet()
# time.sleep(900)
# for physics class  
webbrowser.open(Physics)
automeet()
time.sleep(900)
#  for chemistry class  
webbrowser.open(Chem)
automeet()
time.sleep(900)


















