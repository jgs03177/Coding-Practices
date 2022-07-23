# https://atcoder.jp/contests/abc254/tasks/abc254_f
# need segtree...

import sys
input=sys.stdin.readline

n,q=map(int,input().split())
*as_,=map(int,input().split())
*bs,=map(int,input().split())
for i in range(q):
    h1,h2,w1,w2=map(int,input().split())
