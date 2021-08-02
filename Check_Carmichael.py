import math


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


print(is_carmichael(561))
