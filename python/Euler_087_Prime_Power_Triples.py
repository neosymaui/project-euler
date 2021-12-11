import time
from itertools import product


def prime_gen(n):
    series = [True]*(n+1)
    series[0], series[1] = False, False
    for k in range(3, n+1, 2):
        series[k+1] = False
        for j in range(k**2, n+1, 2*k):
            series[j] = False
    return [var for var in range(0, len(series), 1) if series[var]]


if __name__ == "__main__":
    st = time.clock()

    P = set()
    LIMIT = 50000000

    for a, b, c in product(prime_gen(7072), prime_gen(370), prime_gen(86)):
        n = a**2 + b**3 + c**4
        if n <= LIMIT:
            P.add(n)

    print("Count is", len(P))
    print("Runtime is", time.clock()-st)
