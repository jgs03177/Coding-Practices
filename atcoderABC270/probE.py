import sys

input = sys.stdin.readline

n, k = map(int, input().split())
*a, = map(int, input().split())

l = [(a[i], i) for i in range(n)]
l.sort()
nonempty_boxes = n
last_apple = 0
prve = 0
batch = []
r = 0
for i in range(n):
    e, idx = l[i]
    de = e - prve
    if nonempty_boxes * de <= k:
        prve = e
        k -= nonempty_boxes * de
        nonempty_boxes -= 1
        batch += [prve]
    else:
        de, r = divmod(k, nonempty_boxes)
        if r:
            de += 1
            r = nonempty_boxes - r
        prve += de
        batch += [prve]
        k = 0
    if not k:
        break

lvl = 0
for i in range(n):
    _, idx = l[i]
    if i < len(batch):
        e = batch[i]
        lvl = e
    a[idx] -= lvl

if r:
    ll = sorted(l[len(batch) - 1:], key=lambda x: x[1])
    for i in range(abs(r)):
        _, idx = ll[-i - 1]
        a[idx] += 1
print(*a)
