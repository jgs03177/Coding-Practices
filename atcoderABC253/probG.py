import sys
from collections import deque

input = sys.stdin.readline
n, l, r = map(int, input().split())

queue = deque(range(1, n + 1))
li = []
q = 0
total_swaps = n * (n - 1) // 2
current_swap = n
swaps_done = 0
while swaps_done < total_swaps:
    current_swap -= 1
    start = 1
    end = current_swap + 1
    s1 = False
    lli = []
    rli = []
    if swaps_done < l <= swaps_done + current_swap:
        i = queue.popleft()
        for _ in range(l - swaps_done - 1):
            lli += [queue.popleft()]
        queue.appendleft(i)
        s1 = True
    if swaps_done < r <= swaps_done + current_swap:
        for _ in range(swaps_done + current_swap - r):
            rli += [queue.pop()]
        s1 = True
    if s1:
        queue.rotate(1)
        if len(lli):
            i = queue.popleft()
            queue.extendleft(lli[::-1])
            queue.appendleft(i)
        queue.extend(rli[::-1])
    elif l <= swaps_done and current_swap + swaps_done < r:
        queue.rotate(1)
    li += [queue.popleft()]
    swaps_done += current_swap
li += [queue.pop()]
print(*li)