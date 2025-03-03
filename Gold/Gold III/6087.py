"""
기존에는 거리 이하 정보를 체크없이 모두 큐에 넣어서 동일한 정보가 큐에 많았고
이를 in으로 확인했다.
35508	224
하지만 이건 bfs 특성상 O(WH) 만큼 소요되므로 그리 크지 않기 때문에 가능한 것이기에 더
효율적인 풀이가 필요했다.

gpt에게서 visited에 방향정보 추가를 힌트로 얻을 수 있었다.
이를 deque에서 같은 방향은 appendleft로 우선 탐색을, 다른 방향은 append로 추가한다. 이 때,
방문 체크를 하면서 visited 정보는 업데이트 하지 않는다.
대신 우선 순위 좌표(동일 방향)가 popleft될 때, visited[r][c][d]를 체크한다.
38168	80

이렇게 방향정보를 추가하는 이유가. 병목지점에서 여러 방향이 겹쳐 들어올 때, 일직선으로
들어오는 것을 먼저 처리해주기 위해서다.
"""
from collections import deque
directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def logging(board):
    for row in board:
        print(" ".join(f"{num:3.0f}" for num in row))
    print("========")

def get_min_mirrors(board, lazers):
    INF = float("inf")
    distance = [[INF] * C for _ in range(R)]
    visited = [[[False] * 4 for _ in range(C)] for _ in range(R)]

    sr, sc = lazers[0]
    er, ec = lazers[1]
    q = deque()
    distance[sr][sc] = 0
    for i, (dr, dc) in enumerate(directions):
        nr, nc = sr + dr, sc + dc
        visited[sr][sc][i] = True
        if 0 <= nr < R and 0 <= nc < C and board[nr][nc] != "*":
            q.append((0, i, nr, nc))
    
    while q:
        cost, d, r, c = q.popleft()
        visited[r][c][d] = True
        if (r, c) == (er, ec):
            return cost
        
        for i, (dr, dc) in enumerate(directions):
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and board[nr][nc] != "*" and not visited[nr][nc][i]:
                new_cost = cost if i == d else cost + 1

                if new_cost <= distance[nr][nc]:
                    distance[nr][nc] = new_cost
                    if i == d:
                        q.appendleft((new_cost, i, nr, nc))
                    else:
                        q.append((new_cost, i, nr, nc))

def sol():
    global R, C
    C, R = map(int, input().split())
    board = [list(input()) for _ in range(R)]
    lazers = [(r, c) for r in range(R) for c in range(C) if board[r][c] == "C"]
    print(get_min_mirrors(board, lazers))

sol()