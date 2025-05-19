"""
네트워크 플로우의 Edmonds-karp 방법과 visited 배열을 이용해 계산해 봤지만 최단 경로가 중간에 두 개의 경로로
나눠진다면, 탐색하지 못하는 문제가 있었다.

따라서, 이전에 이분매칭에서 super worker노드를 두어 네트워크 유량 문제로 푼 것처럼. 어느 노드를 방문할 때,
꼭 거쳐야 하는 가상노드를 두고, 그 가상 노드에서 원래 노드 유량 용량을 1로 설정한다. SRC와 SINK는 1로 두지 않고
edge만큼 늘릴 수 있다.

Edmonds-karp 알고리즘은 O(VE^2)이다.
BFS를 통해 최단 경로를 리턴한다. O(V + E). BFS를 반복하면서, 잔여 용량이 0이 되는 간선이 최소 1개 이지만
이는 최악의 경우 O(E)번 반복하게 된다. E는 최대 V^2개 있을 수 있으므로, O(VE^2)이다

V가 2 * N + 1로 최대 800, E가 최대 2 * N + 2 * P 이므로 200,000개가 가능하다.
하지만 시간초과가 발생하지 않는 이유는, 매번 최단 경로를 찾고 Bottle-neck이 빠르게 생성되기 때문이다.
45220	292

Dinic 알고리즘은 BFS로 level 그래프를 생성하고, DFS를 이용해 플로우를 업데이트한다.
BFS와 DFS의 시간복잡도는 O(V + E)이다. 레벨 그래프가 생성될 때 마다, SRC에서 SINK까지의
최단 경로가 최소 1씩 증가한다. 최단 경로의 길이는 최대 V - 1번까지 반복될 수 있다. O(V)
따라서 O(V^2E)를 가진다.
43656	116
"""

from collections import deque
import sys
input = sys.stdin.readline
def get_max_cnt(N, graph, flow, capacity, maxn, src, sink):
    def bfs(src, sink):
        nonlocal level
        level = [-1] * maxn
        level[src] = 0
        q = deque([src])
        while q:
            now = q.popleft()
            for nxt in graph[now]:
                if level[nxt] == -1 and capacity[now][nxt] - flow[now][nxt] > 0:
                    level[nxt] = level[now] + 1 
                    q.append(nxt)
        return level[sink] != -1

    def dfs(now, f):
        if now == sink:
            return f
        for i in range(work[now], len(graph[now])):
            nxt = graph[now][i]
            if level[nxt] == level[now] + 1 and capacity[now][nxt] - flow[now][nxt] > 0:
                result_flow = dfs(nxt, min(f, capacity[now][nxt] - flow[now][nxt]))
                if result_flow > 0:
                    flow[now][nxt] += result_flow
                    flow[nxt][now] -= result_flow
                    work[now] = i
                    return result_flow
        work[now] = len(graph[now])
        return 0

    level = [-1] * maxn
    INF = int(1e6)
    max_flow = 0

    while bfs(src, sink):
        work = [0] * maxn

        while 1:
            result_flow = dfs(src, INF)
            if result_flow == 0:
                break
            max_flow += result_flow
    
    print(max_flow)


def sol():
    def add_edge(a, b, cap):
        graph[a].append(b)
        graph[b].append(a)
        capacity[a][b] += cap

    N, P = map(int, input().split())
    MAXN = 2 * N + 1
    SRC, SINK = 1 + N, 2
    graph = [[] for _ in range(MAXN)]
    flow = [[0] * (MAXN) for _ in range(MAXN)]
    capacity = [[0] * (MAXN) for _ in range(MAXN)]
    for i in range(1, N + 1):
        add_edge(i + N, i, 1)

    for _ in range(P):
        a, b = map(int, input().split())
        c, d = a + N, b + N
        add_edge(a, d, 1)
        add_edge(b, c, 1)
        if c == SRC or a == SINK:
            capacity[c][a] += 1
        if d == SRC or b == SINK:
            capacity[d][b] += 1

    get_max_cnt(N, graph, flow, capacity, MAXN, SRC, SINK)

sol()