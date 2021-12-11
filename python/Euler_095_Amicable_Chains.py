import time


def divisors_as_list(n):
    d = [1]

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            d.append(i)
            d.append(n // i)

    return d


if __name__ == "__main__":
    st = time.clock()

    longest = 10

    amicables = []
    amicable_starts = []
    excludes = []

    for i in range(1, 225):
        test = [i]
        temp = 0

        if i in excludes:
            print("We already processed", i, "in another chain without finding any amicable chain")

        while temp not in test[:-1] and temp != 1 and i not in excludes:
            temp = sum(divisors_as_list(test[-1]))
            # print("Appending", temp, "in", test)
            test.append(temp)

            if temp < test[0] and temp not in amicable_starts:
                print("Shortened research!")

            if temp == test[0] and len(test) > 2:
                print("Amicable chain found !", test)
                amicable_starts.append(test[0])
                break

        if temp == 1:
            excludes = excludes + test
        amicables.append(test)

    print("Excludes", excludes)
    for amicable in amicables:
        print(amicable)
    print("Runtime is", time.clock()-st)
