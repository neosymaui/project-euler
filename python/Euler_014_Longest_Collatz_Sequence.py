import time
import os
import sys


def collatz_sequence(n):
    """ Generates the Collatz Sequence starting with 'n' """
    collatz = [n]

    while collatz[-1] != 1:
        if collatz[-1] % 2 == 0:
            collatz.append(collatz[-1] // 2)
        else:
            collatz.append(collatz[-1] * 3 + 1)

    return collatz


if __name__ == "__main__":
    start = time.clock()

    limit = 1000000
    maximum = 0
    start = 1

    for i in range(1, limit):
        temp = collatz_sequence(i)
        if len(temp) > maximum:
            start = i
            maximum = len(temp)

    print("The starting number", start, "produces a Collatz sequence of length", maximum)
    print("{0} executed in {1}".format(os.path.basename(sys.argv[0]), time.clock() - start))

