dict2 = {"1":"a", "2":"b", "3":"c", "4":"d", "5":"e", "6":"f", "7":"g", "8":"h", "9":"i", "10":"j",
"11":"k", "12":"l", "13":"m", "14":"n", "15":"o", "16":"p", "17":"q", "18":"r", "19":"s", "20":"t",
"21":"u", "22":"v", "23":"w", "24":"x", "25":"y", "26":"z", "27":" "}
list1 = []
text = input("Enter the Encrypted Text:")
text_split = text.split("-")
text_split.pop(0)
for item in text_split:
    if item in dict2:
        a = str(dict2[item])
        list1.append(a)
decry = ''.join(list1)
print(decry)