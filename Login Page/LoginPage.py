userNameList = ["arshad"]
userPasswordList = ["04042004"]
print("WELLCOME TO YOUNG SCIENTISTS")
print("Login or Signup")
userResponse = input()
userResponse.lower()
def signup():
    if userResponse == "signup":
        userName2 = input("Enter the USERNAME :")
        userNameList.append(userName2)
        userPassword2 = input("Enter the password:")
        userPasswordList.append(userPassword2)
while True:
    if userResponse == "login":
        userName = input("Enter the USERNAME :")
        if userName not in userNameList:
            print("")
        if userName in userNameList:
            userPassword = input("Enter the USER PASSWORD :")
            if userPassword in userPasswordList:
                print("YOUR`S WELLCOME")
            else:
                print("Incorrect Password")
                
    
    
    
    
    

 