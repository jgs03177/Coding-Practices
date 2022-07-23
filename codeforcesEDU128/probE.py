import sys
input=sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    s1 = input().rstrip()
    s2 = input().rstrip()
    distance = 0
    cluster = 0
    move = 0
    last1 = 0
    last2 = 0
    lasti = 0
    initial = 1
    lastflip = 0
    for i in range(n):
        if (s1[i] == "*" or s2[i] == "*"):  #present
            if cluster >0 and ((last1 and s1[i] == "*") or (last2 and s2[i] == "*")):
                lastflip=0
                pass  # connected
            else:  # disconnected cluster breaker
                move += cluster
                cluster = 0
                if (last1 and s1[i] == "*") or (last2 and s2[i] == "*"):
                    if not initial:
                        move += i - lasti -1
                        lastflip = 0
                else:
                    if not initial:
                        move += i - lasti -1 + (0 if lastflip%2 else 1)
                        lastflip += 1
                initial = 0
            last1 = s1[i] == "*"
            last2 = s2[i] == "*"
            cluster += last1 + last2
            lasti = i
        else:
            move += cluster
            cluster = 0
    move += cluster
    print(move-1)