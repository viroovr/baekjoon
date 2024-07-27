# 벽 부수고 이동하기
from collections import deque
N, M = map(int, input().split())
road_map = [list(map(int, input())) for _ in range(N)]
check = [[0 for _ in range(M)] for _ in range(N)]
DXDY = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def is_bound(y, x):
    return 0 <= y < N and 0 <= x < M


9 9
0110000111
0110110111
0000110111
1111110111
1111110111
0000000111
0111111111
0010011111
0010111111
0000111110sss


def bfs(y, x, depth):
    q = deque()
    q.append((y, x, 0, depth))
    while q:
        cy, cx, cwall, cdepth = q.popleft()
        print(cdepth, cy, cx, cwall)
        if check[cy][cx] == 1:
            continue
        if cy == N - 1 and cx == M - 1:
            return cdepth
        for dx, dy in DXDY:
            X = cx + dx
            Y = cy + dy
            if not is_bound(Y, X) or check[Y][X]:
                continue
            if road_map[Y][X] == 0:
                q.append((Y, X, cwall, cdepth + 1))
            if road_map[Y][X] == 1 and cwall == 0:
                q.append((Y, X, 1, cdepth + 1))
        check[cy][cx] = 1
    return -1


print(bfs(0, 0, 1))
