import sys

input = sys.stdin.readline

h, w = map(int, input().split())
ss = []
for i in range(h):
    s = input().rstrip()
    ss += [s]

xs = []
for j in range(w):
    x = 0
    for i in range(h):
        x += ss[i][j] == "#"
    xs += [x]
print(*xs)
