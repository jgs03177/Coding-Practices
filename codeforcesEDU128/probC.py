# 코스트(i,j) = max(지운 1의 개수, 남은 0의 개수)
# [i:j] 1의 개수 = [0:j] 1의 개수 - [0:i] 1의 개수
# 지운 1의 개수 = [0:N] 1의 개수 - [0:j] 1의 개수 + [0:i] 1의 개수
# 남은 0의 개수 = j-i - [0:j] 1의 개수 + [0:i] 1의 개수

import sys
input=sys.stdin.readline

t = int(input())

for _ in range(t):
    s = input().rstrip()
    n = len(s)
    left1 = [0]*(n+1)
    for i in range(n):
        left1[i + 1] = left1[i] + (1 if s[i] == "1" else 0)
    tot1 = left1[n]
    mincost = min(tot1,n-tot1)  # # 1s and # 0s
    for i in range(1,n+1):
        mincost = min(mincost, tot1-left1[i]+left1[max(0,i-tot1)])
    print(mincost)
