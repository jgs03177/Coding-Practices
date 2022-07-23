import sys
input=sys.stdin.readline

ntc=int(input())
for t in range(ntc):
    b,k,x1,y1,x2,y2=map(int,input().split())

    rx1=x1%b
    rx2=x2%b
    ry1=y1%b
    ry2=y2%b
    c=k*(abs(x1-x2)+abs(y1-y2))
    lixy1=[(-rx1,0),(0,-ry1)]
    if rx1:
        lixy1+=[(-rx1+b,0)]
    if ry1:
        lixy1+=[(0,-ry1+b)]
    lixy2=[(-rx2,0),(0,-ry2)]
    if rx2:
        lixy2+=[(-rx2+b,0)]
    if ry2:
        lixy2+=[(0,-ry2+b)]
    for dx1,dy1 in lixy1:
        for dx2,dy2 in lixy2:
            o=k*(abs(dx1)+abs(dx2)+abs(dy1)+abs(dy2))+abs(y1+dy1-y2-dy2)+abs(x1+dx1-x2-dx2)
            print(dx1,dy1,dx2,dy2,o)
            c=min(c,o)
    print(c)