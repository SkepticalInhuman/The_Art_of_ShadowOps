import sympy
import random

def generate_large_prime():
 
    lower_bound = 10**29  
    upper_bound = 10**30 - 1  

    prime = sympy.randprime(lower_bound, upper_bound)
    return prime

def is_primitive_root(alpha, p):
    phi = p - 1
    factors = sympy.primefactors(phi)
    for factor in factors:
        if pow(alpha, phi // factor, p) == 1:
            return False
    return True

def keys():
    global public, private
    p = generate_large_prime()
    alpha = random.randint(2, p-1)
    while not is_primitive_root(alpha, p):
        alpha = random.randint(2, p - 1)
    a = random.randint(0, p-1)
    beta = modular_exponentiation(alpha, a , p)
    public = (p, alpha, beta)
    private = a
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
    global public
    p, alpha, beta = public
    k = random.randint(1, p-2)
    gamma = modular_exponentiation(alpha, k, p)
    delta = (m*modular_exponentiation(beta, k, p))%p
    
    encrypted_text = (gamma, delta)
    #encrypted_text = (pow(g,m,N2)*pow(r,N,N2))%N2
    #print(encrypted_text)
    #print(g, r, m, N)
    return encrypted_text

def decrypt(enc):
    global private, public
    p, alpha, beta = public
    a = private
    gamma, delta = enc
    decrypted_text = (delta*modular_exponentiation(gamma, p-1-a, p))%p
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

def join_elements(list_of_lists):
    first_elements = [sublist[0] for sublist in list_of_lists]
    second_elements = [sublist[1] for sublist in list_of_lists]
    
    joined_first_elements = ''.join(map(str, first_elements))
    joined_second_elements = ''.join(map(str, second_elements))
    
    return joined_first_elements, joined_second_elements

if __name__ == '__main__':
    keys()
    message = input("Enter the message\n")
    coded = encoder(message)
 
    print("Initial message:")
    print(message)
    print("\n\nThe encoded message(encrypted by public key)\n")
    o1, o2 = join_elements(coded)
    print(f"({o1}, {o2})")
    print("\n\nThe decoded message(decrypted by public key)\n")
    print(''.join(str(p) for p in decoder(coded)))









