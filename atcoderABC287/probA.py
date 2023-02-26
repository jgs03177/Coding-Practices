import sys

input = sys.stdin.readline

n = int(input())
nfor = 0
for i in range(n):
    s = input().rstrip()
    if s == "For":
        nfor += 1

print("Yes" if nfor > n - nfor else "No")
