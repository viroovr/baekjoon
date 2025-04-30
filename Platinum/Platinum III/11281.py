"""
처음엔 stack에서 요소를 뽑으며, dfs를 돌면서 같은 abs값이 존재한다면 sys.exit(0)
하도록 설정했다. sccs에는 위상 정렬 순서대로 정렬되어있으므로, 앞에서부터 탐색하면서
scc안 노드에 False값을 대입했다.

두번 째는, dfs를 돌면서 scc안에 abs값이 있는지 확인하지 않고, scc_id 배열을 선언해서
각 노드에 scc_id를 부여했다. 위상 정렬상 먼저 오는 것들이 낮은 scc_id를 가지도록 했다.
각 요소의 기본 bool값을 False로 두고, neg값이 먼저온다면 해당 요소를 True로 두도록 했다.

52648	336
74716	408
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def get_index(i):
    return -2 * i if i < 0 else 2 * i - 1

def get_node(index):
    return index // 2 + 1 if index % 2 else -(index // 2)

def get_2_sat(N, graph, t_graph):
    stack = []
    visited = [False] * (2 * N + 1)

    def dfs(node):
        visited[node] = True
        for nxt in graph[node]:
            if not visited[nxt]:
                dfs(nxt)
        
        stack.append(node)
    
    for i in range(1, 2 * N + 1):
        if not visited[i]:
            dfs(i)
    
    visited = [False] * (2 * N + 1)
    scc_id = [0] * (2 * N + 1)
    sccs = []
    scc_count = 0

    def t_dfs(node):
        visited[node] = True
        sccs[-1].append(node)
        scc_id[node] = scc_count
        for nxt in t_graph[node]:
            if not visited[nxt]:
                t_dfs(nxt)

    sccs = []
    while stack:
        i = stack.pop()
        if not visited[i]:
            sccs.append([])
            t_dfs(i)
            scc_count += 1

    bool_val = [0] * (N + 1)
    for i in range(1, N + 1):
        if scc_id[get_index(i)] == scc_id[get_index(-i)]:
            print(0)
            return
        elif scc_id[get_index(i)] > scc_id[get_index(-i)]:
            bool_val[i] = 1

    print(1)
    print(" ".join(map(str, bool_val[1:])))

def sol():
    N, M = map(int, input().split())
    graph = [[] for _ in range(2 * N + 1)]
    t_graph = [[] for _ in range(2 * N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[get_index(-a)].append(get_index(b))
        graph[get_index(-b)].append(get_index(a))
        t_graph[get_index(b)].append(get_index(-a))
        t_graph[get_index(a)].append(get_index(-b))
    
    get_2_sat(N, graph, t_graph)

sol()