import math


def number_to_array(p, a, w):
    m = math.ceil(math.log2(p))
    t = math.ceil(m / w)
    A = []

    for i in reversed(range(1, t + 1)):
        deli = 2 ** ((i - 1) * w)
        bc = int(a / deli)
        A.append(bc)
        a = a - deli * bc

    return A


def addition_multiprecision(a, b, w):
    t = len(a)
    arr_c = []
    e = 0
    for i in range(t - 1, -1, -1):
        x = a[i] + b[i] + e
        e = 0 if x < (2 ** w) else 1
        arr_c.insert(0, x % (2 ** w))
    return e, arr_c


a = number_to_array(2147483647, 38762497, 8)
b = number_to_array(2147483647, 568424364, 8)

print(addition_multiprecision(a,b,8))