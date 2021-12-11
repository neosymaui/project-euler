import time
import os
import sys
from Euler import Euler_000_Utilities as Euler


if __name__ == "__main__":
    start = time.clock()
    print("Result", sum([int(c) for c in str(Euler.fact(100))]))
    print("{0} executed in {1}".format(os.path.basename(sys.argv[0]), time.clock() - start))

