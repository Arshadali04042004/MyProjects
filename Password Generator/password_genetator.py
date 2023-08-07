import string
import random
plen = int(input("Enter the lenght of password:"))
alphabets = list(string.printable)
random.shuffle(alphabets)
password = random.sample(alphabets,plen)
print("".join(password))