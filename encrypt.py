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

# Main Driver for Encryption
# INPUT: Public key and original message as public_key.txt and message.txt
# OUTPUT: Encrypted ciphertext will be outputted to ciphertext.txt
def main():   

    f = open("public_key.txt")
    publicKey = f.readline().split(',')

    f = open("message.txt")
    message = int(f.readline())

    print('original message:')
    print(message)

    n = int(publicKey[0])
    e = int(publicKey[1])

    cipher = modExp(message, e, n)

    print('generated ciphertext:')
    print(cipher)
    
    f = open("ciphertext.txt", "w")
    f.write(str(cipher))

if __name__ == "__main__":
    main()

