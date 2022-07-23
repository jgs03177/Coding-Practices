import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n,m = map(int,input().split())
    s = input().rstrip()
    stdq = [0]*m
    coll = [0]*m
    rowl = [0]*m
    rowsum = 0
    colgood = 0
    buffer = []
    for i in range(n):
        for j in range(m):
            a = int(s[i*m+j])
            rowsum -= stdq[j]
            stdq[j] = a
            rowsum += a
            if rowsum != 0:
                rowl[j] += 1
            if a==1 and coll[j]==0:
                colgood += 1
                coll[j] = 1
            sys.stdout.write(f"{rowl[j]+colgood} ")
    print()
            # buffer.append(rowl[j]+colgood)
    # print(*buffer)
