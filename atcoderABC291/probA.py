import sys

input = sys.stdin.readline

s = input().rstrip()

for i, e in enumerate(s):
    if e.upper() == e:
        print(i + 1)
        break
