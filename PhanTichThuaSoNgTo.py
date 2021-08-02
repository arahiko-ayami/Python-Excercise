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


def miller_rabin(n: int):
    t = 50
    k, s = get_r(n)
    for i in range(1, t):
        a = random.randint(2, n - 2)
        y = calculate_mod(a, k, n)
        if y != 1 and y != (n - 1):
            j = 1
            while j <= s - 1 and y != (n - 1):
                y = (y ** 2) % n
                if y == 1: return False
                j += 1

            if y != n - 1: return False

    return True


def pollard_rho(n: int, c=5):
    if n == 1:
        return 1
    if n % 2 == 0:
        return 2
    if n == 3:
        return 3
    if miller_rabin(n):
        return n

    a = random.randint(2, n)
    b = a
    while True:
        a = (a ** 2 + c) % n
        b = (b ** 2 + c) % n
        b = (b ** 2 + c) % n
        d = gcd(abs(a - b), n)

        if 1 < d < n and miller_rabin(d):
            return d
        if d == n:
            return pollard_rho(n, c - 1)


def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def find_factor(n):
    coSo = list()
    soMu = list()
    while n != 1:
        dem = 0
        i = pollard_rho(n)
        while n % i == 0 and i != 1:
            dem += 1
            n //= i
        if dem > 0:
            coSo.append(i)
            soMu.append(dem)
    return coSo, soMu

print(find_factor(380245276802753))
