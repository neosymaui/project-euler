import time


if __name__ == "__main__":
    st = time.clock()

    TARGET = 2000000
    LIMIT = 100

    nearest_x, nearest_y = 0, 0
    nearest_area = 0
    nearest_number = TARGET

    LIMIT_X = LIMIT
    LIMIT_Y = LIMIT

    for X in range(2, LIMIT_X):
        for Y in range(2, LIMIT_X):
            count = 0

            for x in range(X, 0, -1):
                for y in range(Y, 0, -1):
                    count += (Y - y + 1) * (X - x + 1)

            print(" Grid {0} x {1} -> {2} rectangles".format(X, Y, count))

            if abs(TARGET - count) < nearest_number:
                print(" Grid {0} x {1} -> {2} rectangles is the nearest !".format(X, Y, count))
                nearest_number = abs(TARGET - count)
                nearest_x = X
                nearest_y = Y
                nearest_area = X * Y

    print("{0}, {1} grid is the nearest, its area is {2} !".format(nearest_x, nearest_y, nearest_area))
    print("Runtime is", time.clock()-st)
