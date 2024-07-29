from collections import deque

N, M = map(int, input().split())
miro = [list(map(int, input())) for _ in range(N)]
check = [[0] * M for _ in range(N)]
steps = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def bfs():
    count = 200 ** 2
    q = deque()
    q.append((0, 0, 1))
    while q:
        print(q)
        y, x, depth = q.popleft()
        check[y][x] = 1
        for step in steps:
            next_y, next_x = y + step[1], x + step[0]
            if 0 <= next_y < N and 0 <= next_x < M and miro[next_y][next_x] == 1 and check[next_y][next_x] == 0:
                if next_y == N - 1 and next_x == M - 1:
                    count = min(depth + 1, count)
                else:
                    q.append((next_y, next_x, depth + 1))
    print(count)


bfs()

# Test case 1
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111
# > 10
