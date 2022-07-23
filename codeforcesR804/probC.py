import sys

input=sys.stdin.readline

p=1_000_000_007

def pwrmod(a,b):
    o = 1
    a = a % p
    mul = a
    while b > 0:
        if b%2:
            o = mul * o % p
        b >>= 1
        mul = mul * mul % p
    return o


def cache_factorialmodp(n):
    l = [1]
    last = 1
    for i in range(n):
        last = last * (i+1) % p
        l.append(last)
    return l


cache = cache_factorialmodp(100001)


def npkmodp(n, r):
    assert(0<=r<=n<=100000)
    numer = cache[n]
    denom = cache[n-r]
    sol = numer * pwrmod(denom % p,p-2) % p
    return sol


t=int(input())


for _ in range(t):
    n=int(input())
    *a,=map(int,input().split())

    fix=[1]*n

    idx0=0
    for i in range(n):
        if a[i]==0:
            idx0=i
            break

    q=[]
    cmax=a[0]
    fix[a[0]]=0
    blanks=0
    for i in range(1,idx0+1):
        if a[i]<cmax:
            fix[a[i]] = 0
            if blanks:
                q+=[(cmax,blanks)]
            cmax=a[i]
            blanks=0
        else:
            blanks+=1
    cmax = a[-1]
    fix[a[-1]] = 0
    blanks = 0
    for i in range(n-2,idx0-1,-1):
        if a[i]<cmax:
            fix[a[i]] = 0
            if blanks:
                q+=[(cmax,blanks)]
            cmax=a[i]
            blanks=0
        else:
            blanks+=1

    pref=0
    li=[]
    for i in range(n-1,-1,-1):
        pref+=fix[i]
        li+=[pref]
    li=li[::-1]

    q.sort(reverse=True)
    usedblanks=0
    o=1
    for e in q:
        cmax,blanks=e
        nums=li[cmax]-usedblanks
        nc=npkmodp(nums,blanks)
        o=(o*nc)%p
        usedblanks+=blanks
    print(o)