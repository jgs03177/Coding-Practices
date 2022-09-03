import sys

input = sys.stdin.readline

s = input().rstrip()

rows = [[7],[4],[8,2],[5,1],[9,3],[6],[10]]
res = [all([s[e-1]=="0" for e in l]) for l in rows] # 1 if all knocked

print("Yes" if s[0]=="0" and "1" in "".join(["01"[e] for e in res]).strip("1") else "No")