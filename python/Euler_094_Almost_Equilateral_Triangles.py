import time


if __name__ == "__main__":
    st = time.clock()

    side0, side, s, perimeters, m = 1, 1, 0, 0, 1

    limit = 10**9
    while perimeters <= limit:
        side0, side, m = side, 4 * side - side0 + 2*m, -m
        s += perimeters
        perimeters = 3 * side - m

    print("Result", s)
    print("Runtime is", time.clock()-st)
