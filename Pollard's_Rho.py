def pollard_rho(n):
    a = 2
    b = 2
    while True:
        a = (a ** 2 + 1) % n
        b = (b ** 2 + 1) % n
        b = (b ** 2 + 1) % n
        d = gcd(a - b, n)
        if 1 < d < n:
            return d
        if d == n:
            return False


def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


print(pollard_rho(43567127))
