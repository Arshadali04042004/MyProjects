def learn_mode():
    print("------------learn mode------------")
    with open('file1V2.txt','a') as filepath:
        while True:
            A = input("Enter the question: ")
            if A =="exit" :
                break
            
            B = input("Enter the answer: ")
            
            filepath.write(A+"-->"+B)
            filepath.write("\n")
        
        
        
        
def ask_mode():
    print("------------ask mode-------------")
    dict1 ={}
    with open('file1V2.txt','r') as filepath1:
       
        text=filepath1.readlines()
 #       print(text)
        for i in text:
            list1 = i.split("-->")
            A = list1[0]
            B = list1[1]
 #           print(A,B)
            dict1.update({A:B})
#        print(dict1)
       
        
        while True:
            userAsk = input("You : " )
            if userAsk=="exit":
                break
            if userAsk in dict1:
                print("Bot :",dict1[userAsk])
            else:
                print("Bot : No Info Found!")
                print()
    
while True:
    ask_mode()
    learn_mode()
    ask_mode()
        
        



