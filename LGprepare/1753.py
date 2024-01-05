from sys import stdin, stdout
import heapq
input = stdin.readline
print = stdout.write
V, E = map(int, input().split())
K = int(input())
adjlist = [list() for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adjlist[u].append((v, w))
INF = 10 * 300_000 * 2


def dijkstra(start):
    st = [(0, start)]
    distance = [INF] * (V + 1)
    distance[start] = 0
    while st:
        d, p = heapq.heappop(st)
        if d > distance[p]:
            continue
        for v, w in adjlist[p]:
            nd = d + w
            if nd < distance[v]:
                distance[v] = nd
                heapq.heappush(st, (nd, v))
    return distance


distance = dijkstra(K)
for i in range(1, V + 1):
    if distance[i] == INF:
        print('INF\n')
    else:
        print('%d\n' % distance[i])

