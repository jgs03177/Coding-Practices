import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    *a, = map(int, input().split())
    l = k - 2
    r = k
    o = False
    c = a[k - 1]
    changed = True
    while not o and changed:
        changed = False
        prvl = l
        maxc = c
        maxl = l
        while 0 <= l:
            if c + a[l] >= 0:
                c += a[l]
                l -= 1
                if c >= maxc:
                    maxc = c
                    maxl = l
            else:
                c = maxc
                l = maxl
                changed |= (l != prvl)
                break
        else:
            o = True
            break
        prvr = r
        maxc = c
        maxr = r
        while r < n:
            if c + a[r] >= 0:
                c += a[r]
                r += 1
                if c >= maxc:
                    maxc = c
                    maxr = r
            else:
                c = maxc
                r = maxr
                changed |= (r != prvr)
                break
        else:
            o = True
            break
    print("YES" if o else "NO")
