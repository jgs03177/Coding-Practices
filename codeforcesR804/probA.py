import sys

input=sys.stdin.readline

t=int(input())

for _ in range(t):
    n=int(input())
    if n&1:
        print(-1)
    else:
        print(n//2, 0, 0)
