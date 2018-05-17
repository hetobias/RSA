# Author: Tobias He
# RSA Algorithm Implementation

import random

# Generate two primes using Nth Prime Generator at https://primes.utm.edu/nthprime/index.php#random
p = 864967
q = 863539

# Euclid's algorithm for finding the greatest common divisor
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Euclid's Extended algorithm to find the multiplicative inverse
def euclidExtended(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi / e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi


def generate_publicKey(p, q):
    global n
    n = p * q

    global phi
    phi = (p - 1) * (q - 1)

    global e
    e = random.randrange(1, phi)

    global g
    g = gcd(e, phi)

    # Pick e such that 1 < e < phi , gcd(e, phi) = 1.
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    return (e,n)


def generate_privateKey(p, q):
    # Compute for d such that 1 < d < phi such that ed = 1 (mod phi)
    d = euclidExtended(e, phi)
    return(d,n)


def encrypt(pk, plaintext):
    key ,n = pk
    # Generate the numbers from the plaintext
    cipher = [pow(ord(char),key,n) for char in plaintext]
    # Return as number values
    return cipher


def decrypt(pk, ciphertext):
    key, n = pk
    # Generate the plaintext
    plain = [chr(pow(char, key, n)) for char in ciphertext]
    # Return as a string
    return "".join(plain)


def main():
    print "********************RSA********************"
    public = generate_publicKey(p, q)
    private = generate_privateKey(p, q)
    print "Your public key is  ", public, '\n', "Your private key is ", private, '\n'
    message = raw_input("Enter a message to encrypt with public key: ")
    print '\n'
    encrypted_message = encrypt(public, message)
    print "Your encrypted message is: "
    print " ".join(map(lambda x: str(x), encrypted_message))
    print "Decrypting message with private key ", private, '\n'
    print "Your message is: "
    print decrypt(private, encrypted_message)

main()