import sys
input=sys.stdin.readline

n=int(input())
m=n%60
h=n//60
print(f"2{h+1}:{m:02d}")