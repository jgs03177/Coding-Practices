import sys

input = sys.stdin.readline

nt = int(input())
for t in range(nt):
    *d, = map(int, input().split())
    n = int(input())
    mem = set()
    o = 0
    for i in range(n):
        s = input().rstrip()
        v = 0
        for e in s:
            v *= 10
            v += d[ord(e) - ord('A')]
        o |= (v, len(s)) in mem
        mem.add((v, len(s)))
    y = 'YES' if o else 'NO'
    print(f"Case #{t + 1}: {y}")
