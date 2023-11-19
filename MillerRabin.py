# D21125387 Advanced Security Assignment 2
import random


def test(n):
    # find integers k, q, with k > 0, q odd so that (n-1) = 2^k * q
    # k > 0
    k = 0
    # q odd
    q = n - 1
    while q % 2 == 0:
        k += 1
        q //= 2
    # pick a random integer a with 1 < a < n-1
    a = random.randint(2, n - 2)

    print("n = " + str(n))
    print("k = " + str(k))
    print("q = " + str(q))
    print("a = " + str(a))

    # if a^q mod n = 1, then n is probably prime
    if pow(a, q, n) == 1:
        return "inconclusive"

    # if a^(2^j * q) mod n = -1
    for j in range(0, k):
        if pow(a, (2 ^ j) * q, n) == n - 1:
            return "inconclusive"

    # otherwise, n is composite
    return "composite"


# inconclusive
print(test(347))

# composite
print(test(561))
