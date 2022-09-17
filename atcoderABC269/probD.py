import sys

input = sys.stdin.readline

dxys = [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, 0), (1, 1)]

graph = [[0] * 2003 for _ in range(2003)]   # 0 / 1~1000 / 1001 / 1002~2001 / 2002
                                            # -1001 / -1000~-1 /  0   / 1~1000 / 1001
points = []
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    graph[x + 1001][y + 1001] = 1
    points += [(x + 1001, y + 1001)]

cc = 0
for e in points:
    x, y = e
    if graph[x][y]:
        cc += 1
        q = [(x, y)]
        graph[x][y] = 0
        while q:
            x, y = q.pop()
            for dxy in dxys:
                dx, dy = dxy
                if graph[x + dx][y + dy]:
                    q += [(x + dx, y + dy)]
                    graph[x + dx][y + dy] = 0

print(cc)
