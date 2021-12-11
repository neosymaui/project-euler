import time
import os
import sys


def is_palindrome(n):
    p = str(n)
    return p == p[::-1]


if __name__ == "__main__":
    start = time.clock()

    limit = 1000
    result = 0

    for i in range(1, limit):
        for j in range(1, limit):
            temp = i*j
            if is_palindrome(temp) is True and temp > result:
                result = temp

    print("Result", result)
    print("{0} executed in {1}".format(os.path.basename(sys.argv[0]), time.clock() - start))

