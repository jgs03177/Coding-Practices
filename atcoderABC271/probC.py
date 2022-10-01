import sys

input = sys.stdin.readline

n = int(input())
*a, = map(int, input().split())
a = set(a)
r = len(a)
a = sorted(list(a))
a += [10 ** 9] * (n - r)

k = n
o = 0
for i in range(n):
    if i < k:
        e = a[i]
        while e != o + 1 and i < k - 2:
            k -= 2
            o += 1
        if e == o + 1:
            o += 1
        else:
            if i == k - 2:
                o += 1
            break
    else:
        break
print(o)
