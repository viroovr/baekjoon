# 구슬 탈출 2
from copy import deepcopy


def is_straight(red_pos, blue_pos, y, x):
    # red_pos (rows, columns), blue_pos (rows, columns)
    if red_pos[0] == blue_pos[0] and x != 0:
        if red_pos[1] < blue_pos[1]:
            return 'R'
        else:
            return 'B'
    elif red_pos[1] == blue_pos[1]:
        if y < 0 and red_pos[0] < blue_pos[0]:
            return 'R'
        else:
            return 'B'


def is_possible(y, x, mark, board, red_pos, blue_pos):
    # if y:
    #     dist = N - red_pos[0]
    # else:
    #     dist = M - red_pos[1]
    # for i in range(dist + 1):
    if board[y][x] == '.' or mark:
        Y = red_pos[0] + y * i
        X = red_pos[1] + x * i
    # else:
    #     return True


def process(board, mark, red_pos, blue_pos):
    # NWSE
    Y = [-1, 0, 1, 0]
    X = [0, -1, 0, 1]
    for i in range(len(Y)):
        if is_possible(Y[i], X[i], mark, board, red_pos, blue_pos):
            go_straight()


def solution():
    # N rows M columns

    global N, M, red_pos, blue_pos, hole, board, ret
    N, M = map(int, input().split())

    board = [list(input()) for _ in range(N)]
    # red_pos (rows, columns), blue_pos (rows, columns)
    for i, x in enumerate(board):
        for j, item in enumerate(x):
            if item == 'R':
                red_pos = (i, j)
            elif item == 'B':
                blue_pos = (i, j)
            elif item == 'O':
                hole = (i, j)
    mark = deepcopy(board)
    process(board, mark, red_pos, blue_pos)
    print(board)


solution()
print(N, M, red_pos, blue_pos, hole)
