import sys
input=sys.stdin.readline

n,x=map(int,input().split())

print(chr(ord('A')+(x-1)//n))