# 벽 부수고 이동하기
import sys
sys.setrecursionlimit(10 ** 4)
N, M = 1000, 1000
# N, M = map(int, input().split())
# road_map = [list(map(int, input())) for _ in range(N)]
road_map = [[0 for _ in range(M)] for _ in range(N)]
MIN_DEPTH = 2_001
dp = [[2_001 for _ in range(M)] for _ in range(N)]
check = [[0 for _ in range(M)] for _ in range(N)]
DXDY = [(0, 1), (1, 0), (-1, 0), (0, -1)]
# print(road_map)


def is_bound(y, x):
    return 0 <= y < N and 0 <= x < M


def search(y, x, depth, wall):
    global dp, road_map, check
    # print(depth, y, x)
    if dp[y][x] != MIN_DEPTH:
        return dp[y][x]
    if y == N - 1 and x == M - 1:
        dp[N - 1][M - 1] = min(depth, dp[N - 1][M - 1])
        return dp[N - 1][M - 1]
    min_list = []
    check[y][x] = 1
    for dx, dy in DXDY:
        X = x + dx
        Y = y + dy
        if not is_bound(Y, X) or check[Y][X]:
            continue
        if road_map[Y][X] == 0:
            min_list.append(search(Y, X, depth + 1, wall))
        else:
            if wall == 1:
                continue
            min_list.append(search(Y, X, depth + 1, 1))
    check[y][x] = 0
    if min_list:
        dp[y][x] = min(min_list)
    return dp[y][x]


k = search(0, 0, 1, 0)
print(dp)
if k == MIN_DEPTH:
    print(-1)
else:
    print(k)
