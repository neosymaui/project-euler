import time
import os
import sys


if __name__ == "__main__":
    start = time.clock()

    with open("Euler_022_Names_Scores.txt", "r") as t:
        for line in t.readlines():
            line = line.replace("\"", "")
            names = line.split(',')
        t.close()

    names.sort()
    scores = [0] * len(names)

    for i in range(len(names)):
        scores[i] = (i + 1) * sum([ord(c) - 64 for c in names[i]])

    print("Result", sum(scores))
    print("{0} executed in {1}".format(os.path.basename(sys.argv[0]), time.clock() - start))

