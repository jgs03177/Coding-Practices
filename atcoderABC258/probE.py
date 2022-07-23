import sys

input=sys.stdin.readline

nw,nq,x=map(int,input().split())
*w,=map(int,input().split())
# b[i]: if the first potato is i, how many potatoes are in the box?
b=[]
cw=0 # current weight
cn=0 # current number of potatos
j=0  # idx
tp=sum(w)
for i in range(nw):
    batch=(x-cw)//tp
    if batch>0:
        cn+=nw*batch
        cw+=tp*batch
    while cw<x:
        cw+=w[j]
        j=(j+1)%nw
        cn+=1
    b+=[cn]
    cw-=w[i]
    cn-=1

# visit[i]: visited (at ith)
# kb[i]: n potato in kth box
visit=[0]*nw
kb=[]
offset=1
loop=nw
j=0
for i in range(1,nw+2):
    if visit[j]:
        offset=visit[j]
        loop=i-visit[j]
        break
    kb+=[b[j]]
    visit[j]=i
    j=(j+b[j])%nw

l=[]
for i in range(nq):
    k=int(input())
    k=(k-offset)%loop+offset-1 if k>=offset else k-1
    l+=[kb[k]]

print(*l,sep='\n')