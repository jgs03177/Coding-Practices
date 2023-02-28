import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    s = input().rstrip()
    appearance = [0] * 26
    for c in s:
        appearance[ord(c) - ord('a')] += 1
    freq = sorted(appearance, reverse=True)
    order = sorted(list(range(26)), key=lambda x: appearance[x], reverse=True)
    min_ops = n
    min_d = 1
    # greedy: if appearance[c1]>=d, then change c1 greedily to c2 with a[c1]<d
    for d in range(1, 27):
        if n % d != 0:
            continue
        # make freq[:d]==n//d. if freq[i]>=n//d then cut it down.
        f = n // d
        ops = 0
        for e in freq[:d]:
            ops += abs(e - f)
        for e in freq[d:]:
            ops += e
        ops //= 2
        if min_ops > ops:
            min_ops = ops
            min_d = d
    l = [ord(c) - ord('a') for c in s]

    f = n // min_d
    from_list = [0] * 26
    to_list = []
    for i in range(min_d):
        e = freq[i]
        if e - f >= 0:
            from_list[order[i]] += e - f
        else:
            to_list += [order[i]] * (f - e)
    for i in range(min_d, 26):
        from_list[order[i]] += freq[i]
    for i, c in enumerate(l):
        if from_list[c]:
            l[i] = to_list.pop()
            from_list[c] -= 1
    print(min_ops)
    print(*[chr(c + ord('a')) for c in l], sep='')

    # use 1~26 letters
