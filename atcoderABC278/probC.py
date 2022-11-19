import sys

input = sys.stdin.readline

n, q = map(int, input().split())
d = set()

for i in range(q):
    t, a, b = map(int, input().split())  # 1 follow, 2 uf, 3 question?
    if t == 1:
        d |= {(a, b)}
    elif t == 2:
        d -= {(a, b)}
    else:
        print("Yes" if {(a, b), (b, a)} <= d else "No")
