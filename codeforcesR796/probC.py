import sys

input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n=int(input())
    ss=[0]*26
    a=ord('a')
    for i in range(2*n+1):
        s = input().rstrip()
        for e in s:
            ss[ord(e)-a]^=1
    i=ss.index(1)
    print(chr(a+i))

    # 홀수 번 나오는 알파벳을 찾는다!
    # 그 알파벳은 첫문자 또는 끝문자에 나올 것이다.
    # 그 알파벳들과 첫 문자를 매칭시킨다.
    # 첫 문자 + 남은 알파벳으로 처음 글자를 찾는다.