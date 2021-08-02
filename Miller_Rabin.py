import math
import random


def get_r(n: int):
    s = 1
    r = 0

    while r % 2 == 0:
        r = int((n - 1) / (2 ** s))
        s += 1

    return r, s


def decimal_to_bin(n: int):
    binary = list()

    while n != 0:
        binary.append(n % 2)
        n = math.floor(n / 2)

    return binary


def calculate_mod(a: int, k: int, n: int):
    b = 1
    if k == 0:
        return b

    A = a
    k = decimal_to_bin(k)

    if k[0] == 1:
        b = a

    for i in range(1, len(k)):
        A = (A ** 2) % n
        if k[i] == 1:
            b = (A * b) % n

    return b


def miller_rabin(n: int, t: int):
    k, s = get_r(n)
    for i in range(1, t):
        a = random.randint(2, n - 2)
        y = calculate_mod(a, k, n)
        if y != 1 and y != (n - 1):
            j = 1
            while j <= s - 1 and y != (n - 1):
                y = (y ** 2) % n
                if y == 1: return "Hop so"
                j += 1

            if y != n - 1: return "Hop so"

    return "Nguyen to"


print(miller_rabin(380245276802753, 1000))
