import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def get_scc(N, graph):
    vo = [0] * N
    idx = 0
    low = [0] * N

    stack = []
    on_stack = [False] * N
    result = []
    
    def dfs(x):
        nonlocal idx
        idx += 1
        vo[x] = low[x] = idx
        stack.append(x)
        on_stack[x] = True

        for nxt in graph[x]:
            if vo[nxt] == 0:
                dfs(nxt)
                low[x] = min(low[x], low[nxt])
            elif on_stack[nxt]:
                low[x] = min(low[x], vo[nxt])
        
        if vo[x] == low[x]:
            scc = []
            while stack:
                top = stack.pop()
                on_stack[top] = False
                scc.append(top)
                if top == x:
                    break
            result.append(scc)
    
    for i in range(N):
        if vo[i] == 0:
            dfs(i)
    
    return result

def topology_sort(N, graph, sccs):
    group_id = [0] * N
    for i, scc in enumerate(sccs):
        for node in scc:
            group_id[node] = i
    
    K = len(sccs)
    indegree = [0] * K
    for i in range(N):
        for nxt in graph[i]:
            if group_id[nxt] != group_id[i]:
                indegree[group_id[nxt]] += 1
    
    # print(indegree)
    result = []
    cnt = indegree.count(0)
    if cnt != 1:
        return "Confused"
    
    i = indegree.index(0)
    for x in sccs[i]: 
        result.append(x)
    
    return "\n".join(map(str, sorted(result)))
        

def sol():
    T = int(input())
    for i in range(T):
        if i > 0:
            input()
        N, M = map(int, input().split())
        graph = [[] for _ in range(N)]
        for _ in range(M):
            A, B = map(int, input().split())
            graph[A].append(B)

        sccs = get_scc(N, graph)
        print(topology_sort(N, graph, sccs))
        if i < T - 1:
            print()
sol()