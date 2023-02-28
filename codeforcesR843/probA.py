import sys

input = sys.stdin.readline

t = int(input())

# string l=x+y+z, either y >= x,z or y<=x,z
# if 'a' in l[1:-1] then set y='a' (y>=x,z)
# if not then y = l[1:-1] = "bbbbb" (y<=x,z)

for _ in range(t):
    l = input().rstrip()
    for i, c in enumerate(l[1:-1], 1):
        if c == 'a':
            print(l[:i], c, l[i + 1:])
            break
    else:
        print(l[0], l[1:-1], l[-1])
