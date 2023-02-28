import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    w, d, h = map(int, input().split())
    a, b, f, g = map(int, input().split())
    dw = abs(a - f)
    dd = abs(b - g)
    rw = min(a + f, 2 * w - a - f)
    rd = min(b + g, 2 * d - b - g)
    print(h + min(rw + rd, dw + rd, rw + dd))
