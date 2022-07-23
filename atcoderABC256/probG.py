
n,d=map(int,input().split())
mod=998244353

ll=[1]
for i in range(d-1):
    lll=[1]
    for j in range(len(ll)-1):
        lll+=[(ll[j]+ll[j+1])%mod]
    lll+=[1]
    ll=lll

def matmul(m1,m2):
    return [(m1[0]*m2[0]+m1[1]*m2[1])%mod,
            (m1[0]*m2[1]+m1[1]*m2[2])%mod,
            (m1[1]*m2[1]+m1[2]*m2[2])%mod]

ncr=ll  # d-1 C r
tot=2 # all black and all white
for k in range(1,d+1):
    #for _ in range(n):
    #    b, w= ((b*ncr[k] if k!=d else 0)+w*ncr[k-1])%mod, (b*ncr[k-1]+(w*ncr[k-2] if k!=1 else 0))%mod
    # b = [nck  nck-1] b
    # w = [nck-1  nck-2] w
    # k number of whites
    mn=[1,0,1]  # m0
    m1=[ncr[k] if k!=d else 0, ncr[k-1], ncr[k-2] if k!=1 else 0]
    n2=n
    while n2:
        if n2&1:
            mn=matmul(mn,m1)
        m1=matmul(m1,m1)
        n2>>=1
    tot = (tot + mn[2] + mn[0]) % mod
print(tot)