import sys

input = sys.stdin.readline

t = int(input())
for case in range(t):
    n = int(input())
    *a, = map(int, input().split())
    l1, r1, l2, r2 = map(int, input().split())
    c = 0
    pfa = [0]
    for e in a:
        c += e
        pfa += [c]
    l1 -= 1
    l2 -= 1
    r1 -= 1
    r2 -= 1
    o = 0
    if r1 < l2:  # l1<=r1<=i<l2<=r2
        i = (r1 + l2) // 2  # r1+l2 even -> give 0~i to alice
        # r1+l2 odd -> give 0~i to alice
        va = pfa[i + 1]
        vb = pfa[n] - pfa[i + 1]
        o = va
    elif r2 < l1:  # l2<=r2<i<=l1<=r1
        i = (r2 + l1 + 1) // 2  # r2+l1 even -> give i~n-1 to alice
        # r2+l1 odd -> give i~n-1 to alice
        va = pfa[n] - pfa[i]
        vb = pfa[i]
        o = va
    else:
        va = 0
        for i in range(l1, r1 + 1):  # inclusive
            candidate = []
            if l2 <= i - 1:  # l2 i r2
                vb = pfa[i]  # vb=sum(a[0:i])
                va = pfa[n] - pfa[i]
                candidate += [(vb, va)]
            if i + 1 <= r2:
                vb = pfa[n] - pfa[i + 1]
                va = pfa[i + 1]
                candidate += [(vb, va)]
            vb, va = max(candidate)
            o = max(o, va)
    print(f"Case #{case + 1}: {o}")
