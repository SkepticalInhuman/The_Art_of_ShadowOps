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
# Week 1 Python & Cryptography Assignment 2
## Program1: GCD
Takes input 2 numbers and outputs GCD of those two numbers using two methods. First method involves finding numbers(in the range (1 to min(a,b)) that divide both the input numbers and thus finding the largest common divisor. Second method involves the euclidean approach where GCD(a,b) = GCD(b%a,a) formula is used. This formula is iteratively run till a = 0 and the corresponding b would be the GCD.
![Screenshot 2024-06-20 230634](https://github.com/SkepticalInhuman/Caesar_cipher/assets/96436121/903eb548-d0f9-4cc5-8d1a-a80f04f7c08b)
## Program2: Extended euclidean theorem
Takes input A,B,C,D and outputs a,b,c such that aA+bB+cC=D if there is a solution else outputs "NO solution". This is achieved through extended euclidean theorem. gcd(x,y,z)=gcd(x,gcd(y,z)). First we find a, b such that gcd(x,gcd(y,z))=ax+bgcd(y,z), then c, dsuch that gcd(y,z)=cy+dz. Finally we obtain gcd(x,y,z)=ax+bcy+bdz.
Now ax+by = GCD(a,b) 
gcd(a, b) = gcd(b%a, a)
gcd(b%a, a) = (b%a)x1 + ay1
ax + by = (b%a)x1 + ay1
ax + by = (b – [b/a] * a)x1 + ay1
ax + by = a(y1 – [b/a] * x1) + bx1
Comparing we get x=y1-(b//a)x1 and y = x1. 
Using gcd(x,y,z)=ax+bcy+bdz and x=y1-(b//a)x1 and y = x1 recursively, we are able to obtain the solution. If D is not divisible by GCD(A,B,C) then no solution exists.
![Screenshot 2024-06-20 230826](https://github.com/SkepticalInhuman/Caesar_cipher/assets/96436121/09ad65e5-ece1-4f99-a27f-e2ca3cd645ad)
## RSA
Takes input a string and outputs the encryptd and decrypted code. Two 100 digit primes are genrated using sympy module. The public and private keys are then generated using keys() function. The public key is chosen to be ten didgit number which is co prime[this is done using gcd_euclidean function from program 1] to (p-1)(q-1) where p, q are the large primes which were generated. The private key which is the multiplicative inverse of the public key mod (p-1)(q-1) is generated through the gcdExtended() function from program 2. Each character of the input message is converted to its ascii value and then individually encrypted and the the encrypted text is the join of all the encrypted characters.The message is encrypted using public key. modularexponentiation() function has been defined which calculates a^b mod n more efficiently by calculating mod after every time a is squared rather than calculating mod after a^b. The encrypted message is displayed. Each character of the encrypted message is then decrypted using private key and joined and finally the decrypted message is displayed.
Message is encrypted through message^public mod (p-1)(q-1) and decrypted through encrypted_text^private mod (p-1)(q-1)
![Screenshot (75)](https://github.com/SkepticalInhuman/Caesar_cipher/assets/96436121/0c34c3d9-1d8c-4a2b-ace6-b9f792dbed22)





