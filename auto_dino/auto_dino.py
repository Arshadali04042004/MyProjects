import pyautogui
from PIL import Image, ImageGrab
import time


# def hit(key):
#     pyautogui.keyDown(key)
#     return
# def isCollide(data):
#     for i in range(300, 415):
#         for j in range(410, 560):
#             if data[i, j]>100:
#                 hit('down')
#                 return
#     for i in range(300, 415):
#         for j in range(410, 560):
#             if data[i, j]<100:
#                 hit('up')
#                 return
#     return

# if __name__ == "__main__":
#     print("hey Dino game is about to start inm 3 seconds")
#     time.sleep(3)



#     while True:
#         image = ImageGrab.grab().convert('L')
#         data = image.load()
#         isCollide(data)


#         for i in range(355, 355):
#             for j in range(500, 550):
#                 data[i, j] = 0
#         for i in range(355, 355):
#             for j in range(500, 550):
#                 data[i, j] = 171


#         image.show()
#         break

def hit(key):
    pyautogui.press(key)
def screenshot():
    image = ImageGrab.grab().convert('L')
    return image
def iscollide(data):
    for i in range(570, 595):
        for j in range(215, 225):
            if data[i, j] <100:
               return True
    return False                

time.sleep(2)
while True:
    image = screenshot()
    data = image.load()
    if iscollide(data):
        hit('up')
    screenshot()

    for i in range(580, 615):
        for j in range(215, 235):
            data[i, j] = 0
    # for i in range(580, 615):
    #     for j in range(145, 160):
    #         data[i, j] = 171
    # image.show()
    # break