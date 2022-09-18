# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb409/0000000000bef943#analysis
# Analysis, Approach #3

import sys

input = sys.stdin.readline

t = int(input())

for ntc in range(t):
    n, k, x, d = map(int, input().split())
    m = int(input())
    lrq = []
    for i in range(m):
        p, l, r = map(int, input().split())
        p -= 1
        lrq += [(l, 1, p)]
        lrq += [(r + x, 0, p)]
    lrq.sort()
    status = [0] * n  # status[p]: number of meetings of person p in window
    n_status = [0] * (m + 1)  # n_status[j]: number of person with (status[i]==j) for all person i
    n_status[0] = n
    max_status = 0  # maximum i with non-zero n_status[i]
    n_max_status = k  # number of person we need to add in max_status
    total_cancel = 0
    min_cancel = m
    for e in lrq:
        t, lr, p = e
        if t >= x:
            min_cancel = min(min_cancel, total_cancel)

        if t > d:
            break
        if lr:  # left
            n_status[status[p]] -= 1
            status[p] += 1
            n_status[status[p]] += 1
            if status[p] == max_status:
                n_max_status += 1
            if n_max_status > n_status[max_status]:
                max_status += 1
                n_max_status = 1
            if status[p] <= max_status:
                total_cancel += 1

        else:  # right
            if status[p] <= max_status:
                total_cancel -= 1
            if status[p] == max_status:
                n_max_status -= 1
            n_status[status[p]] -= 1
            status[p] -= 1
            n_status[status[p]] += 1
            if n_max_status == 0:
                max_status -= 1
                n_max_status = n_status[max_status]

    min_cancel = min(min_cancel, total_cancel)
    o = min_cancel
    print(f"Case #{ntc + 1}: {o}")
