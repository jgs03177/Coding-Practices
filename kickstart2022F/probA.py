t=int(input())
for itc in range(t):
    n=int(input())
    l1=[]
    l2=[]
    for i in range(n):
        c,d,u=input().split()
        d=int(d)
        u=int(u)
        l1+=[(c,u)]
        l2+=[(d,u)]
    l1.sort()
    l2.sort()
    o=0
    for e1,e2 in zip(l1,l2):
        o+=e1[1]==e2[1]
    print(f"Case #{itc+1}: {o}")