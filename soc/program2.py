from caesarcipher_file import caesar_file

while(True):
    encrypt = input("Enter 'e' for encryption or 'd' for decryption: ")
    inp_file = input("Enter input filename: ")
    key = input("Enter caesar cipher key: ")
    out_file = "output.txt"
    if ((encrypt == 'e') or (encrypt == "E")):
        enc = True
        caesar_file(inp_file, out_file, key, enc)
        print("Text encrypted")
    elif ((encrypt == 'd') or (encrypt == "D")):
        enc = False
        caesar_file(inp_file, out_file, key, enc)  
        print("Text decrypted")  
    else:
        print("Invalid input")
    break