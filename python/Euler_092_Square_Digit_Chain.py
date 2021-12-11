import time


def square_digit_chain_next(n):
    return sum([int(c)**2 for c in str(n)])


if __name__ == "__main__":
    st = time.clock()

    d = {}
    end_loop = [1, 89]

    for test in range(1, 10000000):
        chain = [test]
        while test not in end_loop:
            # We check whether we already found this number.
            if test in d.keys():
                d[chain[0]] = d[test]
                break

            test = square_digit_chain_next(test)
            chain.append(test)

        if test == 89:
            d[chain[0]] = 1
        elif test == 1:
            d[chain[0]] = 0

    print("Result", sum([v for v in d.values()]))
    print("Runtime is", time.clock()-st)
