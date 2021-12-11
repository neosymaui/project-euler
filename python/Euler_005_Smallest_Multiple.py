import time
import os
import sys
from functools import reduce
from math import gcd


def least_common_multiplier(a, b):
    return a // gcd(a, b) * b


if __name__ == "__main__":
    start = time.clock()

    limit = 20
    result = reduce(least_common_multiplier, range(limit // 3, limit + 1))
    print("Result", result)
    print("{0} executed in {1}".format(os.path.basename(sys.argv[0]), time.clock() - start))

