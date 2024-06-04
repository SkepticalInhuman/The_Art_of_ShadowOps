from caesarcipher import caesar

while (True) :
    encrypt = input("Enter 'e' for encryption or 'd' for decryption: ")
    mess = input("Enter the string: ")
    key = input("Enter caesar cipher key: ")
    
    if ((encrypt == 'e') or (encrypt == "E")):
        enc = True
        print(caesar(enc,mess,key))
    elif ((encrypt == 'd') or (encrypt == "D")):
        enc = False
        print(caesar(enc,mess,key))    
    else:
        print("Invalid input")
    break