import time


def prime_gen(n):
    # Generate Primes less than the given "n"
    series = [True]*(n+1)
    series[0], series[1] = False, False
    for k in range(3, n+1, 2):
        series[k+1] = False
        for j in range(k**2, n+1, 2*k):
            series[j] = False
    return [var for var in range(0, len(series), 1) if series[var]]

if __name__ == "__main__":
    st = time.clock()

    LIMIT = 5000
    NUMBER_OF_PRIMES = 100
    target = 11
    primes = list(prime_gen(NUMBER_OF_PRIMES))

    while True:
        possible_ways = [1] + [0] * target

        for p in primes:
            for i in range(p, target + 1):
                possible_ways[i] += possible_ways[i - p]

        if possible_ways[target] > LIMIT:
            print("Target found is", target)
            break

        target += 1

    print(possible_ways)
    print("Runtime is", time.clock()-st)
