import sys

input = sys.stdin.readline

n = int(input())
q = n // 4
r = n % 4
print(q * 4 + 2 + 4 * (r >= 3))
