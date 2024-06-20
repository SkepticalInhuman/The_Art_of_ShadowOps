def gcd_on(a,b):
    gcd = 1
    for i in range(1, min(a,b) + 1):
        if (a%i == 0) and (b%i == 0):
            gcd = i
    return gcd

def gcd_euclidean(a,b):
    while (a != 0):
        a,b = b%a, a
    return b

def main():
    a = int(input("Enter first number :"))
    b = int(input("Enter second number :"))
    o_gcd = gcd_on(a,b)
    e_gcd = gcd_euclidean(a,b)

    print(f"GCD in O(N) = {o_gcd}")
    print(f"GCD using euclidean approach = {e_gcd}")

if __name__ == "__main__":
    main()