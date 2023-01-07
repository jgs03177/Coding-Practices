# Upsolving prob F with editorial
# https://atcoder.jp/contests/abc284/editorial/5492

"""Editorial summary
e.g. s="abcde", i=2
t="abedcbacde"
"abedc" "bacde" (split half)
"abedc" "edcab" (reverse second half)
"abedc" "edcabedcab" (duplicate second half)
"""


# https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm
# KMP


def kmp_table(w):
    """Analyze KMP table of w.
    Input:
        w, the string to be analyzed.
    Output:
        t, list of positions (kmp table).
    """
    pos = 1  # cursor of t
    cnd = 0  # cursor of w
    t = [-1]

    while pos < len(w):
        if w[pos] == w[cnd]:
            t += [t[cnd]]
        else:
            t += [cnd]
            while cnd >= 0 and w[pos] != w[cnd]:
                cnd = t[cnd]
        pos += 1
        cnd += 1
    t += [cnd]
    return t


def kmp_search(s, w):
    """Find w in s.
    Input:
        s, the string to be searched.
        w, the string sought.
    Output:
        p, list of positions, where w is found.
    """
    t = kmp_table(w)
    j = 0  # cursor of s
    k = 0  # cursor of w
    p = []
    while j < len(s):
        if w[k] == s[j]:  # success
            j += 1
            k += 1
            if k == len(w):  # occurrence found
                p += [j - k]
                k = t[k]
        else:  # fail
            k = t[k]
            if k < 0:
                j += 1
                k += 1
    return p


# testing
# print(kmp_search("abababab","aba"))


n = int(input())
t = input().rstrip()

t0, t1 = t[:n], t[n:]
keyword = t0
base = t1[::-1] + t1[::-1]

ii = kmp_search(base, keyword)

if ii:
    i = n - ii[0]
    print(t[:i] + t[n + i:])
    print(i)
else:
    print(-1)
