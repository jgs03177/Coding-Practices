import sys

input = sys.stdin.readline

n,m = map(int, input().split())
*a, = map(int, input().split())

minus_part = sum(a[:m])

maxsum=0
for i in range(m):
    maxsum+=(i+1)*a[i]

cursum=maxsum
for i in range(m,n):
    cursum-=minus_part
    cursum+=m*a[i]
    minus_part-=a[i-m]
    minus_part+=a[i]
    maxsum=max(maxsum,cursum)

print(maxsum)