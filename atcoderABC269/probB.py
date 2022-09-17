import sys

input = sys.stdin.readline

r = set()
c = set()
for i in range(1, 11):
    s = input().rstrip()
    for j in range(10):
        if s[j] == "#":
            c.add(j + 1)
            r.add(i)
print(f"{min(r)} {max(r)}\n{min(c)} {max(c)}")
