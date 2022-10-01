import sys

input = sys.stdin.readline

mod = 998244353

n, x, y = map(int, input().split())
s = input().rstrip()
sb = [x if e == 'T' else y for e in s]


def powmod(a, b, p):
    o = 1
    m = a
    while b:
        if b & 1:
            o = o * m % p
        b >>= 1
        m = m * m % p
    return o


def inv(a, p):
    return powmod(a, p - 2, p)


def matmulmod(a, b, p):
    ## (a * b) mod p
    c = []
    for i in range(24):
        cc = []
        for j in range(24):
            # c[i][j] = sum([a[i][k]*b[k][j] for k in range(24)])
            cc += [sum([a[i][k] * b[k][j] for k in range(24)]) % p]
        c += [cc]
    return c


def matpowmod(a, b, p):
    ## (a ** b) mod p
    o = [[0] * 24 for _ in range(24)]  # identity o
    for i in range(24):
        o[i][i] = 1
    m = a
    while b:
        if b & 1:
            o = matmulmod(o, m, p)
        b >>= 1
        m = matmulmod(m, m, p)
    return o


inv100 = inv(100, mod)

# create a state transition graph: counter t, start from clock i, t increase at clock i+j+1.
transition = []  # A; p_t+1 = A * p_t, transition a[i][j]
for i in range(24):
    p, q = 0, 1
    l = [0] * 24
    for j in range(24):
        x = sb[(i + j) % 24]
        p, q = q * x * inv100 % mod, q * (100 - x) * inv100 % mod  # prob_t = q_0 * q_1 * ... * q_(t-1) * p_t
        l[(i + j + 1) % 24] = p
    qq = 1 - q  # qq = 1 - \prod_i q_i
    invqq = inv(qq, mod)
    l = [e * invqq % mod for e in l]
    transition += [l]


pn = matpowmod(transition, n, mod)[0]  # p_n; p_t = A^t p_0, where p_0=[1,0,...,0]
o = 0
for i in range(24):
    if s[i] == 'A':
        o = (o + pn[(i + 1) % 24]) % mod
print(o)
