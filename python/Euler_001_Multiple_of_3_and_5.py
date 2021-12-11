import time
import os
import sys


if __name__ == "__main__":
    start = time.clock()

    result = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            result += i

    print("Result", result)
    print("{0} executed in {1}".format(os.path.basename(sys.argv[0]), time.clock() - start))

