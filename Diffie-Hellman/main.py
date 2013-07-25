from random import getrandbits
from random import randint
import sys

def is_prime_calc(num):
    return all(num % i for i in xrange(2, num))

def is_prime(num):
    return is_prime_calc(num)

def get_random_prime():
    while True:
        n = getrandbits(12) + 3;
        if is_prime(n):
            return n

def gcd(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def primitive_root(modulo):
    required_set = set()
    for num in range (1, modulo):
        if (gcd(num, modulo) == 1):
            required_set.add(num)
    for g in range(1, modulo):
        actual_set = set()
        for powers in range(1, modulo):
            actual_set.add(pow(g, powers) % modulo)
        if required_set == actual_set:
            return g

# Generating private keys
alice_private = randint(999, 999999)
print 'Alice private key is %d' % alice_private
bob_private = randint(999, 999999)
print 'Bob private key is %d' % bob_private

# Generating p-g parameters
p = get_random_prime()
g = primitive_root(p)

print '\n p parameter is %d, g parameter is %d \n' % (p, g)

# Generating public keys
alice_public = pow(g, alice_private) % p
bob_public = pow(g, bob_private) % p

print 'Alice public key is %d' % alice_public
print 'Bob public key is %d' % bob_public

alice_key = (pow(bob_public, alice_private)) % p
bob_key = (pow(alice_public, bob_private)) % p

print '\n Common secret: %d == %d' % (alice_key, bob_key)

