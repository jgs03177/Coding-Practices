import sys

input = sys.stdin.readline

t = int(input())
pi = "314159265358979323846264338327"
# 3.14159265358979323846264338327950288
for _ in range(t):
    s = input().rstrip()
    for i in range(len(s)):
        if s[i] != pi[i]:
            print(i)
            break
    else:
        print(len(s))
