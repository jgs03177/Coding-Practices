# Upsolving based on the editorial.
# https://codeforces.com/blog/entry/110901


def inv(x, mod):
    return pow(x, mod - 2, mod)


def preprocess(n, mod):
    fact = [1]
    c = 1
    for i in range(1, n + 1):  # 1 ... n
        c = c * i % mod
        fact += [c]

    ic = inv(c, mod)
    ifact = [ic]
    for i in range(n, 0, -1):  # n ... 1
        ic = ic * i % mod
        ifact += [ic]
    ifact = ifact[::-1]
    return fact, ifact


def main():
    n, M = map(int, input().split())
    fact, ifact = preprocess(3 * n, M)

    def ncr(n, r, mod):
        # assume 0<=r<=n
        return fact[n] * ifact[r] * ifact[n - r] % mod

    """
    Let sorted array: [a1, a2; b1, b2; c1, c2]
                       ------  ------  ------
                       A side  B side  C side
    
    0 -> already sorted (1 case)
    
    <=1 -> a and b are mixed, c is sorted + b and c are mixed, a is sorted - both case
    (2n)! + (2n)! - n! cases
    
    <=2 -> no c is on A side + no a is on C side - both case
    (2n)Cn * n! * (2n)! + (2n)Cn * n! * (2n)! - X
    X = sum_(i=0...n) S_i
    S_i = (no a is on C side, no c in A side, i a is on A side)
        = nCi * nC(n-i) * (2n-i)Cn * n!**3
    Explanation:                                    e.g.
    First, place a's on A:              nCi cases.  [_aaa_a;      ;      ]
    Second, place a's on B:         nC(n-i) cases.  [ aaa a;__aa__;      ]
    Finally, place c's on B or C:  (2n-i)Cn cases.  [ aaa a;_caac_;c__ccc]
    The remaining positions are automatically b's.  [baaaba;bcaacb;cbbccc]
    Permutation of each cases: n!**3
    
    <=3 -> any (3n)!
    """

    o0 = 1
    o1 = (2 * fact[2 * n] - fact[n]) % M
    X = 0
    for i in range(n + 1):
        X = (X + ncr(n, n - i, M) * ncr(n, i, M) * ncr(2 * n - i, n, M)) % M
    X = X * fact[n] ** 3 % M
    o2 = (2 * ncr(2 * n, n, M) * fact[n] * fact[2 * n] - X) % M
    o3 = fact[3 * n]

    o = ((o3 - o2) * 3 + (o2 - o1) * 2 + (o1 - o0) * 1) % M
    print(o)


if __name__ == "__main__":
    main()
