from random import getrandbits
from random import randint
import sys

def is_prime_calc(num):
    return all(num % i for i in xrange(2, num))

def is_prime(num):
    return is_prime_calc(num)

def getRandomPrime():
    while True:
        n = getrandbits(12) + 3;
        if is_prime(n):
            return n

def primitiveRoot(modulo):
    requiredSet = set()
    requiredSet.update(range(1,modulo))
    for g in range(0, modulo):
        actualSet = set()
        for powers in range(1, modulo):
            actualSet.add(pow(g, powers) % modulo)
        if (requiredSet == actualSet):
            return g

# Generating private keys
alice_private = randint(999, 999999)
print 'Alice private key is %d' % alice_private
bob_private = randint(999, 999999)
print 'Bob private key is %d' % bob_private

# Generating p-g parameters
p = getRandomPrime()
g = primitiveRoot(p)

print '\n p parameter is %d, g parameter is %d \n' % (p, g)

# Generating public keys
alice_public = pow(g, alice_private) % p
bob_public = pow(g, bob_private) % p

print 'Alice public key is %d' % alice_public
print 'Bob public key is %d' % bob_public

alice_key = (pow(bob_public, alice_private)) % p
bob_key = (pow(alice_public, bob_private)) % p

print '\n Common secret: %d == %d' % (alice_key, bob_key)



#print multiplicativeOrder(2,15)
#print euler(7)
# print euler(67342)
# print getRandomPrime()
# print 'Bob random prime:   ' + str(bob_p)
# alice_p = getRandomPrime()
# print 'Alice random prime: ' + str(alice_p)


