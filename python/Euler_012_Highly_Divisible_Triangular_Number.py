import time
import os
import sys
from Euler import Euler_000_Utilities as Euler


if __name__ == "__main__":
    start = time.clock()

    triangle_number = 0

    for i in range(1, 100000):
        triangle_number += i
        if 2 * len(list(Euler.divisors(triangle_number))) > 500:
            print("Result", triangle_number)
            break

    print("{0} executed in {1}".format(os.path.basename(sys.argv[0]), time.clock() - start))

