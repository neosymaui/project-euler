import time
import os
import sys


if __name__ == "__main__":
    start = time.clock()

    print("Result", sum([int(c) for c in str(2**1000)]))
    print("{0} executed in {1}".format(os.path.basename(sys.argv[0]), time.clock() - start))

