import sys

input = sys.stdin.readline

n, s = map(int, input().split())
visit = [None] * (s + 1)
visit[0] = ""
for i in range(n):
    visit2 = [None] * (s + 1)
    a, b = map(int, input().split())
    for j in range(s + 1):
        va = None
        vb = None
        if j >= a and visit[j - a] is not None:
            va = visit[j - a] + "H"
        if j >= b and visit[j - b] is not None:
            vb = visit[j - b] + "T"
        visit2[j] = va if va is not None else vb
    visit = visit2
print("Yes" if visit[s] is not None else "No")
if visit[s] is not None: print(visit[s])
