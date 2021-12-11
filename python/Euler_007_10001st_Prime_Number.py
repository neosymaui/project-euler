import time
import os
import sys
from Euler import Euler_000_Utilities as Euler


if __name__ == "__main__":
    start = time.clock()
    print("Result", Euler.sieve_for_primes_to(105000)[10000])
    print("{0} executed in {1}".format(os.path.basename(sys.argv[0]), time.clock() - start))

