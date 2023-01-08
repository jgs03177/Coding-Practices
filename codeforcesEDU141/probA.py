import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    *a, = map(int, input().split())
    a = a[::-1]
    maxa = a[0]
    for i in range(1, n):
        if a[i] != maxa:
            b = a[i]
            a.pop(i)
            print("YES")
            print(b, *a)
            break
    else:
        print("NO")
