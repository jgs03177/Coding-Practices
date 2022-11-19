import sys

input = sys.stdin.readline

n = int(input())
*a, = map(int, input().split())
ta = [0] * n
da = 0
tda = 0
q = int(input())
for t in range(1, q + 1):
    act, *ix = map(int, input().split())
    if act == 1:
        da = ix[0]
        tda = t
    elif act == 2:
        i = ix[0] - 1
        x = ix[1]
        if ta[i] >= tda:
            a[i] += x
        else:
            ta[i] = tda
            a[i] = x
    else:
        i = ix[0] - 1
        print(a[i] + da if ta[i] >= tda else da)
