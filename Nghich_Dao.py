def inverse(p, a):
    u = a
    v = p
    x1 = 1
    x2 = 0
    while u != 1:
        q = v//u
        r = v-q*u
        x = x2-q*x1
        v = u
        u = r
        x2 = x1
        x1 = x
    return x1 % p


print(inverse(489573857, 45682375))