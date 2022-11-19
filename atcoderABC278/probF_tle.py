import sys

input = sys.stdin.readline

n = int(input())
g = []
for i in range(n):
    s = input().rstrip()
    g += [(s[0], s[-1])]

state = 0
chose = 0


def search(last):
    # return False if lose, True if win
    global state, chose
    if chose == n:
        return False
    for i in range(n):
        flag = state >> i & 1
        if not flag and g[i][0] == last:
            state |= (1 << i)
            chose += 1
            winstatus = search(g[i][1])
            chose -= 1
            state &= not (1 << i)
            if not winstatus:
                return True
    return False


for i in range(n):
    state |= (1 << i)
    chose += 1
    winstatus = search(g[i][1])
    if not winstatus:
        print("First")
        break
    chose -= 1
    state &= not (1 << i)
else:
    print("Second")
