import pickle as plk
dict1 = {}
    
def learn_mode():
    print("------------learn mode------------")
    with open('file1.pickle','ab') as filepath:
        while True:
            A = input("Enter the question: ")
            if A =="exit" :
                break
            
            B = input("Enter the answer: ")
            dict1.update({A:B})
            plk.dump(dict1,filepath)
        
        
        
        
def ask_mode():
    print("------------ask mode-------------")
    with open('file1.pickle','rb') as filepath1:
        dict2 = plk.load(filepath1)
        print(dict2)
        filepath1.close()
        while True:
            userAsk = input("You : " )
            if userAsk=="exit":
                break
            print("Bot :",dict2[userAsk])
    
while True:
    learn_mode()
    ask_mode()
    learn_mode()
        
        



