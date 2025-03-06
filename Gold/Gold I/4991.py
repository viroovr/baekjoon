"""
처음에는, 로봇위치와 더러운 칸 위치에서 시작하는 visited 배열들의 최소합을 생각했다.
하지만 무방향 경로 문제가아닌, 방향 경로 문제이므로 이 방법은 롤백했다.

각 지점 bfs를 통해 최단 경로 graph를 생성하고, brute forth backtracking으로 N! 경로에 대해 
최단 방문 경로 길이를 계산했다. N이 최대 10일때, 10! ~= 3*10^6 이므로 충분히 시간 범위 내라, 가능하다.
35508	384

gpt에게 물어보니 dp + bitmasking으로 하면, N * 2 ^ N 시간복잡도의 풀이가 가능했다.
1은 방문했음을, 0은 방문하지 않음을 나타내는 경로를 bit로 표현해서 dp로 푼다.
10 * 2 ^ 10 ~= 10^4 이므로 더 효율적인 알고리즘임을 학습했다.
35508	216
"""
from heapq import heappop, heappush
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def bfs(start_r, start_c, rooms):
    visited = [[INF] * C for _ in range(R)]
    visited[start_r][start_c] = 0
    q = [(0, start_r, start_c)]
    while q:
        cost, r, c = heappop(q)
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and rooms[nr][nc] != "x":
                new_cost = cost + 1
                if new_cost < visited[nr][nc]:
                    visited[nr][nc] = new_cost
                    heappush(q, (new_cost, nr, nc))
    return visited

def build_distance_graph(rooms):
    dirties = []
    robot = (0, 0)
    for r in range(R):
        for c in range(C):
            if rooms[r][c] == "*":
                dirties.append((r, c))
            elif rooms[r][c] == "o":
                robot = (r, c)
    nodes = [robot] + dirties
    N = len(nodes)

    graph = [[0] * N for _ in range(N)]
    for i, (r, c) in enumerate(nodes):
        distance = bfs(r, c, rooms)
        for j, (nr, nc) in enumerate(nodes):
            if j == i:
                continue
            
            if distance[nr][nc] == INF:
                return None, None
            graph[i][j] = distance[nr][nc]
    return graph, N

def get_min_moving(graph, N):
    dp = [[INF] * N for _ in range(1 << N)]

    dp[1][0] = 0
    for mask in range(1, 1 << N):
        for i in range(N):
            if dp[mask][i] == INF:
                continue

            for j in range(N):
                if mask >> j & 1 == 0:
                    new_mask = mask | (1 << j)
                    dp[new_mask][j] = min(dp[new_mask][j], dp[mask][i] + graph[i][j])
    
    return min(dp[-1][1:])

INF = 20*20*10
while True:
    C, R = map(int, input().split())
    if C == 0:
        break
    rooms = [list(input()) for _ in range(R)]
    graph, N = build_distance_graph(rooms)
    if graph:
        print(get_min_moving(graph, N))
    else:
        print(-1)
