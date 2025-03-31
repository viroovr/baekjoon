"""
MST문제인줄 알고 삽질했다. 각 노드에 도착한 시간 중에, 최댓값만 알면되는거다.

50040	708 
50020	628 q의 cost가 distance보다 작다면 continue
"""

from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def get_infection_time(graph, N, c):
    INF = int(1e8)
    distance = [INF] * (N + 1)

    q = [(0, c)]
    distance[c] = 0

    while q:
        cost, x = heappop(q)

        if cost > distance[x]:
            continue

        for b, s in graph[x]:
            new_cost = cost + s
            if new_cost < distance[b]:
                distance[b] = new_cost
                heappush(q, (new_cost, b))

    new_distance = [i for i in distance if i != INF]
    max_cost = max(new_distance)
    cnt = len(new_distance)
    
    return f"{cnt} {max_cost}"

def sol():
    idx = 0
    T = int(input())
    result = []
    for _ in range(T):
        n, d, c = map(int, input().split())

        graph = [[] for _ in range(n + 1)]
        for _ in range(d):
            a, b, s = map(int, input().split())
            graph[b].append((a, s))

        result.append(get_infection_time(graph, n, c))

    sys.stdout.write("\n".join(result)+"\n")
sol()
    