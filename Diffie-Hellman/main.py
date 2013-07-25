from random import getrandbits

def is_prime_calc(num):
    return all(num % i for i in xrange(2, num))

def is_prime(num):
    return is_prime_calc(num)

def getRandomPrime():
    while True:
        n = getrandbits(15) + 3;
        if is_prime(n):
            return n

bob_p = getRandomPrime()
print 'Bob random prime:   ' + str(bob_p)
alice_p = getRandomPrime()
print 'Alice random prime: ' + str(alice_p)


