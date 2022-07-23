import sys
input=sys.stdin.readline

n=int(input())
*a,=map(int,input().split())
pre=0
b=[]
for i in range(n-1,-1,-1):
    pre+=a[i]
    b+=[pre]
p=0
for i in range(n):
    if b[i]>=4:
        p+=1
print(p)