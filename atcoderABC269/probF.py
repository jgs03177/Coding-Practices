import sys

input = sys.stdin.readline

modulo = 998244353


def val(i, j, m):
    return (i - 1) * m + j


def find(a, b, c, d, m):
    dx = b - a + 1  # dx number of cells
    dy = d - c + 1  # dy number of cells
    v1 = val(a, c, m) + val(b, d, m)

    if dx & 1 and dy & 1:  # odd odd
        ncell = dx * dy // 2 + (not (a + c) & 1)
        o = v1 * ncell // 2 % modulo
    elif (not dx & 1) and (not dy & 1):  # even even
        ncell = dx * dy // 2
        o = v1 * ncell // 2 % modulo
    else:
        if dx & 1:
            o = (find(a, b, c + 1, d, m) + find(a + (a + c) % 2, b - (b + c) % 2, c, c, m)) % modulo
        else:
            o = (find(a + 1, b, c, d, m) + find(a, a, c + (a + c) % 2, d - (a + d) % 2, m)) % modulo
    return o


n, m = map(int, input().split())
q = int(input())
for i in range(q):
    a, b, c, d = map(int, input().split())
    print(find(a, b, c, d, m))
