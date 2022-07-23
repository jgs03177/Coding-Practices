import sys
input=sys.stdin.readline

t = int(input())
for _ in range(t):
    n,k=map(int,input().split())
    *a,=map(int,input().split())
    b=[(i,a[i]-(n-i-k)) for i in range(n)]  # dmg difference (nojump vs jump)
    b.sort(key=lambda x:x[1], reverse=True)
    dtrap=sum(a)
    for i in range(k):
        idx=b[i][0]
        dtrap-=a[idx]
        dtrap+=n-idx-1
    dtrap-=k*(k-1)//2
    print(dtrap)