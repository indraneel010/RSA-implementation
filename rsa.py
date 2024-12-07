import random

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(e, phi):
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        else:
            gcd, x, y = extended_gcd(b % a, a)
            return gcd, y - (b // a) * x, x

    gcd, x, y = extended_gcd(e, phi)
    if gcd != 1:
        return None
    else:
        return x % phi

def generate_keys():
    with open('primes.txt', 'r') as f:
        primes = [int(line.strip()) for line in f.readlines()]

    p = random.choice(primes)
    q = random.choice(primes)
    while q == p:
        q = random.choice(primes)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randint(2, phi)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi)

    d = multiplicative_inverse(e, phi)

    return ((e, n), (d, n))

def encrypt(message, public_key):
    e, n = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

def decrypt(encrypted_message, private_key):
    d, n = private_key
    decrypted_message = [chr(pow(char, d, n)) for char in encrypted_message]
    return ''.join(decrypted_message)

public_key, private_key = generate_keys()
print("Public Key:", public_key)
print("Private Key:", private_key)

message = "Hello, World!"
encrypted_message = encrypt(message, public_key)
print("Encrypted Message:", encrypted_message)

decrypted_message = decrypt(encrypted_message, private_key)
print("Decrypted Message:", decrypted_message)

