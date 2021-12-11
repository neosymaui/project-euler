import time
import os
import sys
from functools import reduce


if __name__ == "__main__":
    start = time.clock()

    limit = 100 + 1
    square = sum([i for i in range(1, limit)])
    result = square**2 - sum([i**2 for i in range(1, limit)])



    print("Result", result)
    print("{0} executed in {1}".format(os.path.basename(sys.argv[0]), time.clock() - start))

