import string
import time
from itertools import product
allLatters = string.printable
allLatters2 = string.printable
allLatters3 = string.printable
allLatters4 = string.printable

com = product(allLatters,allLatters2,allLatters3,allLatters4)
m = 1
a = time.time()
with open("text.txt","w") as  filepath:
    for i in com:
        m+=1
        passw = ''.join(list(i))
        print(passw,"        ",m/1000000,"%")
        filepath.write(str(m))
        filepath.write("-->  ")
        filepath.write(str(passw))
    
        filepath.write("\n")
b = time.time()
print(b-a)