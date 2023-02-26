import sys

input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()
ns = len(s)
nt = len(t)

fr = nt
for i in range(nt):
    if s[i] == t[i] or s[i] == '?' or t[i] == '?':
        pass
    else:
        fr = i
        break

bk = nt
for i in range(nt):
    if s[-i - 1] == t[-i - 1] or s[-i - 1] == '?' or t[-i - 1] == '?':
        pass
    else:
        bk = i
        break

for x in range(nt + 1):
    print("Yes" if fr >= x and bk >= nt - x else "No")
