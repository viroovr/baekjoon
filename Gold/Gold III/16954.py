"""
벽이 1초뒤에 한칸 씩 내려오므로 미리 boards를 생성해서 각 t에맞는 board의 벽을 확인하는 코드를 짰다.
하지만 현재 위치 그대로있는 조건과, visted값이 현재 t보다 작으면 이동하지 않는다는 이상한 조건을 추가했다.
이렇게 틀렸는데, visted 조건을 제거하고 나니 해결되긴 했다.
133152	608

하지만 중복 방문을 처리해줘야 하므로, visited set을 설정해서 (r,c,t)값을 저장하고 이를 확인했다.
그리고 미리 board를 생성하지 않고, 현재 r값에서 t만큼 뺀 행의 열값이 벽인지 확인하도록 바꿨다.
34984	60
"""

from collections import deque

def can_go(N, board):
    directions = [(0,0),(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    sr, sc = N - 1, 0
    er, ec = 0, N - 1
    q = deque([(sr, sc, 0)])
    visited = [[[False] * N for _ in range(N)] for _ in range(N)]

    while q:
        r, c, t = q.popleft()

        if t == 8:
            return 1

        if board[max(0, r - t)][c] == "#":
            continue

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and not visited[t][nr][nc]:
                if nr - t >= 0 and board[nr - t][nc] == "#":
                    continue
                if (nr, nc) == (er, ec):
                    return 1
                q.append((nr, nc, t + 1))
                visited[t][nr][nc] = True
    return 0

def sol():
    N = 8
    board = [list(input()) for _ in range(N)]
    print(can_go(N, board))

sol()
