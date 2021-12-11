import time


if __name__ == "__main__":
    st = time.clock()

    # Each value is the list of all the digits located 'after' the corresponding key in the passcode.
    ranks_before = {
        "0": [],
        "1": [],
        "2": [],
        "3": [],
        "4": [],
        "5": [],
        "6": [],
        "7": [],
        "8": [],
        "9": []
    }

    appeared_chars = []

    with open("Euler_079_keylog.txt", "r") as key_log:
        # We retrieve the lines of the key log.
        for random_chars in key_log.readlines():
            for i in range(len(random_chars)-1):
                if random_chars[i] not in appeared_chars:
                    appeared_chars.append(random_chars[i])

            if random_chars[1] not in ranks_before[random_chars[0]]:
                ranks_before[random_chars[0]].append(random_chars[1])

            if random_chars[2] not in ranks_before[random_chars[0]]:
                ranks_before[random_chars[0]].append(random_chars[2])

            if random_chars[2] not in ranks_before[random_chars[1]]:
                ranks_before[random_chars[1]].append(random_chars[2])

    key_log.close()

    password = [""] * len(appeared_chars)
    for char in appeared_chars:
        print(char, " -> ", len(appeared_chars) - len(ranks_before[char]), " -> ", ranks_before[char])
        password[len(appeared_chars) - len(ranks_before[char]) - 1] = char

    print("Euler 079 ->", "".join(password))
    print("Runtime is", time.clock()-st)
