from collections import deque
# N은 세로 M은 가로
N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
# print(N, M, K, board)
direct = [(-1, 0), (0, -1), (1, 0), (0, 1)]
check = [[False] * M for _ in range(N)]
# print(check)
score_board = [[0] * M for _ in range(N)]
# print(score_board)


def bfs(y, x):
    if check[y][x]:
        return
    q = deque()
    rb = board[y][x]
    q.append((y, x))
    score = []
    while q:
        v = q.popleft()
        # print(v, q, v[0], v[1], check[v[0]][v[1]])
        if check[v[0]][v[1]]:
            continue
        score.append(v)
        check[v[0]][v[1]] = True
        # pprint(check)
        for d in direct:
            coor = (v[0] + d[0], v[1] + d[1])
            # print(coor)
            if coor[0] < 0 or coor[0] >= N or coor[1] < 0 or coor[1] >= M or check[coor[0]][coor[1]]:
                continue
            if board[coor[0]][coor[1]] == rb:
                q.append((coor[0], coor[1]))
        # pprint(check)
    if score:
        sc = rb * len(score)
        for v in score:
            score_board[v[0]][v[1]] = sc
        # pprint(score_board)


for i in range(N):
    for j in range(M):
        bfs(i, j)
# pprint(score_board)

dice = [2, 4, 1, 3, 5, 6]


def roll_dice(d):
    y, x = d[0], d[1]
    if x == 0:
        if y == 1:
            dice[0], dice[2], dice[4], dice[-1] = dice[-1], dice[0], dice[2], dice[4]
        else:
            dice[0], dice[2], dice[4], dice[-1] = dice[2], dice[4], dice[-1], dice[0]
    elif x == 1:
        dice[1], dice[2], dice[3], dice[-1] = dice[-1], dice[1], dice[2], dice[3]
    else:
        dice[1], dice[2], dice[3], dice[-1] = dice[2], dice[3], dice[-1], dice[1]


def check_num(cur_num, dice_num):
    if cur_num > dice_num:
        return 1
    elif cur_num < dice_num:
        return -1
    else:
        return 0


total = 0
cur = (0, 0)
k = 3
# direct = [(-1, 0), (0, -1), (1, 0), (0, 1)]
for u in range(K):
    p, q = cur[0] + direct[k][0], cur[1] + direct[k][1]
    if p < 0:
        k = 2
    elif p >= N:
        k = 0
    elif q < 0:
        k = 3
    elif q >= M:
        k = 1
    # temp = cur
    cur = (cur[0] + direct[k][0], cur[1] + direct[k][1])
    roll_dice(direct[k])
    # w = direct[k]
    k = k + check_num(board[cur[0]][cur[1]], dice[-1])

    if k >= 4:
        k = 0
    elif k < 0:
        k = 3
    # print(w, temp, dice, total, u)

    total += score_board[cur[0]][cur[1]]
print(total)
