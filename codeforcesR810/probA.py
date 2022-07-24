import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    l = [n]
    for i in range(1,n):
        l+=[i]
    print(*l)