import sympy
from program1 import gcd_euclidean
from program2 import gcdExtended
import random

def generate_large_prime():
 
    lower_bound = 10**7  
    upper_bound = 10**8 - 1  

    prime = sympy.randprime(lower_bound, upper_bound)
    return prime

def keys():
    global public, private, N
    p = generate_large_prime()
    q = generate_large_prime()
    N = p*q
    phi = (p-1)*(q-1)
    gcd, x, d = gcdExtended(N, phi)
    mu = d
    public = N+1
    private = (phi, mu)
    #print(public, private)


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
    g = public
    N2 = N*N
    while True:
        r = random.randint(0, N)
        if gcd_euclidean(r,N) == 1:
            break
    
    encrypted_text = modular_exponentiation(g, m, N2)
    encrypted_text *= modular_exponentiation(r, N, N2)
    encrypted_text = encrypted_text%(N2)
    #encrypted_text = (pow(g,m,N2)*pow(r,N,N2))%N2
    #print(encrypted_text)
    #print(g, r, m, N)
    return encrypted_text

def decrypt(enc):
    global private, N
    n = N
    phi = private[0]
    mu = private[1]
    d = modular_exponentiation(enc, phi, n**2)
    e = int((d-1)/n) 
    #print(phi, mu, d, e)
    decrypted_text = modular_exponentiation(e*mu, 1, n)
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









