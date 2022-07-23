import sys
from collections import deque

input=sys.stdin.readline

t=int(input())

for _ in range(t):
    n,k = map(int,input().split())
    s = input().rstrip()
    q = deque()
    m = k
    minm = k
    for i in range(k):
        isb="B" == s[i]
        m-=isb
        minm=min(minm,m)
        q+=[isb]
    for i in range(k,n):
        prvb=q.popleft()
        m+=prvb
        isb="B" == s[i]
        m-=isb
        minm=min(minm,m)
        q+=[isb]
    print(minm)