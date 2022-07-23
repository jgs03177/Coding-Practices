import sys
input=sys.stdin.readline

n=int(input())
ss=[]
for i in range(n):
    s=input().rstrip()
    ss+=[s]

ll=[]
for a in range(n):
    for b in range(n):
        for dx,dy in (1,1), (1,0), (1,-1), (0,-1): #, (-1,-1), (-1, 0),(-1, 1), (0,1):
            l=""
            i,j=a,b
            for _ in range(n):
                l+=ss[i][j]
                i,j=(dx+i)%n,(dy+j)%n
            ll+=[l, l[::-1]]
        # for i in range(n):
        #     l=""
        #     for j in range(n):
        #         l+=ss[j][i]
        #     ll+=[l,l[::-1]]
        #
        # for i in range(n):
        #     l=""
        #     for j in range(n):
        #         l+=ss[(i+j)%n][j]
        #     ll+=[l,l[::-1]]
        #
        # for i in range(n):
        #     l=""
        #     for j in range(n):
        #         l+=ss[(i-j)%n][j]
        #     ll+=[l,l[::-1]]

print(max(ll))
