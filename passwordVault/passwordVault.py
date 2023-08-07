import time
from win10toast import ToastNotifier
import pyperclip
import string
import random
import os
os.system('mode con: cols=50 lines=25')
os.system('color a')


# with open("./res/user_info.txt", "w") as qw:
#     pass
# Loading animation :----
# animation = ["LOADING :[■□□□□□□□□□]","LOADING :[■■□□□□□□□□]",
# "LOADING :[■■■□□□□□□□]", "LOADING :[■■■■□□□□□□]", "LOADING :[■■■■■□□□□□]", 
# "LOADING :[■■■■■■□□□□]", "LOADING :[■■■■■■■□□□]", "LOADING :[■■■■■■■■□□]", 
# "LOADING :[■■■■■■■■■□]", "LOADING :[■■■■■■■■■■]"]
# for i in range(len(animation)):
#     time.sleep(0.1)
#     sys.stdout.write("\r" + animation[i % len(animation)])
#     sys.stdout.flush()
# print("\n")
# Programe to password vault --
# print("___________________________________ Welcome To PasswordVault ___________________________"), time.sleep(0.1)
# print("______________________________ Enter <help> to search function ________________________"),time.sleep(0.1)
# # print("______Press 1 to create a new account_______")
# print("_______________________________________________________________________________________")

while True:

    loginUser = input("Enter the Login User id :")      # Input from user
    with open("./res/user_info.txt", "r") as filepath4:       # Open file in read mode to verify passwr
        login = filepath4.read()
        loginId = login[:len(loginUser)]
        loginPass = login[len(loginUser):]
    if loginUser == "1":
        loginUsername = input("Enter the New User Name:")
        loginUserpassword = input("Enter the New password:")
        print()
        userInfo = loginUsername + loginUserpassword
        with open("./res/user_info.txt", "w") as filepath3:
            filepath3.write(userInfo)
            ToastNotifier().show_toast("PasswordVault", f"New User {loginUsername} created.",
            duration =4 ,icon_path="./res/passwordvault.ico")
            print(">>> Login now")          
    elif loginUser == loginId:
        logpass = input("Enter the password :")
        print()
        if logpass == loginPass:
            print("What you want to do :-")
            print("1.Save New password    2.View Your Password")
            print("3.Password Generator   4.List All Password")
            print("Note : Enter only Option Number.")
            aim = input(">>>")
            if "1" in aim:
                UserName = input("Enter the UserName :")
                UserPassword = input ("Enter the passWord :")
                storing_info = UserName +"---"+ UserPassword
                with open(".//res/storPassword.txt", "a") as filepath:
                    filepath.write(storing_info)
                    filepath.write("\n")
                ToastNotifier().show_toast("PasswordVault", "Password Saved Successfully.",
                duration =4 ,icon_path="./res/passwordvault.ico") 
                print()
                            
            elif "2" in aim:
                ShowPass = input("Enter the UserName :")
                with open("./res/storPassword.txt", "r") as filepath2:
                    for reading_info in filepath2.readlines():
                        if ShowPass in reading_info:
                            getting_info = reading_info.split("---")
                            userID = getting_info[0]
                            userpass = getting_info[1]
                            if ShowPass == userID :
                                print("Your PassWord is   :",userpass)
                                ToastNotifier().show_toast("PasswordVault", "Password is copied to your clipboard !", 
                                duration = 4,icon_path="./res/passwordvault.ico") 
                                pyperclip.copy(userpass)
                    
                            else:
                                print(">>>UserName does not match !")

            # elif "3" in aim:
            #     remId = input("Enter the Username :")
            #     with open("./res/storPassword.txt","a+") as rempass:
            #         for removing_pass in rempass.readline():
            #             if remId in removing_pass:
            #                 rempass.truncate(remId)
                # print("Coming soon in next version 1.5")
            elif "4" in aim:
                with open("./res/storPassword.txt","r") as listPass:
                    for items in listPass.readlines():
                        print(items)
                    print()

            elif "3" in aim:
                plen = int(input("Enter the lenght of password:"))
                alphabets = list(string.printable)
                random.shuffle(alphabets)
                password = random.sample(alphabets,plen)
                geneted_pass = "".join(password)
                print(f"Your {plen} Digit Password :{geneted_pass}")
                # print("".join(password))
                pyperclip.copy(geneted_pass)
                ToastNotifier().show_toast("PasswordVault", "Password is copied to your clipboard !", 
                duration = 4,icon_path="./res/passwordvault.ico") 
                print()

            else:
                print(">>>Choose correct option !")    
        else:
            print(">>>Incorrect password !")
    elif loginUser == "<help>":
        print("1-Press 1 to create a new user")
        print("2-Password automatically copied to your clipboard.")
        print()
else:
    print("Incorrect Username!")
   
        

