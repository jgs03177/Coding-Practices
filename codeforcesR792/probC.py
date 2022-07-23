import sys
input=sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m=map(int,input().split())
    oa=[]
    na=[]
    li=[]
    recheck=[]
    for j in range(n):
        *a, = map(int, input().split())
        oa.append(a)
    for j in range(n):
        a = oa[j]
        aa = sorted(a)
        rec=True
        for i in range(m):
            if a[i]!=aa[i]:
                rec=False
                if i not in li:
                    li+=[i]
                if len(li)>2:
                    break
        if len(li)>2:
            break
        if rec:
            recheck+=[j]
    if len(li)>2:
        print(-1)
    elif len(li)==0:
        print(1,1)
    elif len(recheck):
        assert(len(li)==2)
        successtest=True
        for i in recheck:
            if oa[i][li[0]]!=oa[i][li[1]]:
                successtest=False
                break
        print(li[0]+1,li[1]+1) if successtest else print(-1)
    else:
        print(li[0]+1,li[1]+1)