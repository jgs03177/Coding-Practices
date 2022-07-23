import sys,math

input=sys.stdin.readline

t=int(input())

isprime=[1]*201
primes=[1]
for i in range(2,201):
    if isprime[i]:
        primes+=[i]
        for j in range(i+i,201,i):
            isprime[i]=0

def lcm(a,b):
    return a*b//math.gcd(a,b)

for _ in range(t):
    n=int(input())
    s = input().rstrip()
    *lp, = map(int,input().split())
    visit=[1]*n
    cycles=[]
    for i in range(n):
        if visit[i]:
            p=i
            cycle=0
            while visit[p]:
                visit[p]=0
                cycle+=1
                p=lp[p]-1
            divisors=[]
            for prime in primes:
                if cycle%prime==0:
                    divisors+=[prime]
            for divisor in divisors:
                repeatword=""
                p=i
                isFail=False
                for _ in range(divisor):
                    repeatword+=s[p]
                    p=lp[p]-1
                for j in range(cycle-divisor):
                    if s[p]!=repeatword[j%divisor]:
                        isFail=True
                        break
                    p=lp[p]-1
                if isFail:
                    continue
                cycle=divisor
                break
            cycles+=[cycle]

    result=cycles[0]
    for e in cycles[1:]:
        result=lcm(result,e)

    print(result)