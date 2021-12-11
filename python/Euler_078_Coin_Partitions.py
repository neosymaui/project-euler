import time

if __name__ == "__main__":
    st = time.clock()

    LIMIT = 60000
    DIVISOR = 1000000
    possible_ways = [1] + [0] * LIMIT

    for n in range(1, LIMIT):
        for i in range(n, LIMIT + 1):
            possible_ways[i] += possible_ways[i-n]

    for i in range(len(possible_ways)):
        if possible_ways[i] % DIVISOR == 0:
            print("Found n = {0} and p(n) = {1}".format(i, possible_ways[i]))

    print(possible_ways[-1])
    print("Runtime is", time.clock()-st)
