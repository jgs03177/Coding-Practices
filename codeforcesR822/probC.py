import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    s = list(input().rstrip())
    o = 0
    for i in range(n):
        if s[i] != '1':
            m = i + 1
            idx = i
            while idx < n and s[idx] != '1':
                if s[idx] == '0':
                    o += m
                s[idx] = '2'
                idx += m
    print(o)
