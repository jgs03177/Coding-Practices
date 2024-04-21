def pwrmod(a, b, p):
    # b positive integer
    o = 1
    a = a % p
    mul = a
    while b > 0:
        if b % 2:
            o = mul * o % p
        b >>= 1
        mul = mul * mul % p
    return o


def miller_rabin(n):
    # n = d * 2^s + 1
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    a_list = [2, 7, 61]
    if n in a_list:
        return True
    for a in a_list:
        # ad = (a ** d) % n
        ad = pow(a, d, n)  # or use pwrmod
        if ad == 1 or ad == n - 1:
            continue  # not composite
        composite = True
        for _ in range(s - 1):
            ad = (ad * ad) % n
            if ad == n - 1:
                composite = False  # not composite
                break
        if composite:
            return False
    return True
