import sys

input = sys.stdin.readline

n = int(input())
l = "0123456789ABCDEF"
print(l[n // 16], l[n % 16], sep="")
