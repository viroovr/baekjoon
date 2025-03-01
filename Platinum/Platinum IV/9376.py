"""
gpt에게서 얻은 세명의 bfs결과의 거리 합이 최소인 것을 고르라는 힌트.

📌 핵심 아이디어: 최단 거리 합 최소 위치 찾기
우리는 감옥을 탈출하는 데 필요한 문의 개수를 최소화해야 해.
이걸 그래프 탐색 문제로 보면, 세 개의 출발점에서 BFS를 수행한 후, 가장 효율적인 탈출 경로를 찾아야 하는 문제로 바꿀 수 있어.
🚀 왜 세 개의 BFS를 수행하는가?
1. 각 시작점에서 모든 위치까지의 최단 거리(문의 개수)를 구하기 위해
    감옥 바깥(상근이), 죄수 1, 죄수 2 → 각자 BFS 실행
    이걸 통해 맵의 모든 지점에서 해당 지점까지 도달하는 데 필요한 문의 개수를 알아낼 수 있음.
2. 최적의 탈출 위치를 찾기 위해
    (i, j) 지점이 최적의 탈출 위치가 되려면, 세 명이 해당 지점까지 도달하는 문의 개수 합이 최소가 되어야 함.

두 명으로는 단순하게 목적지까지 최단경로를 선택하게 되는데, 이는 최적이 아님. 두 명의 그리디 최단경로 합이, 리얼 최단경로 합(겹쳐지는 경우) 보다 클 수 있기 때문에.
세 명으로의 거리합의 최솟값으로 확실하게 최단경로를 정한다. 이는 해당 점으로 두명의 죄수가 이동하는 최단거리합에다가 해당 점에서 밖으로 향하는 최단거리의 합은 2명이 밖으로 향하는 최단거리 최적해
이기 때문이다.
이를 위해서 바깥 좌표를 두어서 바깥에서 시작한 상근이와 바깥까지 포함한 경로에서 최단경로를 찾아다니는 두 죄수의 거리 합으로 결정한다.
"""
from heapq import heappop, heappush
directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def bfs(start_coords, prison):
    INF = float("inf")
    visited = [[INF] * w for _ in range(h)]
    q = []

    for r, c in start_coords:
        t = 1 if prison[r][c] == "#" else 0
        visited[r][c] = t
        heappush(q, (t, r, c))

    while q:
        cost, r, c = heappop(q)
        for dr, dc in directions:
            nr, nc = dr + r, dc + c
            if 0 <= nr < h and 0 <= nc < w and prison[nr][nc] != "*":
                new_cost = cost + (1 if prison[nr][nc] == "#" else 0)

                if visited[nr][nc] > new_cost:
                    visited[nr][nc] = new_cost
                    heappush(q, (new_cost, nr, nc))
    return visited

def bfs_dp(edge_doors, prison, prisonors):
    INF = float("inf")
    pv1 = bfs([prisonors[0]], prison)
    pv2 = bfs([prisonors[1]], prison)
    v3 = bfs(edge_doors, prison)

    min_val = INF
    for y in range(h):
        for x in range(w):
            if prison[y][x] == "*":
                continue

            cnt = pv1[y][x] + pv2[y][x] + v3[y][x]
            if prison[y][x] == "#":
                cnt -= 2
            
            min_val = min(cnt, min_val)

    return min(min_val, v3[prisonors[0][0]][prisonors[0][1]] + v3[prisonors[1][0]][prisonors[1][1]])

def sol():
    T = int(input())
    for _ in range(T):
        global h, w, prison
        h, w = map(int, input().split())
        prison = [list(input()) for _ in range(h)]
        prisonors, edge_doors = [], []
        for r in range(h):
            for c in range(w):
                if prison[r][c] != '*':
                    if (0 <= c < w and (r == h - 1 or r == 0)) or (0 <= r < h and (c == 0 or c == w - 1)):
                        edge_doors.append((r, c))
                    if prison[r][c] == '$':
                        prisonors.append((r, c))

        print(bfs_dp(edge_doors, prison, prisonors))

sol()