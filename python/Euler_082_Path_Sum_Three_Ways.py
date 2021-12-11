import time


if __name__ == "__main__":
    st = time.clock()

    matrix = []

    with open("Euler_082_matrix.txt", "r") as m:
        for line in m.readlines():
            to_store = line[:-1].split(',')
            matrix.append([int(element) for element in to_store])
    m.close

    n, m = len(matrix), len(matrix[0])

    sums = [matrix[i][-1] for i in range(n)]

    for i in range(m - 2, -1, -1):
        sums[0] += matrix[0][i]

        for j in range(1, n):
            sums[j] = min(sums[j], sums[j - 1]) + matrix[j][i]

        for j in range(n - 2, -1, -1):
            sums[j] = min(sums[j], sums[j + 1] + matrix[j][i])

    print("Euler 082 -> ", min(sums))
    print("Runtime is", time.clock()-st)
