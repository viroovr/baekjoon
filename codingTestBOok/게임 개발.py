N, M = map(int, input().split())
B, A, d = map(int, input().split())
minimap = [list(map(int, input().split())) for _ in range(N)]
check = [[False for _ in range(M)] for _ in range(N)]

steps = [(0, -1), (1, 0), (0, 1), (-1, 0)]
count = 1
while True:
    for i in range(4):
        d %= 4
        next_x = steps[d][0] + A
        next_y = steps[d][1] + B
        d += 1
        if 0 <= next_x < M and 0 <= next_y < N and minimap[next_y][next_x] == 0 and not check[next_y][next_x]:
            check[B][A] = True
            A = next_x
            B = next_y
            count += 1
            break
    else:
        d = (d + 2) % 4
        next_x = steps[d][0] + A
        next_y = steps[d][1] + B
        if 0 <= next_x < M and 0 <= next_y < N and minimap[next_y][next_x] == 0:
            A = next_x
            B = next_y
            count += 1
        else:
            break

print(count)
