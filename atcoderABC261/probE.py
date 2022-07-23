import sys
input=sys.stdin.readline

n,c=map(int,input().split())
x1=(2<<30)-1
x0=0
out0=x0
out1=x1
for i in range(n):
    t,a=map(int,input().split())
    if t==1:
        out1&=a
        out0&=a
    elif t==2:
        out1|=a
        out0|=a
    else:
        out1^=a
        out0^=a
    ones = c
    zeros = (~c)&x1
    c = (ones&out1)|(zeros&out0)
    print(c)
