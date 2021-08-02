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


def subtraction_multiprecision(a, b, w):
    a = list(reversed(a))
    b = list(reversed(b))

    epsilonSave = 0
    A = []

    for i in range(len(a)):
        total = a[i] - b[i] - epsilonSave
        modRes = total % (2 ** w)
        epsilonSave = 1 if total < 0 else 0
        A.append(modRes)

    A = list(reversed(A))

    return epsilonSave, A


def subtraction_fp(p, w, a, b):
    if isinstance(a, int) and isinstance(b, int):
        a = number_to_array(p, a, w)
        b = number_to_array(p, b, w)

    epsilon, c = subtraction_multiprecision(a, b, w)
    p_array = number_to_array(p, p, w)

    if epsilon == 1:
        epsilon, c = addition_multiprecision(c, p_array, w)
    return c


print(subtraction_fp(2147483647, 8, 38762497, 568424364))
