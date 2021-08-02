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


print(number_to_array(2147483647, 38762497, 8))
