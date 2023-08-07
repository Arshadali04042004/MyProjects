import pickle

print("________ Welcome To PasswordVault __________")
print("_____ Enter <help> to search function ______")
print("____________________________________________")

while True:
    passwordDict = {}
    loginUser = input("Enter the Login User id :")
    with open("user_info2.txt", "r") as filepath4:
        login = filepath4.read()
        loginId = login[:len(loginUser)]
        loginPass = login[len(loginUser):]
        

    if loginUser == "1":
        loginUsername = input("Enter the New User Name:")
        loginUserpassword = input("Enter the New password:")
        print()
        userInfo = loginUsername + loginUserpassword
        with open("user_info2.txt", "a") as filepath3:
            filepath3.write(userInfo)
            

        
    elif loginUser == loginId:

        logpass = input("Enter the password :")
        
        if logpass == loginPass:
            print("What you want to do :-")
            print("1.Save New password    2. View Your Password")
            aim = input(">>>")
            if "1" in aim:
                UserName = input("Enter the UserName :")
                UserPassword = input ("Enter the passWord :")
                passwordDict.update({UserName:UserPassword})
                with open("storPassword2.txt","wb") as filePassDict:
                    pickle.dump(passwordDict, filePassDict, protocol=2)   

                    
            
            elif "2" in aim:
                with open("storPassword2.txt", "rb") as filepath2:
                    passwordDict = pickle.load(filepath2)
                    acc = input("Enter the UserName :")
            
                if acc in passwordDict :
                    print("Your PassWord is  : ", passwordDict[acc] )
                else:
                    print("UserName does not match !")
            else:
                print("Please choose correct option !")
        else:
            print("Incorrect password!")
    
    elif loginUser == "<help>":
        print("1-Press 1 to create a new user")
        print("2-")
    else:
        print("Incorrect Username!")