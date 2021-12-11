import time
import os
import sys


def fibonacci_even_numbers(n):
    """" Each third term is even. """
    x = y = 1
    current_sum = 0
    while current_sum < n:
        current_sum += (x + y)
        x, y = x + 2 * y, 2 * x + 3 * y
    return current_sum


if __name__ == "__main__":
    start = time.clock()
    result = fibonacci_even_numbers(4000000)
    print("Result", result)
    print("{0} executed in {1}".format(os.path.basename(sys.argv[0]), time.clock() - start))

