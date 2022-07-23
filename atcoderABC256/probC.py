import sys
input=sys.stdin.readline

h1,h2,h3,w1,w2,w3=map(int,input().split())

t=0
for i1 in range(1,29):
    for i2 in range(1,29):
        i3=w1-i1-i2
        if i3 < 1:
            continue
        for j1 in range(1,29):
            k1 = h1-i1-j1
            if k1 < 1:
                continue
            for j2 in range(1,29):
                k2 = h2-i2-j2
                if k2 < 1:
                    continue
                j3 = w2-j1-j2
                if j3 < 1:
                    continue
                k3 = h3-i3-j3
                k32 = w3-k1-k2
                if k3!=k32 or k3 < 1:
                    continue
                t+=1
print(t)