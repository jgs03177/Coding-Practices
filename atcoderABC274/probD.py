import sys

input = sys.stdin.readline

n, x, y = map(int, input().split())
*a, = map(int, input().split())

# even a -> x value
# odd a -> y value

status = [[0] * 20001, [0] * 20001]
status[0][10000 + a[0]] = 1
status[1][10000] = 1
for i, a in enumerate(a[1:], 1):
    prv = status[i & 1]
    new = []
    for j in range(20001):
        new += [(prv[j - a] if j - a >= 0 else 0) | (prv[j + a] if j + a <= 20000 else 0)]
    status[i & 1] = new
print("Yes" if status[0][x + 10000] and status[1][y + 10000] else "No")
