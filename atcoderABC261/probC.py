import sys
input=sys.stdin.readline

n=int(input())
d={}
for i in range(n):
    s=input().rstrip()
    g = d.setdefault(s, 0)
    o = s + (f"({g})" if g else "")
    print(o)
    d[s]=g+1
