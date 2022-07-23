import sys
input=sys.stdin.readline

t = int(input())
for _ in range(t):
    n,k=map(int,input().split())
    *a,=map(int,input().split())
    l = [0]*n
    d = {}
    dis = n
    dup = 0
    for e in a:
        if e<n:
            l[e]+=1
        else:
            d.setdefault(e,0)
            d[e]+=1
    mex=n
    tempk=k
    for i in range(n):
        if l[i]:
            pass
        elif tempk>0:
            tempk-=1
        else:
            mex=i
            break
    *dl,=d.values()
    for i in range(mex,n):
        if l[i]:
            dl+=[l[i]]
    dl.sort(reverse=True)
    tempk=k
    while len(dl) and k:
        c = dl.pop()
        if k>=c:
            k=k-c
        else:
            k=0
            dl.append(c)
    print(len(dl))


# s = input().split().rstrip()

# sys.stdout.write()