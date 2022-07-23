import sys,math
input=sys.stdin.readline

n=int(input())

v=0
ll=[]
for i in range(n):
    l=[]
    for j in range(n):
        v+=1
        s=v-1 if j&1 else v+1
        if j==n-1 and n&1:
            s=v
        l+=[s]
    ll+=[l]
for l in ll:
    print(*l)