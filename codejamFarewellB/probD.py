# Upsolving with Analysis
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000c9607c/0000000000cad77d#analysis
# Test Set 2: TLE(Python), RE(PyPy)

import sys

input = sys.stdin.readline
sys.setrecursionlimit(302000)

t = int(input())
for case in range(t):
    n, l = map(int, input().split())
    nv = n + l
    graph = [[] for _ in range(nv)]
    for i in range(l):
        nk = input()
        *k, = map(int, input().split())
        for e in k:
            # trainline: 0, ..., l-1
            # trainstation: l, ..., l+n-1
            tl = i
            ts = l + e - 1
            graph[tl] += [ts]
            graph[ts] += [tl]

    # https://en.wikipedia.org/wiki/Biconnected_component#Pseudocode

    parent = [-1] * nv
    visited = [0] * nv
    depth = [0] * nv
    low = [0] * nv
    articulationpoint = [0] * nv


    def dfs(v, d):
        visited[v] = 1
        depth[v] = d
        low[v] = d
        childcount = 0

        for u in graph[v]:
            if not visited[u]:
                parent[u] = v
                dfs(u, d + 1)
                childcount += 1
                if low[u] >= depth[v]:
                    articulationpoint[v] = 1
                low[v] = min(low[v], low[u])
            elif u != parent[v]:
                low[v] = min(low[v], depth[u])
        if parent[v] == -1:
            articulationpoint[v] = int(childcount > 1)


    root = 0
    dfs(root, 0)
    o = sum(articulationpoint[:l])

    print(f"Case #{case + 1}: {o}")
