import sys
input=sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    ss = []
    topmost = 5
    leftmost = 5
    for i in range(n):
        s = input().rstrip()
        ss.append(s)
        for j in range(m):
            if s[j]=="R":
                topmost = min(i, topmost)
                leftmost = min(j, leftmost)
    print("YES" if ss[topmost][leftmost]=="R" else "NO")

