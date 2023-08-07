"""THE ENCRYPTOR AND DECRYTOR"""

dict1 = {"a":-1,"b":-2,"c":-3,"d":-4,"e":-5,"f":-6,"g":-7,"h":-8,"i":-9,"j":-10,
"k":-11,"l":-12,"m":-13,"n":-14,"o":-15,"p":-16,"q":-17,"r":-18,"s":-19,"t":-20,
"u":-21,"v":-22,"w":-23,"x":-24,"y":-25,"z":-26," ":-27, "A":-28, ".":-29, ",":-30}

dict2 = {"1":"a", "2":"b", "3":"c", "4":"d", "5":"e", "6":"f", "7":"g", "8":"h", "9":"i", "10":"j",
"11":"k", "12":"l", "13":"m", "14":"n", "15":"o", "16":"p", "17":"q", "18":"r", "19":"s", "20":"t",
"21":"u", "22":"v", "23":"w", "24":"x", "25":"y", "26":"z", "27":" ", "28":"A", "29":".", "30":","}

def encryptor():
    user = input("Enter the Text:")
    list1 = list(user)
    list2 = []
    for item in list1:
        if item in dict1:
            a = str(dict1[item])
            list2 .append(a)
    encry = ''.join(list2)
    print("Encrypted Text:",encry)

def decryptor(): 
    list1 = []
    text = input("Ebter the Encrypted Text:")
    text_split = text.split("-")
    text_split.pop(0)
    for item in text_split:
        if item in dict2:
            a = str(dict2[item])
            list1.append(a)
    decry = ''.join(list1)
    print(decry)
    
while True:
    encry_or_decry = input("Enter Encrypt or Decrypt: ").lower()
    if encry_or_decry == "e":
        encryptor()
    elif encry_or_decry == "d":
        decryptor()
    else:
        print("Enter valid choice.")
    








