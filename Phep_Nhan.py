import math


def chuyenSoThanhMang(p: int, a: int, w: int):
    matrixA = []
    m = math.ceil(math.log(p, 2))
    t = math.ceil(m / w)
    for i in range(t - 1, -1, -1):
        tmp = pow(2, w * i)
        matrixA.append(math.floor(a / tmp))
        a = a % tmp
    return matrixA


def phepNhan(matrixA: list(), matrixB: list(), w: int):
    c = list()
    l = len(matrixA)
    a = matrixA.copy()
    b = matrixB.copy()

    a.reverse()
    b.reverse()

    for i in range(0, l * 2):
        c.append(0)

    for i in range(0, len(a)):
        u = 0
        for j in range(0, len(b)):
            temp = c[i + j] + a[i] * b[j] + u
            u = math.floor(temp / 256)
            c[i + j] = temp % 256
        c[i + l] = u

    c.reverse()

    return c


def main():
    p = 2147483647
    w = 8
    a = 524647
    b = 32549
    A = chuyenSoThanhMang(p, a, w)
    B = chuyenSoThanhMang(p, b, w)
    print(A)
    print(B)
    C = phepNhan(A, B, w)
    print(C)


if __name__ == "__main__":
    main()