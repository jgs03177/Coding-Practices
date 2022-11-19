import sys

input = sys.stdin.readline

h, m = map(int, input().split())
t = h * 60 + m

while True:
    h, m = t // 60, t % 60
    h1, m1 = h % 10, m // 10
    h2, m2 = h - h1 + m1, m - m1 * 10 + h1 * 10
    if 0 <= h2 <= 23 and 0 <= m2 <= 59:
        break
    t = (t + 1) % (60 * 24)

print(h, m)
