import sys

input = sys.stdin.readline

n, k = map(int, input().split())
*a, = map(int, input().split())

score = [0] * 10001
for i in range(1, n + 1):
    for e in a:
        if i < e:
            break
        score[i] = max(score[i], (i - e) - score[i - e] + e)

print(score[n])
