# https://www.acmicpc.net/problem/11779
import heapq


def dijkstra(s, e, graph):
    q = [(0, s)]
    route = [0] * n
    distance = [float('inf')] * n
    distance[s] = 0

    # dijkstra
    while q:
        td, v = heapq.heappop(q)
        if td > distance[v]:  # visited already...
            continue

        for u, c in graph[v]:
            if distance[u] > distance[v] + c:
                distance[u] = distance[v] + c
                route[u] = v  # v -> u
                heapq.heappush(q, (distance[u], u))

    result = [e]
    v = e
    while v != s:
        v = route[v]
        result += [v]

    return distance[e], result[::-1]


if __name__ == '__main__':
    import sys

    input = sys.stdin.readline

    n = int(input())
    m = int(input())
    graph = [[] for _ in range(n)]
    for i in range(m):
        s, e, c = map(int, input().split())
        s -= 1
        e -= 1
        graph[s] += [(e, c)]

    # start -> end
    s, e = map(int, input().split())
    s -= 1
    e -= 1

    min_d, trace = dijkstra(s,e,graph)
    print(min_d)
    print(len(trace))
    print(*[v + 1 for v in trace])
