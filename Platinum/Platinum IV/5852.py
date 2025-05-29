"""
여러 알고리즘이 섞여 있는 문제이다.
순차적으로 함수로 분리해서 풀어나가면 된다.

마지막에 최단 루트로 모든 섬들을 방문하는 것을 TSP를 응용해서 생각하면 된다.
TSP는 한번 방문한 곳을 방문하지 않았지만, 이 문제는 한번 방문한 곳을 한번 더 
방문해도 되기 때문에 mask부분에서 1인 부분 확인을 제거하면 된다.

39576	784
"""

from collections import deque

def label_islands(R, C, grids):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    label = [[0] * C for _ in range(R)]
    idx = 1

    for r in range(R):
        for c in range(C):
            if grids[r][c] == "X" and label[r][c] == 0:
                q = deque([(r, c)])
                label[r][c] = idx
                while q:
                    r_, c_ = q.popleft()
                    for dr, dc in directions:
                        nr, nc = r_ + dr, c_ + dc
                        if 0 <= nr < R and 0 <= nc < C and grids[nr][nc] == "X" and label[nr][nc] == 0:
                            label[nr][nc] = idx
                            q.append((nr, nc))
                idx += 1
    
    return label, idx - 1

def build_graph(R, C, grids, label, N):
    INF = int(1e9)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    g = [[INF] * (N + 1) for _ in range(N + 1)]

    for r in range(R):
        for c in range(C):
            if label[r][c] > 0:
                q = deque([(r, c)])
                visited = [[-1] * C for _ in range(R)]
                src = label[r][c]
                visited[r][c] = 0

                while q:
                    r_, c_ = q.popleft()
                    for dr, dc in directions:
                        nr, nc = r_ + dr, c_ + dc
                        if 0 <= nr < R and 0 <= nc < C and visited[nr][nc] == -1 and grids[nr][nc] != ".":
                            visited[nr][nc] = visited[r_][c_] + (1 if grids[nr][nc] == "S" else 0)
                            if label[nr][nc] > 0 and label[nr][nc] != src:
                                dst = label[nr][nc]
                                g[src][dst] = min(g[src][dst], visited[nr][nc])
                                g[dst][src] = min(g[dst][src], visited[nr][nc])
                            else:
                                q.append((nr, nc))
    return g

def tsp(g, N):
    INF = int(1e9)
    dp = [[INF] * N for _ in range(1 << N)]
    for i in range(N):
        dp[1 << i][i] = 0

    for mask in range(1 << N):
        for i in range(N):
            if not (mask & (1 << i)):
                continue
            for j in range(N):
                cost = g[i + 1][j + 1]
                if cost == INF:
                    continue
                new_mask = mask | (1 << j)
                dp[new_mask][j] = min(dp[new_mask][j], cost + dp[mask][i])
    return min(dp[(1 << N) - 1])

def get_min_distance(R, C, grids):
    label, N = label_islands(R, C, grids)
    g = build_graph(R, C, grids, label, N)

    print(tsp(g, N))
    
def sol():
    R, C = map(int, input().split())
    grids = [list(input()) for _ in range(R)]

    get_min_distance(R, C, grids)

sol()