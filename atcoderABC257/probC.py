import sys
input=sys.stdin.readline

n=int(input())
s=input().rstrip()
*w,=map(int,input().split())

p=[]
zeros=0
for i in range(n):
    t=(s[i]=='0')
    zeros+=t
    e=(w[i],t)
    p+=[e]

p.sort(key=lambda x:x[0])

score=[]
current0=0
current1=n-zeros
prv=-1
for i in range(n):
    weight,is0=p[i]
    if weight==prv:
        pass
    else:
        score+=[current0+current1]
        prv=weight
    current0+=is0   # add 1 if 0
    current1-=(1-is0)  # subtract 1 if 1
score+=[current0+current1]

print(max(score))
