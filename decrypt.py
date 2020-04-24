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

# Main Driver for Decryption
# INPUT: Private key and ciphertext as private_key.txt and ciphertext.txt
# OUTPUT: Decrypted message as decrypted_message.txt
def main():
    f = open("private_key.txt", "r")
    privateKey = f.readline().split(',')

    n = int(privateKey[0])
    d = int(privateKey[1])

    f = open("ciphertext.txt", "r")
    ciphertext = int(f.readline())

    print('ciphertext:')
    print(ciphertext)

    decrypted = modExp(ciphertext, d, n)

    print('decrypted:')
    print(decrypted)
    
    f = open("decrypted_message.txt", "w")
    f.write(str(decrypted))

if __name__ == "__main__":
    main()

