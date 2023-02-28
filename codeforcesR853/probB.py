import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    s = input().rstrip()
    # match 1~n
    match = [0] * n
    for i in range(n):
        match[i] = s[i] == s[n - 1 - i]
    flip = 0
    for i in range(n // 2):
        if flip == 0:
            if not match[i]:
                flip = 1
        if flip == 1:
            if match[i]:
                flip = 2
        if flip == 2:
            if not match[i]:
                flip = 3
    print("YES" if flip < 3 else "NO")
