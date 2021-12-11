import time
import numpy as np


def gen_prime_pyth_trips(limit=None):
    """ Barning way of generating Pythagorean triplets. """
    u = np.mat(' 1  2  2; -2 -1 -2; 2  2  3')
    a = np.mat(' 1  2  2;  2  1  2; 2  2  3')
    d = np.mat('-1 -2 -2;  2  1  2; 2  2  3')

    uad = np.array([u, a, d])
    m = np.array([3, 4, 5])

    while m.size:
        m = m.reshape(-1, 3)
        if limit:
            m = m[m[:, 2] <= limit]
        yield from m
        m = np.dot(m, uad)


def gen_all_pyth_trips(limit):
    for prim in gen_prime_pyth_trips(limit):
        i = prim
        for _ in range(limit//prim[2]):
            yield i
            i = i + prim

if __name__ == "__main__":
    LIMIT = 1500000
    Lengths = [0 for i in range(LIMIT)]

    st = time.clock()
    pyth_trips = list(gen_all_pyth_trips(10**6))

    for triplet in pyth_trips:
        length = triplet[0] + triplet[1] + triplet[2]
        if length < LIMIT:
            Lengths[triplet[0] + triplet[1] + triplet[2]] += 1

    counter = Lengths.count(1)

    print(Lengths)
    print(counter)
    print("Runtime is", time.clock()-st)
