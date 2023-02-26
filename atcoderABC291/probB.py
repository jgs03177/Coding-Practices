import sys

input = sys.stdin.readline

n = int(input())
*x, = map(int, input().split())

print(sum(sorted(x)[n:-n]) / (3 * n))
