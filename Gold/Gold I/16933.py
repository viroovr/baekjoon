"""
제자리에서 대기 하는 것도 고려 요소에 넣는다.

bfs문제에서 queue폭발과 방문처리 이 요소들을 잘 처리하는게 아직은 부족한것 같다.
dijikstra적 관점으로 다 해결하려다 보니 생긴 일
python으로 시간내에 안풀리는 문제
367188	5288
"""

from collections import deque


import sys
input = sys.stdin.readline

def get_shortest_path(N, M, K, grids):
    visited = [[[0] * M for _ in range(N)] for _ in range(K + 1)]

    visited[0][0][0] = 1
    q = deque([(1, 0, 0, 0)])
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while q:
        cost, broken, x, y = q.popleft()

        if y == N - 1 and x == M - 1:
            print(cost)
            return
        
        day = cost % 2
        for dx, dy in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M:
                if grids[ny][nx] == 1 and broken < K and visited[broken + 1][ny][nx] == 0:
                    if day:
                        visited[broken + 1][ny][nx] = cost
                        q.append((cost + 1, broken + 1, nx, ny))
                    else:
                        q.append((cost + 1, broken, x, y))
                elif grids[ny][nx] == 0 and visited[broken][ny][nx] == 0:
                        visited[broken][ny][nx] = cost
                        q.append((cost + 1, broken, nx, ny))

    # for row in visited:
    #     print(*row)

    print(-1)

def sol():
    N, M, K = map(int, input().split())
    grids = [list(map(int, list(input().rstrip()))) for _ in range(N)]

    get_shortest_path(N, M, K, grids)

sol()