import sys

input = sys.stdin.readline

n=int(input())
ss=[]
for i in range(n):
    s = input().rstrip()
    ss += [s]
print(*ss[::-1], sep="\n")
