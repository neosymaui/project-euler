import time
import os
import sys
from Euler import Euler_000_Utilities as Euler


if __name__ == "__main__":
    start = time.clock()

    target = 1000
    pythagorean_triplet = dict()
    for r in range(2, 550, 2):
        st = r * r // 2
        for s, t in Euler.divisors(st):
            x = (r + s) + (r + t) + (r + s + t)
            pythagorean_triplet[x] = (r + s) * (r + t) * (r + s + t)

    print("Result", pythagorean_triplet[target])
    print("{0} executed in {1}".format(os.path.basename(sys.argv[0]), time.clock() - start))

