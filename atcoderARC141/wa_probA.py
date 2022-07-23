import sys, math

input = sys.stdin.readline
qs = []
for i in range(1, 9):  # i: len(m) for targetable m
    q = 1
    j = i  # j: len(n) for targetable n
    while True:
        q = q * (10 ** i) + 1  # q: repeating positions, n = m * q. eg -> 123123123 = 123 * 1001001
        j += i
        if j > 18:
            break
        qs += [(q, i, j)]
qs.sort(key=lambda x: x[2])  # order q by the target length of n

t = int(input())
for _ in range(t):
    n = int(input())
    sn = int(math.log(n, 10)) + 1  # sn = len(n)
    result = 11
    for q, i, j in qs:  # q: positions, i: target length of m, j: target length of n
        if j > sn:  # if len(n) < targetable length of n, then searching is useless
            break
        target = min(n, 10 ** j - 1)  # n or 999999999
        r = target % q  # how much should i subtract, to make n2 repeating
        n2 = target - r
        d = n2 // q
        if 10 ** (i - 1) <= d < 10 ** i:
            result = max(result, n2)
    print(result)