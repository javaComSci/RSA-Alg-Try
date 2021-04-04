import random
from math import gcd

def is_prime(n):
    if n == 2:
        return True
    for i in range(2,int(n/2) + 1):
        if n % i == 0:
            return False
    return True

def are_coprime(a, b):
    return gcd(a, b) == 1


def get_primes(low, high):
    primes = [i for i in range(low, high) if is_prime(i)]
    if len(primes) < 2:
        raise Exception("2 primes do not exist in this range " + low + " " + high) 
    p = random.choice(primes)
    q = p
    while q == p:
        q = random.choice(primes)
    return (p, q)


def calculate_n(p, q):
    return p*q


def calculate_totient(p, q):
    return (p-1)*(q-1)


def get_encryption_key(n, L):
    possible_e = []
    for i in range(2, L):
        if are_coprime(i, L) and are_coprime(i, n):
            possible_e.append(i)
    if len(possible_e) == 0:
        raise Exception("No possible encryption keys")
    return random.choice(possible_e)


def get_decryption_key(e, n, L):
    # must follow that d * e mod L = 1
    for i in range(1, n):
        if i != e and (i * e) % L == 1:
            return i


def do_encryption(m, e, n):
    # m^e % n
    c = (m**e) % n
    return c


def do_decryption(c, d, n):
    # c^d % n
    m = (c**d) % n
    return m


if __name__ == "__main__":
    (p, q) = get_primes(234, 4958)
    print("P:", p, "Q:", q)
    n = calculate_n(p, q)
    L = calculate_totient(p, q)
    e = get_encryption_key(n, L)
    d = get_decryption_key(e, n, L)

    c = do_encryption(23498, e, n)
    print(c)
    m = do_decryption(c, d, n)
    print(m)
    