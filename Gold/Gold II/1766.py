"""
작은 숫자가 우선으로 와야하므로 우선순위 큐를 이용해 작은 숫자를 먼저 처리했다.

print(*result) 와 print(" ".join(map(str, result)))) 가 시간 차이가 16ms정도 났는데
이는 내부적으로 연산 횟수 차이라 생각된다.

*는 result의 요소를 unpacking하고 이를 string으로 처리한 뒤 출력 포맷을 정해 출력하므로 복잡하지만
join 연산은 모든 요소를 한 개의 string으로 변환해서 바로 출력하므로 빠르다.
41656	144 *result
43472	132 join문
"""

import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def get_grade(N, graph, indegrees):
    q = []
    for i in range(1, N + 1):
        if indegrees[i] == 0:
            heappush(q, i)
    result = []
    while q:
        x = heappop(q)
        result.append(x)
        for nxt in graph[x]:
            indegrees[nxt] -= 1
            if indegrees[nxt] == 0:
                heappush(q, nxt)

    print(" ".join(map(str, result)))

def sol():
    N, M = map(int, input().split())
    
    graph = [[] for _ in range(N + 1)]
    indegrees = [0] * (N + 1)
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegrees[b] += 1
    
    get_grade(N, graph, indegrees)

sol()