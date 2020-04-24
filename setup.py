from random import randrange
from random import randint

# Source: Book Excercise 23b page 108
# INPUT: y,x,n such that y^x mod n
# OUTPUT z such that z = y^x mod n
def modExp(y,x,n):    
    a = x
    b = 1
    c = y

    while a != 0:
        if (a % 2 == 0):
            a = a//2
            c = c * c % n
        else:
            a = a -1
            b = b * c % n
    
    return b

# Source: https://www.geeksforgeeks.org/python-program-for-basic-and-extended-euclidean-algorithms-2/
# INPUT: a,b such that ax + by = 1
# OUTPUT: GCD(a,b), x, y such that ax + by = 1
def extEuclid(a, b):
    # Base case for recursive calls
    if a == 0:
        return b,0,1

    # Keep adding to recursive stack until base case is reached
    gcd, x1, y1 = extEuclid(b%a, a)

    # Update x and y from recursive calls
    x = y1 - (b//a) * x1
    y = x1
    
    return gcd,x,y

# Fermat's algorithm
# INPUT: Some number to check to see if prime
# OUTPUT: Boolean of primality
def primeCheck(n):
    a = randint(2, n-2)
    return modExp(a, n-1, n) == 1

# Generates a random number with 'n' digits
# INPUT: n such that n = # digits
# OUTPUT: Random number of 'n' digits
def randomByDigits(n):
    return randint(10**(n-1), (10**n)-1)

# Generates a public key and private key given project specifications
# OUTPUT: RSA public and private key
def genKeys():    
    # Generating p and q such that they are 95digits apart and > 100 digits
    p = randomByDigits(100)
    q = randomByDigits(195)

    while (not primeCheck(p)):    
        p = randomByDigits(100)
    
    while (not primeCheck(q)):
        q = randomByDigits(195)

    n = p * q    
    e = 2**16 + 1

    gcd,x,y = extEuclid(e, (p-1)*(q-1))

    if p - q < 10**95 and gcd == 1:
        gcd,x,y = extEuclid(e, (p-1)*(q-1))
        d = x % ((p-1)*(q-1))
    else:
        print("Something went wrong. Check variable configuration or run again.")
    
    print('public key:')
    print('n=', n, '\ne=', e)
    print('private key:')
    print('n=', n, '\nd=', d)
    return {'n': n,'e': e}, {'n': n, 'd': d}

# Main Driver for Key Setup
# INPUT: message.txt file
# OUTPUT: Keys will be written into public_key.txt and private_key.txt
def main():
    publicKey, privateKey = genKeys()

    f = open("public_key.txt", "w")
    f.write(str(publicKey['n']) + ',' + str(publicKey['e']))

    f = open("private_key.txt", "w")
    f.write(str(privateKey['n']) + ',' + str(privateKey['d']))

if __name__ == "__main__":
    main()