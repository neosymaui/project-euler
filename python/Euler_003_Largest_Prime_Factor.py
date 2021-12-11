import time
import os
import sys


def sieve(n):
    """" Return all primes <= n."""
    np1 = n + 1
    s = list(range(np1))
    s[1] = 0
    square_root = int(round(n**0.5))
    for i in range(2, square_root + 1):
        if s[i]:
            s[i*i: np1: i] = [0] * len(range(i*i, np1, i))
    return list(filter(None, s))


if __name__ == "__main__":
    start = time.clock()

    value = 600851475143
    result = 0

    for prime in sieve(10000):
        if value % prime == 0:
            value //= prime

            if value == 1:
                result = prime
                break

    print("Result", result)
    print("{0} executed in {1}".format(os.path.basename(sys.argv[0]), time.clock() - start))

