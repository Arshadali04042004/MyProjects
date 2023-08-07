import string
alphabets = list(string.ascii_letters)
numbers = list(string.digits)
UserInput = input("Enter the letter :")
if UserInput  in alphabets:
    print("It is a Alphabet.")
elif UserInput in numbers:
    print("It is a number")
else:
    print("it is a symbol")