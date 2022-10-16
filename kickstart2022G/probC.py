# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb2e1/0000000000c17491#analysis
# Analysis
import sys

input = sys.stdin.readline

ntc = int(input())
for t in range(ntc):
    n = int(input())
    *a, = map(int, input().split())
    b = [0]  # b[i]=sum(a[:i])
             # sum(a[i:j])=b[j]-b[i]
    current = 0
    for e in a:
        current += e
        b += [current]
    nsv = []  # nsv[i]=j where j is the nsv index of b.
              # i.e. smallest j>=i s.t. b[j]<b[i]
    q = []
    for i in range(n, -1, -1):
        e = b[i]
        while q and b[q[-1]] >= e:
            q.pop()
        nsv += [q[-1] if q else n + 1]
        q += [i]
    nsv = nsv[::-1]
    current = 0
    c = [0]  # c[i] = sum(b[:i])
             # sum(b[i:j])=c[j]-c[i]
    for e in b:
        current += e
        c += [current]
    o = 0
    for i in range(n):
        # for j in range(i+1,nsv[i]):
        #    o+=a[i:j]  # i.e. o+=b[j]-b[i]
        o -= b[i] * (nsv[i] - i - 1)
        o += c[nsv[i]]-c[i+1]  # o+=b[i+1:nsv[i]]

    print(f"Case #{t + 1}: {o}")
