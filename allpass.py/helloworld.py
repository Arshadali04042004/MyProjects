import string
from itertools import product
SmallLetter = string.ascii_lowercase
SmallLetter2 = string.ascii_lowercase
SmallLetter3 = string.ascii_lowercase
SmallLetter4 = string.ascii_lowercase
allposs = product(SmallLetter,SmallLetter2,SmallLetter3,SmallLetter4)
m = 1
with open("text.txt","w") as  filepath:
    for i in allposs:
        m+=1
        passw = ''.join(list(i))
        print(passw,"        ",(m/456976)*100 ,"%")
        filepath.write(str(m))
        filepath.write("-->  ")
        filepath.write(str(passw))
    
        filepath.write("\n")


