# from https://github.com/cheran-senthil/PyRival/blob/master/pyrival/combinatorics/nCr_mod.py

def make_nCr_mod(max_n, mod):
    max_n = min(max_n, mod - 1)

    fact, inv_fact = [0] * (max_n + 1), [0] * (max_n + 1)
    fact[0] = 1
    for i in range(max_n):
        fact[i + 1] = fact[i] * (i + 1) % mod

    inv_fact[-1] = pow(fact[-1], mod - 2, mod)
    for i in reversed(range(max_n)):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod

    def nCr_mod(n, r):
        res = 1
        while n or r:
            a, b = n % mod, r % mod
            if a < b:
                return 0
            res = res * fact[a] % mod * inv_fact[b] % mod * inv_fact[a - b] % mod
            n //= mod
            r //= mod
        return res

    return nCr_mod


if __name__ == '__main__':
    mod = 998_244_353
    ncr_mod = make_nCr_mod(2_000_000, mod)

    n=3
    r=2
    c1 = ncr_mod(n,r)