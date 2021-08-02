import math
import random


def get_r(n: int):
    s = 1
    r = 0

    while r % 2 == 0:
        r = int((n - 1) / (2 ** s))
        s += 1

    return r, s


def miller_rabin(n: int, t: int):
    if n == 2 or n == 3:
        return True

    k, s = get_r(n)
    for i in range(1, t):
        a = random.randint(2, n - 2)
        y = power(a, k, n)
        if y != 1 and y != (n - 1):
            j = 1
            while j <= s - 1 and y != (n - 1):
                y = (y ** 2) % n
                if y == 1: return False
                j += 1

            if y != n - 1: return False

    return True

def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if a % b == 0:
        return b
    return gcd(b, a % b)


def power(x, y, mod):
    if y == 0:
        return 1
    temp = power(x, math.floor(y / 2), mod) % mod
    temp = (temp * temp) % mod
    if y % 2 == 1:
        temp = (temp * x) % mod
    return temp


def is_carmichael(n):
    if n < 561:
        return False

    for i in range(2, n):
        if gcd(n, i) == 1:
            if power(i, n - 1, n) != 1:
                return False

    return True


def list_carmichael(n):
    if n < 561:
        return "Khong co Carmichael"

    carmichael_list = list()

    for i in range(561, n + 1):
        if not miller_rabin(i, 10) and is_carmichael(i):
            carmichael_list.append(i)

    return carmichael_list


print(list_carmichael(8911))
