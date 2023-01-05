import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    *p, = map(int, input().split())
    adj_swap = False
    visited = [0] * n
    o = 0
    for i in range(n):
        mark = i + 1
        travels = 0
        while visited[i] == 0:
            visited[i] = mark
            j = p[i] - 1
            i = j
            travels += 1
        o += max(travels - 1, 0)
    for i in range(n - 1):
        if visited[i] == visited[i + 1]:
            adj_swap = True
            break
    if adj_swap:
        print(o - 1)
    else:
        print(o + 1)
