import sys

input = sys.stdin.readline

s = input().rstrip()
print({"Mo":5,"Tu":4,"We":3,"Th":2,"Fr":1}[s[0:2]])