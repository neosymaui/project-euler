import time
from math import gcd


if __name__ == "__main__":
    st = time.clock()

    limit = 50
    result = 0

    for x in range(1, limit+1):
        for y in range(1, limit):
            g = gcd(x, y)
            result += min(x * g // y, g * (limit - y) // x)

    final = result * 2 + limit * limit * 3
    print("Result", final)
    print("Runtime is", time.clock()-st)
