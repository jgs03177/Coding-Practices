import sys
input=sys.stdin.readline

# Fenwicktree

def _getParent(i):
    return i - (i & (-i))

def _getNext(i):
    return i + (i & (-i))

def getSum(data, i):
    s=0
    i+=1
    while i>0:
        s += data[i]
        i = _getParent(i)
    return s

def update(data, i, v):
    i+=1
    while i<len(data):
        data[i] += v
        i = _getNext(i)

n=int(input())
*cs,=map(int,input().split())
*xs,=map(int,input().split())

trees = [0]*(n+2)
dbs = [[] for i in range(n+1)]

for i in range(n-1,-1,-1):
    c=cs[i]
    x=xs[i]
    dbs[0]+=[x]
    dbs[c]+=[x]

o = 0
for c in range(n+1):
    for x in dbs[c]:
        e1 = getSum(trees, x - 1)
        o+=-e1 if c else e1
        update(trees, x, 1)
    for x in dbs[c]:
        update(trees, x, -1)
print(o)