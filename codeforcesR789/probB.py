import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n = int(input())
    a = input().rstrip()
    state = -1
    nop = 0
    nseg = 0
    for i in range(1,n):
        if i % 2:  # odd
            if a[i-1] != a[i]:  # changed
                nop += 1
            else:
                if state != a[i]:
                    nseg += 1
                state = a[i]
    print(nop, max(nseg,1))

# 처음 문자:
# 상태 0, 홀수개에서 상태 바뀌면: 횟수 +1, 상태 1로 변경
#        짝수개면 그대로
# 상태 1, 짝수개: 횟수 1
#        홀수개: 상태 0으로 변경
# 100001
# 1001
# 11100111
# 11100110
# 100110
# 101101