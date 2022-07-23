n,k=map(int,input().split())
*as_,=map(int,input().split())

l=[]
for i in range(k):
    l+=[sorted(as_[i::k])]

counts=0
prv=0
isyes=True
for i in range((n-1)//k):
    for j in range(k):
        if prv>l[j][i]:
            isyes=False
            break
        prv=l[j][i]
        counts+=1
        if counts>=n:
            break
    if isyes==False:
        break
print("Yes" if isyes else "No")