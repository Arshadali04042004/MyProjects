from cryptography.fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)

while True:
    user_input = input("Enter the Text:")
    inp = input("Enter E for 'Encrypt' OR D for 'Decrypt' :")
    inp2 = inp.upper()
    if inp2=="E":
        user_input_to_byte  = bytes(user_input,'utf-8')
        encrypting_text = f.encrypt(user_input_to_byte)
        print("Encrypted Text:",encrypting_text)
    elif inp2=="D":
        token = f.decrypt(encrypting_text)
        print("Decrypted Text:",token)
    else:
        print("Error Occured While Converting Text!")