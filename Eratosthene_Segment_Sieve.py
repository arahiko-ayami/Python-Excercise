from math import floor, sqrt

prime = []


def simpleSieve(limit):
    danh_dau = [True for i in range(limit + 1)]
    p = 2
    while (p * p <= limit):
        if (danh_dau[p] == True):

            for i in range(p * p, limit + 1, p):
                danh_dau[i] = False
        p += 1

    for p in range(2, limit):
        if danh_dau[p]:
            prime.append(p)


def segmentedSieve(n):
    limit = int(floor(sqrt(n)) + 1)
    simpleSieve(limit)

    low = limit
    high = limit * 2

    while low < n:
        if high >= n:
            high = n

        danh_dau = [True for i in range(limit + 1)]

        for i in range(len(prime)):

            loLim = int(floor(low / prime[i]) * prime[i])
            if loLim < low:
                loLim += prime[i]

            for j in range(loLim, high, prime[i]):
                danh_dau[j - low] = False

        for i in range(low, high):
            if danh_dau[i - low]:
                prime.append(i)

        low = low + limit
        high = high + limit


n = 30
segmentedSieve(n)
[print(prime[i], end=' ') for i in range(len(prime))]
