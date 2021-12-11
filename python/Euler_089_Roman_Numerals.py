import time
import re


if __name__ == "__main__":
    st = time.clock()

    with open("Euler_089_roman.txt", "r") as m:
        rows = m.read()
    m.close

    print("count is", len(rows) - len(re.sub("DCCCC|LXXXX|VIIII|CCCC|XXXX|IIII", "rg", rows)))
    print("Runtime is", time.clock()-st)
