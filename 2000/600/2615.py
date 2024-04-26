num = 19


def board_input():
    return [list(input().split()) for _ in range(num)]


def checking_condition(board, mark, y, x):
    return board[y][x] == '0'


def check_winning(board, mark, y, x):
    if checking_condition(board, mark, y, x):
        return 0
    Y = [1, 1, 0, -1]
    X = [0, 1, 1, 1]
    for index, (j, i) in enumerate(zip(Y, X)):
        mark[y][x][index] = True
        cnt = directing(board, mark, y, x, i, j, index, 1)
        # print("x, y: ", x, y, " index :", index, " cnt :", cnt)
        if cnt == 5:
            return (y, x, i, j)
    else:
        return 0


def is_in_board(x, y):
    return 0 <= x < num and 0 <= y < num


def directing(board, mark, y, x, i, j, index, count):
    x1, y1 = x + i * count, y + j * count
    # print("y, x, y1, x1, count", y, x, y1, x1, count)
    # if count <= 0:
    #     return 0
    if not is_in_board(x1, y1):
        return count
    if board[y][x] == board[y1][x1]:
        if mark[y1][x1][index]:
            return count
        mark[y1][x1][index] = True
        return directing(board, mark, y, x, i, j, index, count + 1)
    else:
        return count


def judge_winner(board):
    # mark = (아래, 대각, 오른)
    mark = [[[False] * 4 for _ in range(num)] for _ in range(num)]
    for x in range(num):
        for y in range(num):
            # print("=================y,x: ", y, x)
            cond = check_winning(board, mark, y, x)
            if cond == 0:
                continue
            return cond
    else:
        return -1


def print_winner(board, cond):
    if cond == -1:
        print(0)
        return
    who_win = board[cond[0]][cond[1]]
    print(who_win)
    print(cond[0] + 1, cond[1] + 1)


def main():
    board = board_input()
    print_winner(board, judge_winner(board))
    # print(board)


main()
