import sys
input = sys.stdin.readline

from heapq import heappop, heappush

def get_min_cost(N, M, graph, start, end):
    INF = int(2e9)
    distance = [INF] * (N + 1)
    distance[start] = 0

    parent = [-1] * (N + 1)
    q = [(0, start)]

    while q:
        cost, x = heappop(q)

        if x == end:
            break

        if cost > distance[x]:
            continue

        for y, c in graph[x]:
            if distance[y] > cost + c:
                distance[y] = cost + c
                heappush(q, (cost + c, y))
                parent[y] = x
    
    print(distance[end])

    i = end
    result = []
    while i != -1:
        result.append(i)
        i = parent[i]
    
    print(len(result))
    print(*reversed(result))

def sol():
    N = int(input().strip())
    M = int(input().strip())

    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b, c = map(int, input().strip().split())
        graph[a].append((b, c))
    
    start, end = map(int, input().strip().split())

    get_min_cost(N, M, graph, start, end)

sol()