import time
# import itertools
# import functools


def product_sum(p, s, c, start):
    k = p - s + c
    if k < k_max:
        if p < n[k]:
            n[k] = p

        for i in range(start, k_max // p * 2 + 1):
            product_sum(p * i, s + i, c + 1, i)

if __name__ == "__main__":
    st = time.clock()

    k_max = 12000
    n = [2 * k_max] * k_max
    product_sum(1, 1, 1, 2)
    print("Result = ", sum(set(n[2:])))

    # limit = 12
    # result = []
    #
    # for k in range(2, limit + 1):
    #     min_product_sum_number = 0
    #     for sequence in itertools.combinations_with_replacement(range(1, k+1), k):
    #         l = list(sequence)
    #
    #         # We check whether the current list is a product-sum number.
    #         sum_l = sum(l)
    #         if sum_l == functools.reduce(lambda x, y: x*y, l):
    #             # print("Product-sum number found ->", l, sum_l)
    #             if min_product_sum_number == 0 or sum_l < min_product_sum_number:
    #                 min_product_sum_number = sum_l
    #
    #     print("Minimum Product-sum number for k=", k, "found ->", min_product_sum_number)
    #     if min_product_sum_number not in result:
    #         result.append(min_product_sum_number)
    #
    # print("Sum of non-repetitive minimum product-sum numbers:", sum(result))
    print("Runtime is", time.clock()-st)
