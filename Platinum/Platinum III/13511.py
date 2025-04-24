"""
로직은 맞앗는데, k번째 요소 찾기에서 깊이를 잘못 계산해줬다.
u와 lca내에 kth 요소를 찾을 때 깊이를 1을 기준으로 깊이 계산을 해서 틀리고 있었다.

참고한 로직은 같은 레벨의 두 노드에서 lca를 찾는 건데, LOG - 1부터 조상을 찾으면서 
다를 경우, 그 조상을 현재 노드로 설정한다. 다를 경우에 한 해 계속 바뀌므로 직전 노드까지
변경된다. 따라서 최종 노드의 부모 노드를 반환하면 된다.

245508	2072
"""
from collections import deque
import sys 
input = sys.stdin.readline
def build_tree(N, graph):
    q = deque([1])
    depth = [-1] * (N + 1)
    parent = [(0, 0)] * (N + 1)
    depth[1] = 1
    while q:
        u = q.popleft()
        for v, w in graph[u]:
            if v == parent[u][0]:
                continue
            q.append(v)
            parent[v] = (u, w)
            depth[v] = depth[u] + 1

    return parent, depth

def build_dp(parent):
    dp = [parent]
    for _ in range(LOG):
        r = []
        for u, w in dp[-1]:
            if u and dp[-1][u][0]:
                r.append((dp[-1][u][0], dp[-1][u][1] + w))
            else:
                r.append((0, 0))
        dp.append(r)
    return dp

def get_path_cost(u, v):
    if depth[u] < depth[v]:
        u, v = v, u

    cost = 0
    for i in range(LOG - 1, -1, -1):
        if depth[dp[i][u][0]] >= depth[v]:
            cost += dp[i][u][1]
            u = dp[i][u][0]

    if u == v:
        return cost
    
    for i in range(LOG - 1, -1, -1):
        if dp[i][u][0] != dp[i][v][0]:
            cost += dp[i][u][1] + dp[i][v][1]
            u = dp[i][u][0]
            v = dp[i][v][0]
    return cost + dp[0][u][1] + dp[0][v][1]

def get_lca(u, v):
    if depth[u] < depth[v]:
        u, v = v, u
    
    for i in range(LOG - 1, -1, -1):
        if depth[dp[i][u][0]] >= depth[v]:
            u = dp[i][u][0]

    if u == v:
        return u
    
    for i in range(LOG - 1, -1, -1):
        if dp[i][u][0] != dp[i][v][0]:
            u = dp[i][u][0]
            v = dp[i][v][0]

    return dp[0][u][0]

def get_th(d, u):
    for i in range(LOG - 1, -1, -1):
        if depth[dp[i][u][0]] > d:
            u = dp[i][u][0]

    if depth[u] == d:
        return u
    
    return dp[0][u][0]

def get_kth_element(u, v, k):
    lca = get_lca(u, v)
    d = depth[lca] + abs((depth[u] - depth[lca] + 1) - k)

    if depth[u] - depth[lca] + 1 >= k:
        return get_th(d, u)
    return get_th(d, v)

def sol():
    global dp, LOG, depth
    N = int(input())
    graph = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    LOG = len(bin(N)) - 2
    parent, depth = build_tree(N, graph)
    dp = build_dp(parent)

    M = int(input())
    result = []
    for _ in range(M):
        query = tuple(map(int, input().split()))
        if query[0] == 1:
            result.append(get_path_cost(query[1], query[2]))
        else:
            result.append(get_kth_element(query[1], query[2], query[3]))
    
    sys.stdout.write("\n".join(map(str, result)) + "\n")
        
        

sol()