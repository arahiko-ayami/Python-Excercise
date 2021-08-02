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


a = number_to_array(2147483647, 38762497, 8)
b = number_to_array(2147483647, 568424364, 8)

print(subtraction_multiprecision(a, b, 8))
