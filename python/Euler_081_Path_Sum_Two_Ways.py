import time


if __name__ == "__main__":
    st = time.clock()

    matrix = []

    with open("Euler_081_matrix.txt", "r") as m:
        for line in m.readlines():
            to_store = line[:-1].split(',')
            matrix.append([int(element) for element in to_store])
    m.close

    n, m = len(matrix), len(matrix[0])

    for i in range(n):
        for j in range(m):
            if i * j > 0:
                matrix[i][j] += min( matrix[i - 1][j], matrix[i][j - 1])
            elif i > 0:
                matrix[i][j] += matrix[i - 1][j]
            elif j > 0:
                matrix[i][j] += matrix[i][j - 1]

    print("Euler 081 -> ", matrix[-1][-1])
    print("Runtime is", time.clock()-st)
