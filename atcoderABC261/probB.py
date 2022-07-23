import sys
input=sys.stdin.readline

n=int(input())
g=[]
for i in range(n):
    s=input().rstrip()
    g+=[s]

fake=0
for i in range(n):
    for j in range(i+1,n):
        a =g[i][j] == "W" and g[j][i]=="L"
        b =g[i][j] == "L" and g[j][i] == "W"
        c = g[i][j] == "D" and g[j][i] == "D"
        fake = fake | (not (a|b|c))

print(["correct", "incorrect"][fake])