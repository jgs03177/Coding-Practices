import math

n, a, b = map(int, input().split())

tnn = n * (n + 1) // 2
na = n // a
tna = a * na * (na + 1) // 2
nb = n // b
tnb = b * nb * (nb + 1) // 2
ab = a * b // math.gcd(a, b)
nab = n // ab
tnab = ab * nab * (nab + 1) // 2
o = tnn - tna - tnb + tnab
print(o)