import sys
input=sys.stdin.readline

n=int(input())
print(n*2)
h=n%4
print((str(h) if h else "")+"4"*(n//4))