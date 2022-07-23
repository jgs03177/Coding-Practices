import sys
input=sys.stdin.readline

t = int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    z=c
    y=c+b
    x=c+b+a
    print(x,y,z)

# s = input().split().rstrip()

# sys.stdout.write()