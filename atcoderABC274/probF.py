# Atcoder ABC274 Prob F upsolving v2
# https://atcoder.jp/contests/abc274/editorial/5083
# Code adapted for Python to get AC.
"""
x(i,t) position of fish i at time t
    x(i,t) = x0(i) + v(i) * t
consider net of size a, left boundary positioning on fish i.
    left boundary: x(i,t), right boundary: x(i,t)+a
fish j meets i (left boundary) at time t
    x(i,t) == x(j,t)
  <==>  x0(i)-x0(j) + (v(i)-v(j)) * t == 0
    t_l(i,j) = - (x0(i)-x0(j)) / (v(i)-v(j))
fish j meets right boundary at time t:
    x(i,t)+a == x(j,t)
  <==>  x0(i)-x0(j)+a + (v(i)-v(j)) * t == 0
    t_r(i,j) = - (x0(i)-x0(j)+a) / (v(i)-v(j))
let t_in = min(t_l,t_r), t_out = max(t_l,t_r)
consider total value only on those t values.

Pseudocode:
sort fishes based on the x0s.
for i in range(n):
    consider a net ranged x(i,t), x(i,t)+a
    calculate total value at t=0
    list = empty
    for j in range(n) and j!=i:
        get t_min(i,j), t_max(i,j)
        store in the list as a (t, in=0/out=1, j) format. in first, out second.
    sort the list
    calculate prev_time
    for t,io,j in list if t>0 or t==0 and io=out:
        update total value by adding/removing the value of j.
        update max total value
"""
import sys
from collections import defaultdict


def frac(a,b):
    return int(a*10**12//b)


input = sys.stdin.readline

n, a = map(int, input().split())
w = []
x0 = []
v = []

for _ in range(n):
    wi, x0i, vi = map(int, input().split())
    w += [wi]
    x0 += [x0i]
    v += [vi]

zero = frac(0, 1)
max_total_value = 0
for i in range(n):
    eventadd = defaultdict(int)
    eventdel = defaultdict(int)
    for j in range(n):
        v_diff = v[j] - v[i]
        x0_diff = x0[j] - x0[i]
        if v_diff == 0:
            if 0 <= x0_diff <= a:
                eventadd[zero] += w[j]
        elif v_diff > 0:
            start = frac(-x0_diff, v_diff)
            end = frac(a - x0_diff, v_diff)
            eventadd[start] += w[j]
            eventdel[end] += w[j]
        else:
            start = frac(x0_diff - a, -v_diff)
            end = frac(x0_diff, -v_diff)
            eventadd[start] += w[j]
            eventdel[end] += w[j]
    total_value = 0
    for t in sorted(eventadd.keys()|eventdel.keys()):
        total_value += eventadd[t]
        if not (t < zero):
            max_total_value = max(max_total_value, total_value)
        total_value -= eventdel[t]

print(max_total_value)
