import random

def is_prime(n):
    if n == 2:
        return True
    for i in range(2,int(n/2) + 1):
        if n % i == 0:
            return False
    return True


def get_primes(low, high):
    primes = [i for i in range(low, high) if is_prime(i)]
    if len(primes) < 2:
        raise Exception("2 primes do not exist in this range " + low + " " + high) 
    p = random.choice(primes)
    q = p
    while q == p:
        q = random.choice(primes)
    return (p, q)


if __name__ == "__main__":
    (p, q) = get_primes(200, 700)
    print("P:", p, "Q:", q)