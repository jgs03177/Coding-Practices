import sys

input = sys.stdin.readline

x, y, z = map(int, input().split())
if (y - x) * (y) > 0:
    print(abs(x))
elif (-y) * (z - y) > 0:
    print(abs(z) + abs(z - y) + abs(y - x))
else:
    print(-1)
