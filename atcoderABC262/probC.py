import sys

input = sys.stdin.readline

n = int(input())
*a, = map(int, input().split())
nc = 0
nc2 = 0
for i in range(n):
    if i + 1 == a[i]:
        nc += 1
    elif a[a[i] - 1] - 1 == i:
        nc2 += 1
p1 = nc * (nc - 1) // 2 + nc2 // 2
print(p1)
