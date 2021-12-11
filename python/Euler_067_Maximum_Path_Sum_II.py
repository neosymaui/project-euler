import time
import os
import sys


if __name__ == "__main__":
    start = time.clock()

    triangle = []
    with open("Euler_067_triangle.txt", "r") as t:
        for line in t.readlines():
            triangle.append([int(number) for number in line[:-1].split(' ')])
        t.close()

    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i - 1][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

    print("Result", max(triangle[-1]))
    print("{0} executed in {1}".format(os.path.basename(sys.argv[0]), time.clock() - start))

