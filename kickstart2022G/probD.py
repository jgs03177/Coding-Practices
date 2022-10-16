# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb2e1/0000000000c17b68
# Analysis, Test Set 1~2
import sys

input = sys.stdin.readline

ntc = int(input())
for t in range(ntc):
    n, ene = map(int, input().split())
    l = []
    xmax = 0
    for i in range(n):
        x, y, c = map(int, input().split())
        l += [(y, x, c)]
        xmax = max(xmax,x)
    l.sort(reverse=True)
    l += [(-1, 0, 0)]
    prvy = l[0][0]
    cs = [0] * (xmax + 1)
    rdp = [0] * (xmax + 1)
    ldp = [-ene] * (xmax + 1)
    for y, xx, cc in l:
        if y != prvy:
            prvy = y

            nrdp = [0] * (xmax + 1)
            nldp = [0] * (xmax + 1)
            nrdp[0] = max(rdp[0], ldp[0] - ene) + cs[0]
            for x in range(1, xmax + 1):
                nrdp[x] = max(nrdp[x - 1], rdp[x]) + cs[x]
            nldp[xmax] = max(ldp[xmax], rdp[xmax] - ene) + cs[xmax]
            for x in range(xmax - 1, -1, -1):
                nldp[x] = max(nldp[x + 1], ldp[x]) + cs[x]
            rdp = nrdp
            ldp = nldp

            cs = [0] * (xmax + 1)
        cs[xx] = cc
    o = max(rdp[xmax], ldp[0])

    print(f"Case #{t + 1}: {o}")
