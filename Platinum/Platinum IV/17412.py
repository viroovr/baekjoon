"""
Ford-Fulkserson 알고리즘에 대해 학습할 수 있는 기초적인 문제이다.

소스에서 유량으로의 최대 유량을 구하는 문제이며, 이를 탐욕적 방법으로
최적해를 찾아낸다.

BFS를 사용하면 O(VE^2)로 개선됨이 증명되었다.


"""

from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    q = deque([SOURCE])
    parent = [-1] * MAX_NODE
    parent[SOURCE] = SOURCE

    while q and parent[SINK] == -1:
        node = q.popleft()
        for nxt in graph[node]:
            if capacity[node][nxt] - flow[node][nxt] > 0 and parent[nxt] == -1:
                parent[nxt] = node
                q.append(nxt)
                
    return parent

def get_max_route():
    total_flow = 0
    print(graph)
    while True:
        parent = bfs()
        if parent[SINK] == -1:
            break
        
        print(parent)
        amount = INF
        cur = SINK
        while cur != SOURCE:
            amount = min(amount, capacity[parent[cur]][cur] - flow[parent[cur]][cur])
            cur = parent[cur]

        cur = SINK
        while cur != SOURCE:
            flow[parent[cur]][cur] += amount
            flow[cur][parent[cur]] -= amount
            cur = parent[cur]

        total_flow += amount
    
    print(total_flow)

N, P = map(int, input().split())
SINK = 2
SOURCE = 1
MAX_NODE = N + 1
INF = 12345
graph = [[]] + [set() for _ in range(N)]
flow = [[0] * MAX_NODE for _ in range(MAX_NODE)]
capacity = [[0] * MAX_NODE for _ in range(MAX_NODE)]

for _ in range(P):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)
    capacity[a][b] += 1

get_max_route()
