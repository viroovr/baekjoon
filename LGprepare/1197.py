from heapq import heappop, heappush
from sys import stdin
input = stdin.readline
V, E = map(int, input().split())
adjlist = [[] for _ in range(V + 1)]
for _ in range(E):
    A, B, C = map(int, input().split())
    adjlist[A].append((B, C))
    adjlist[B].append((A, C))
# print("adjlist : ", adjlist)


def solution(vertex):
    visited = [False] * (V + 1)
    visited[0] = 0
    point_set = []
    queue = [(0, vertex)]
    total_distance = 0
    while len(point_set) < V:
        # print(queue, visited, point_set)
        current_weight, current_vertex = heappop(queue)
        if visited[current_vertex]:
            continue
        visited[current_vertex] = True
        point_set.append(current_vertex)
        total_distance += current_weight
        for next_vertex, weight in adjlist[current_vertex]:
            if not visited[next_vertex]:
                heappush(queue, (weight, next_vertex))

    return total_distance


print(solution(1))
