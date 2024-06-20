import sympy
from program1 import gcd_euclidean
from program2 import gcdExtended

def generate_100_digit_prime():
 
    lower_bound = 10**99  
    upper_bound = 10**100 - 1  

    prime = sympy.randprime(lower_bound, upper_bound)
    return prime

def keys():
    global public, private, N
    p = generate_100_digit_prime()
    q = generate_100_digit_prime()
    N = p*q
    b = (p-1)*(q-1)
    e = 10**10
    while True:
        if gcd_euclidean(e, b) == 1:
            public = e
            #print (e)
            gcd, x, d = gcdExtended(b, e)
            private = d
            #print(d)
            if d>0:
                break
        e += 1

def modular_exponentiation(a, b, n):

    result = 1
    base = a % n

    while b > 0:
        
        if b % 2 == 1:
            result = (result * base) % n

       
        base = (base * base) % n
        b //= 2

    return result

def encrypt(m):
    global public, N
    e = public
    encrypted_text = modular_exponentiation(m, e, N)
    #print(encrypted_text)
    return encrypted_text

def decrypt(enc):
    global private, N
    d = private
    decrypted_text = modular_exponentiation(enc, d, N)
    #print(decrypted_text)
    return decrypted_text

def encoder(message):
    encoded = []
    for letter in message:
        encoded.append(encrypt(ord(letter)))
    return encoded

def decoder(encoded):
    s = ''
    for num in encoded:
        s += chr(decrypt(num))
    return s

if __name__ == '__main__':
    keys()
    message = input("Enter the message\n")
    coded = encoder(message)
 
    print("Initial message:")
    print(message)
    print("\n\nThe encoded message(encrypted by public key)\n")
    print(''.join(str(p) for p in coded))
    print("\n\nThe decoded message(decrypted by public key)\n")
    print(''.join(str(p) for p in decoder(coded)))









