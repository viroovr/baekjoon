"""
강한 연결 요소끼리 묶는 것 까지 잘했다. 하지만 그 후에 순차적으로 넘어지는 것을
구현하기에 실패했다. bfs로 union-find를 시도했다. 그러나 위상 정렬이 필요했다.
위상 정렬은 순서가 정해져있는 작업을 차례로 수행해야 할 때 그 순서를 결정할 때 사용하는
알고리즘이다.
순서대로 graph에서 정렬해야 할 때 위상정렬을 떠올리고 indegree를 떠올리자

90356	864
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def get_minimum_domino(N, graph):
    low = [0] * (N + 1)
    node_id = [0] * (N + 1)
    idx = 1
    stack = []
    on_stack = [False] * (N + 1)

    result = []
    def dfs(x):
        nonlocal idx
        node_id[x] = low[x] = idx
        idx += 1
        stack.append(x)
        on_stack[x] = True
        
        for nxt in graph[x]:
            if node_id[nxt] == 0:
                dfs(nxt)
                low[x] = min(low[nxt], low[x])
            elif on_stack[nxt]:
                low[x] = min(node_id[nxt], low[x])
        
        if node_id[x] == low[x]:
            scc = []
            while stack:
                nxt = stack.pop()
                on_stack[nxt] = False
                scc.append(nxt)
                if nxt == x:
                    break
            result.append(scc)
            
    for i in range(1, N + 1):
        if node_id[i] == 0:
            dfs(i)

    group_id = [0] * (N + 1)
    for i, gr in enumerate(result):
        for x in gr:
            group_id[x] = i
    
    K = len(result)
    indegree = [0] * K
    for u in range(1, N + 1):
        for v in graph[u]:
            if group_id[u] != group_id[v]:
                indegree[group_id[v]] += 1

    res = 0
    for deg in indegree:
        if deg == 0:
            res += 1

    return res

def sol():
    T = int(input())
    result = []
    for _ in range(T):
        N, M = map(int, input().split())
        graph = [[] for _ in range(N + 1)]
        for _ in range(M):
            x, y = map(int, input().split())
            graph[x].append(y)
        
        result.append(get_minimum_domino(N, graph))
    
    sys.stdout.write("\n".join(map(str, result)) + "\n")

sol()