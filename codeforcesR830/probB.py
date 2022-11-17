import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    s = input().rstrip()
    init = s[0] == "0"
    nflip = 0
    prv = s[0]
    for c in s:
        nflip += prv != c
        prv = c
    print(max(0, nflip - init))
