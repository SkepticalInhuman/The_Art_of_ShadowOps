# Caesar_cipher
## Program 1: Caesar Cipher with User Input
Program1 takes input string, key and option between encryption and decryption from the user. It then uses caesar() function from the caesarcipher.py file and outputs the encrypted or decrypted message.
![image](https://github.com/SkepticalInhuman/Caesar_cipher/assets/96436121/28a3e4b8-54b8-4d75-ad57-9a321b043681)
## Program 2: File-Based Caesar Cipher
Program 2 takes filename, key and option between encryption and decryption from the user and then outputs a output.txt file containing the encrypted or decrypted message. It works by importing caesar_file() function from caesarcipher_file.py.
![image](https://github.com/SkepticalInhuman/Caesar_cipher/assets/96436121/bb2906aa-e10e-4234-8bb0-0785239a3044)
![image](https://github.com/SkepticalInhuman/Caesar_cipher/assets/96436121/d5a99e4a-9619-42e6-807c-18c3eb3444ff)
![image](https://github.com/SkepticalInhuman/Caesar_cipher/assets/96436121/2439068e-29bc-4136-9222-b2b8b840668b)
![image](https://github.com/SkepticalInhuman/Caesar_cipher/assets/96436121/915685d8-131d-418c-ac09-909e20f650d3)

caesar() function iterates through the string and shifts each character by the value of the key. Lowercase letters is shifted to lowercase message similarly uppercase letters is shifted to uppercase letters only. Special characters are left the same.
caesar_file() function reads the text file and then uses caesar() function to encrypt or decrypt and writes the output in "output.txt" file.



