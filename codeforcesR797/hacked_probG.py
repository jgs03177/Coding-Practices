import sys,bisect

input=sys.stdin.readline

t=int(input())

for _ in range(t):
    input()
    n,m = map(int,input().split())
    *a, = map(int,input().split())
    lastmin=a[0]
    idx=[0]
    for i in range(1,n):
        e=a[i]
        if lastmin>e:
            idx+=[i]
            lastmin=e
    l=[]
    for i in range(m):
        k,d = map(int,input().split())
        k-=1
        a[k]-=d
        ak=a[k]
        e=bisect.bisect_right(idx,k)  # find leading train idx of idx
        e=e-1
        o=idx[e]  # leading train idx
        newidx=idx[:e+1]
        if a[o] > ak:  # if i became slower
            newidx+=[k]  # add me as a leader
        keepstart=len(idx)
        for j in range(e+1,len(idx)):
            o=idx[j]
            if a[o] < ak:
                keepstart=j
                break
        newidx += idx[keepstart:]
        idx=newidx
        l+=[len(idx)]

    print(*l)
        # 속도변화한 기차를 끌고 가던 기차를 찾는다.
        # 1. 내가 끌고가던 기차라면, 4번으로
        # 2. 끌고가던 기차보다 여전히 내가 더 빠르면, 5번으로.
        # 3. 내가 끌고가는 기차보다 더 느려졌으면, 나를 인덱스에 추가하고 4번으로
        # 4. 나보다 뒤에 끌고가던 기차들이 나보다 더 빠르면, 인덱스에서 제거.
        # 5. 끌고가는 기차 수 카운트
