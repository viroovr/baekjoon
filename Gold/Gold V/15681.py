"""
dfs를 이용해서 child부터 세야 하는 문제
bfs와 union find에 꽂혀서 바로 생각하지 못했다.
74792	320
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def get_sub_trees(edges, queries):
    size = [-1] * (N + 1)
    
    def dfs(cur):
        size[cur] = 1
        for node in edges[cur]:
            if size[node] != -1:
                continue
            size[cur] += dfs(node)
        return size[cur]

    dfs(R)

    result = []
    for q in queries:
        result.append(str(size[q]))
    
    return "\n".join(result)

def sol():
    global N, R, Q
    N, R, Q = map(int, input().split())
    edges = [[] for _ in range(N + 1)]

    for _ in range(N - 1): 
        u, v = map(int, input().split())
        edges[u].append(v)
        edges[v].append(u)
    
    queries = [int(input()) for _ in range(Q)]

    print(get_sub_trees(edges, queries))

sol()