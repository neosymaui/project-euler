import time
import os
import sys
from Euler import Euler_000_Utilities as Euler


if __name__ == "__main__":
    start = time.clock()

    # Binomial coefficient, we need to choose 'n' amongst 'n+m'.
    n = 20
    m = 20
    print("The number of routes in a", n, "x", m, "grid are", Euler.fact(n+m) // Euler.fact(n) // Euler.fact(m))
    print("{0} executed in {1}".format(os.path.basename(sys.argv[0]), time.clock() - start))

