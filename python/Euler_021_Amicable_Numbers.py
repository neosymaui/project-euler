import time
import os
import sys
from Euler import Euler_000_Utilities as Euler


if __name__ == "__main__":
    start = time.clock()

    amicable_sum = 0
    for i in range(1, 10000):
        d_i = sum(Euler.divisors_list(i))
        d_d_i = sum(Euler.divisors_list(d_i))

        if d_d_i == i and i != d_i:
            # Amicable numbers found.
            print("Amicable numbers found ->", i, "and", d_i)
            amicable_sum += i + d_i

    print("Result", amicable_sum // 2)
    print("{0} executed in {1}".format(os.path.basename(sys.argv[0]), time.clock() - start))

