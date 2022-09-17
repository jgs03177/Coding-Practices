import sys
import math

input = sys.stdin.readline

n = int(input())
max_iter = math.ceil(math.log2(n))
interval = 2 ** (max_iter - 1)
x, y = 0, 0
e = interval
for i in range(max_iter):
    interval //= 2
    print(f"? {1} {n} {1} {min(e, n)}", flush=True)
    t = int(input())
    d = e
    if t == d:
        e += interval
    else:
        e -= interval
    if interval == 0:
        e += t == d
y = e
interval = 2 ** (max_iter - 1)
e = interval
for i in range(max_iter):
    interval //= 2
    print(f"? {1} {min(e, n)} {1} {n}", flush=True)
    t = int(input())
    d = e
    if t == d:
        e += interval
    else:
        e -= interval
    if interval == 0:
        e += t == d
x = e
print(f"! {x} {y}", flush=True)
