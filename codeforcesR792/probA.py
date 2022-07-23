import sys
input=sys.stdin.readline

t = int(input())
for _ in range(t):
    num = int(input())
    fd = num%10
    minnum = fd
    num2 = num
    while num2:
        dig = num2%10
        if dig < minnum:
            minnum=dig
        num2 //= 10
    if num < 100:
        minnum=fd
    print(minnum)

    # 2자리: 첫째수
    # 그이상: 가장작은수

# a,b=map(int,input().split())

# sys.stdout.write()