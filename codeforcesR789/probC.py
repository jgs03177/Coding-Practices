#dp
import sys
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    n = int(input())
    *p, = map(int,input().split())
    np = [[0]*(n+1) for _ in range(n+1)]  # m[i][j]: number of elements smaller than j in p_1 ... p_i
    for i in range(n):  # position 1~n+1
        pi = p[i]
        for a in range(1,n+1):  # number a in pi
            if pi <= a:       # count the smaller number in left (including itself)
                np[i+1][a] = np[i][a] + 1
            else:
                np[i+1][a] = np[i][a]
    # print(np)
    ans = 0
    for b in range(1,n):
        for c in range(b+1,n-1):
            pb=p[b]  # for every pb and pc
            pc=p[c]
            # count the combinations: #small than pc but idx < b * #big than pc but idx > c
            l = np[b][pc]
            r = pb-np[c+1][pb]
            ans+=l*r
    print(ans)