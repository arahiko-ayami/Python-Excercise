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


def compare_array(a, b):
    for i in range(len(a)):
        if a[i] > b[i]:
            return True
        elif a[i] < b[i]:
            return False
        else:
            if i == len(a) - 1:
                return True
            continue


def addition_fp(p, w, a, b):
    if isinstance(a, int) and isinstance(b, int):
        a = number_to_array(p, a, w)
        b = number_to_array(p, b, w)

    epsilon, c = addition_multiprecision(a, b, w)
    p_array = number_to_array(p, p, w)

    while (not (epsilon == 0 and compare_array(c, p_array) == False)):
        epsilon, c = subtraction_multiprecision(c, p_array, w)
    return c


print(addition_fp(2147483647, 8, 2147483646, 2147483643))
