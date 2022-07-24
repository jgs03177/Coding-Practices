import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    h, w = map(int, input().split())
    n = int(input())
    s = input().rstrip()
    *l, = map(int, input().split())
