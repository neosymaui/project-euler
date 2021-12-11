import time
from decimal import getcontext, Decimal


if __name__ == "__main__":
    st = time.clock()
    getcontext().prec = 104

    integer_power = [x**2 for x in range(11)]

    total_sum = 0

    for number in range(2, 101):
        current_sum = 0
        if number not in integer_power:
            dec = str(Decimal(number).sqrt())
            dot_offset = dec.find(".")

            for char in dec[:-4]:
                if char != ".":
                    current_sum += int(char)
                    total_sum += int(char)

            print(number, " -> ", dec, " -> ",  current_sum)

    print("total sum -> ", total_sum)
    print("Runtime is", time.clock()-st)
