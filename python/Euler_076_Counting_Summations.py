import time

if __name__ == "__main__":
    st = time.clock()

    LIMIT = 5
    possible_ways = [1] + [0] * LIMIT

    for n in range(1, LIMIT):
        for i in range(n, LIMIT + 1):
            possible_ways[i] += possible_ways[i-n]

    print(possible_ways)
    print("Runtime is", time.clock()-st)
