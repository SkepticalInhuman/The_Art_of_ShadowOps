def gcdExtended(a, b):
    
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = gcdExtended(b % a, a)

    
    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y

def main():
    
    A = int(input("Enter value for A: "))
    B = int(input("Enter value for B: "))
    C = int(input("Enter value for C: "))
    D = int(input("Enter value for D: "))

    gcd1, c, d = gcdExtended(B, C)
    gcd2, a, b = gcdExtended(A, gcd1)

    if D % gcd2 == 0:
        factor = D // gcd2
        print(f"Solution: a = {a * factor}, b = {b * c * factor}, c = {b * d * factor}")
    else:
        print("No solution")

if __name__ == "__main__":
    main()
