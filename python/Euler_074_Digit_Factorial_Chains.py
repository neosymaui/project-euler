import time

def fact(n):
    """ This function computes 'n!' """
    if n < 2:
        return 1
    else:
        return n * fact(n-1)


def convert_digits(n):
    """ This function converts an integer into a list of its digits. """
    length = len(str(n)) - 1
    digits = [0 for i in range(length + 1)]

    while n > 1:
        digits[length] = int(n % 10)
        n /= 10
        length -= 1

    return digits


def sum_fact_of_digits(n):
    converted = convert_digits(n)
    result = 0

    for digit in converted:
        result += fact(digit)

    return result

def loop_fact_of_digits(start):
    result = [start]
    loop_ended = False

    while loop_ended is False:
        # We compute the sum of the fact of digits, of the latest element in the
        # chain.
        to_add = sum_fact_of_digits(result[-1])

        if to_add in result:
            loop_ended = True
        else:
            result.append(to_add)

    return result


def print_chain(chain):
    to_be_printed = [str(element) for element in chain]
    print(to_be_printed[0] + " <=> {0} Items <=> ".format(len(to_be_printed)) + " -> ".join(to_be_printed))


if __name__ == "__main__":
    LIMIT = 1000000

    st = time.clock()

    count = 0
    for i in range(LIMIT):
        chain = loop_fact_of_digits(i)

        if len(chain) == 60:
            count += 1

        # print_chain(chain)

    print(count)
    print("Runtime is",time.clock()-st)
