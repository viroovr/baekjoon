N, M = map(int, input().split())
mold = [list(map(int, input())) for _ in range(N)]
check = [[0] * M for _ in range(N)]
steps = [(0, -1), (1, 0), (0, 1), (-1, 0)]
count = 0


def dfs(y, x, d):
    global count
    if check[y][x] == 1 or mold[y][x] == 1:
        return
    check[y][x] = 1
    for step in steps:
        next_y, next_x = y + step[1], x + step[0]
        if 0 <= next_x < M and 0 <= next_y < N and check[next_y][next_x] == 0 and mold[next_y][next_x] == 0:
            dfs(next_y, next_x, d + 1)
    if d == 0:
        count += 1


for x in range(M):
    for y in range(N):
        dfs(y, x, 0)

print(count)

# Test case 1
# 4 5
# 00110
# 00011
# 11111
# 00000

# Test case 2
# 15 14
# 00000111100000
# 11111101111110
# 11011101101110
# 11011101100000
# 11011111111111
# 11011111111100
# 11000000001111
# 01111111111111
# 00000000011111
# 01111111111000
# 00111111111000
# 00000001111000
# 11111111100011
# 11100011111111
# 11100011111111
