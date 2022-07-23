n=int(input())
l=[[1]]
for i in range(n-1):
    ll=l[-1]
    lll=[1]
    for j in range(len(ll)-1):
        lll+=[ll[j]+ll[j+1]]
    lll+=[1]
    l+=[lll]
for e in l:
    print(*e)