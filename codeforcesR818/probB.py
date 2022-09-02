import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k, r, c = map(int, input().split())
    r, c = (r-1)%k,(c-1)%k
    l = [["."]*k for _ in range(k)]
    for i in range(k):
        l[i][i] = "X"
    l[r][r] = "."
    l[c][c] = "."
    l[r][c] = "X"
    l[c][r] = "X"
    for i in range(n//k):
        for e in l:
            print("".join(e)*(n//k))

