"""
아이디어가 아주 신선했다.
시간초과가 계속 나서 왜 나지 O(N) 아닌가? 했는데
각 쿼리에 대해 실행하므로 O(M * N)으로 100억번 연산을 하게 돼 시간초과가 나는것이다.
쿼리의 개수를 간과한 문제

2^K 조상으로 빠르게 건너뛰어, 1개씩 건너뛰는 것보다 시간 단축을 함
O(NlogN + MlogN)의 시간복잡도 가능하다.


depth를 0으로 초기화하는게 -1로 초기화하는것보다 빠른가?
파이썬에서 리스트를 생성할 때:
    depth = [-1] * (N + 1):
        * -1 값을 가진 리스트를 생성해야 하므로 메모리 할당 + 값 초기화 과정이 필요.
        * 즉, (N+1)개의 -1을 복사해서 리스트에 저장해야 함.
    depth = [0] * (N + 1):
        * 같은 방식이지만, -1보다 0의 연산이 더 빠르게 최적화될 가능성이 높음.
        * 이유: 0은 메모리에서 "null-like" 값으로 최적화될 수 있음 (CPU, OS 의존).

1. depth를 0으로 초기화
2. data.split()/ idx사용
3. a,b 동일 깊이 옮기기 bit연산
96832	1148
96856	1140    1
103696	1048    1,2,3
104360	952     1,2
"""

import sys
from collections import deque

LOG = 17

def build_tree(graph):
    parent = [[-1] * LOG for _ in range(N + 1)]
    depth = [0] * (N + 1)

    q = deque([1])

    while q:
        x = q.popleft()

        for node in graph[x]:
            if node == parent[x][0]:
                continue
            parent[node][0] = x
            depth[node] = depth[x] + 1
            q.append(node)
    
    return parent, depth

def preprocess(parent):
    for k in range(1, LOG):
        for i in range(1, N + 1):
            if parent[i][k - 1] != -1:
                parent[i][k] = parent[parent[i][k - 1]][k - 1]

def lca(a, b):
    if depth[a] < depth[b]:
        a, b = b, a

    for k in range(LOG - 1, -1, -1):
        if depth[a] - (1 << k) >= depth[b]:
            a = parent[a][k]
    
    if a == b:
        return a

    for k in range(LOG - 1, -1, -1):
        if parent[a][k] != parent[b][k]:
            a = parent[a][k]
            b = parent[b][k]

    return parent[a][0]

def sol():
    global N, M, parent, depth
    data = sys.stdin.read().split()
    idx = 0

    N = int(data[idx])
    idx += 1

    graph = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = int(data[idx]), int(data[idx + 1])
        graph[a].append(b)
        graph[b].append(a)
        idx += 2
    
    parent, depth = build_tree(graph)
    preprocess(parent)

    M = int(data[idx])
    idx += 1

    result = []
    for _ in range(M):
        result.append(str(lca(int(data[idx]), int(data[idx + 1]))))
        idx += 2

    sys.stdout.write("\n".join(result)+"\n")

sol()
