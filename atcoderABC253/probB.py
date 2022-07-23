h, w = map(int, input().split())
g = []
for i in range(h):
    l = input()
    g += [l]
xx, yy = [], []
for i in range(h):
    for j in range(w):
        if g[i][j] == "o":
            xx += [i]
            yy += [j]
print(abs(xx[0] - xx[1]) + abs(yy[0] - yy[1]))