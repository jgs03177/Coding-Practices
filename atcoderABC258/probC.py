import sys
input=sys.stdin.readline

n,q=map(int,input().split())
s=input().rstrip()
offset=0
for i in range(q):
    a,x=map(int,input().split())
    if a==1:
        offset=(offset+x)%n
    else:
        print(s[x-offset-1])