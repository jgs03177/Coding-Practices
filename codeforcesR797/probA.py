import sys

input=sys.stdin.readline

t=int(input())

for _ in range(t):
    n = int(input())
    mid=n//3
    remain=n%3
    a = mid + (remain>=2)
    b = mid+1 + (remain>=1)
    c = mid-1
    print(a,b,c)
