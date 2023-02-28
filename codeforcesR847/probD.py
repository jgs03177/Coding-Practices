import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    *a, = map(int, input().split())
    a.sort()
    prve = 0
    ecount = 0
    l = []
    for e in a:
        if e == prve:
            ecount += 1
            continue
        if prve != 0:
            l += [(prve, ecount)]
        prve = e
        ecount = 1
    l += [(prve, ecount)]

    prve = 0
    prvecount = 0
    o = 0
    for e, ecount in l:
        if e == prve + 1:
            o -= min(prvecount, ecount)
        o += ecount
        prve = e
        prvecount = ecount
    print(o)
