"""
강한 연결요소를 찾고 시작점에서 레스토랑 까지 최댓값을 탐색한다.
이 때, 최댓값 탐색과정을 DFS로 해서 시간초과가 발생했다. 동일하게 방문된
노드를 또 한번 방문하므로 시간초과가 발생할 수 있다.
이를 위해 다이나믹 프로그래밍을 이용해서 최댓값을 메모이제이션 하는 방법을
gpt를 통해 알게됬다. 

알고리즘들이 두 개 이상이 나올 수 있음을 안 문제이다.
당연히 다른 문제들도 두 개 이상 나올수 있지만, Tarjan알고리즘이 구현이 길어서
구현하다 보면 두 개 이상의 풀이법으로 접근하고 있음을 강하게 느끼기 때문이다.

하지만 이 방법이 맞다. SCC압축을 통해 사이클을 제거하고, 압축된 DAG위에서
최댓값을 구하기 때문이다.

337788	2608    Tarjan
379308	3136    kosaraju
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def get_max_withdrawal(N, graph, atms, S, restaurant):

    groups = [0] * (N + 1)
    weights = []
    group_res = []
    SG = -1
    gidx = 0
    
    vo = [0] * (N + 1)
    low = [0] * (N + 1)
    idx = 0
    stack = []
    on_stack = [False] * (N + 1)

    def dfs(node):
        nonlocal idx, gidx, SG
        idx += 1
        vo[node] = low[node] = idx
        stack.append(node)
        on_stack[node] =  True

        for nxt in graph[node]:
            if vo[nxt] == 0:
                dfs(nxt)
                low[node] = min(low[nxt], low[node])
            elif on_stack[nxt]:
                low[node] = min(vo[nxt], low[node])
        
        if low[node] == vo[node]:
            scc = []
            while stack:
                top = stack.pop()
                scc.append(top)
                on_stack[top] = False
                if top == node:
                    break
            w = 0
            res = False
            for node in scc:
                if node == S:
                    SG = gidx
                if restaurant[node]:
                    res = True
                w += atms[node]
                groups[node] = gidx
            weights.append(w)
            group_res.append(res)
            gidx += 1

    for i in range(1, N + 1):
        if vo[i] == 0:
            dfs(i)

    group_graph = [set() for _ in range(gidx)]
    for i in range(1, N + 1):
        for nxt in graph[i]:
            if groups[i] != groups[nxt]:
                group_graph[groups[i]].add(groups[nxt])

    cost = [0] * gidx
    q = deque([SG])
    cost[SG] = weights[SG]
    while q:
        node = q.popleft()
        cur_cost = cost[node]
        for nxt in group_graph[node]:
            new_cost = cur_cost + weights[nxt]
            if new_cost > cost[nxt]:
                q.append(nxt)
                cost[nxt] = new_cost

    max_val = -1
    for i in range(gidx):
        if group_res[i]:
            max_val = max(cost[i], max_val)

    print(max_val)

from collections import deque
def sol():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
    
    atms = [0] + [int(input()) for _ in range(N)]

    S, _ = map(int, input().split())
    restaurant = [False] * (N + 1)
    for i in map(int, input().split()):
        restaurant[i] = True
    
    get_max_withdrawal(N, graph, atms, S, restaurant)

sol()