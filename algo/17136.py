# from sys import stdin
# from copy import deepcopy
# from pprint import pprint
# input = stdin.readline
# NUM = 10
# board = []
# for _ in range(NUM):
#     board.append(list(map(int, input().split())))

# # print(board)
# # 0 0 0 0 0 0 0 0 0 0
# # 0 1 1 0 0 0 0 0 0 0
# # 0 1 1 1 0 0 0 0 0 0
# # 0 0 1 1 1 1 1 0 0 0
# # 0 0 0 1 1 1 1 0 0 0
# # 0 0 0 0 1 1 1 0 0 0
# # 0 0 1 0 0 0 0 0 0 0
# # 0 0 0 0 0 0 0 0 0 0
# # 0 0 0 0 0 0 0 0 0 0
# # 0 0 0 0 0 0 0 0 0 0
# dp_table = []
# usage = [0] * 5


# def update_dptable():
#     global dp_table, board
#     dp_table = deepcopy(board)
#     for i in range(1, NUM):
#         for j in range(1, NUM):
#             if board[i][j] == 0:
#                 dp_table[i][j] = 0
#             else:
#                 dp_table[i][j] = min(dp_table[i - 1][j - 1],
#                                      dp_table[i - 1][j], dp_table[i][j - 1]) + 1
#     dp_table = [list(reversed(dp_table[i])) for i in range(NUM)]


# def mask_board(n, i, j):
#     global board
#     # print(f"n, i, j : {n}, {i}, {j}")
#     for y in range(i, i - n, -1):
#         for x in range(NUM - j - 1, NUM - 1 - j - n, -1):
#             board[y][x] = 0


# def update_usage(n):
#     global usage
#     usage[n - 1] += 1
#     return usage[n - 1] <= 5


# def maxnum():
#     global dp_table, NUM
#     ma, p, q = 0, 0, 0
#     for i in range(NUM):
#         for j in range(NUM):
#             if dp_table[i][j] > ma:
#                 ma = dp_table[i][j]
#                 p = i
#                 q = j
#     return ma, p, q


# # print("prev")
# # pprint(dp_table)
# update_dptable()

# # print("next")
# # pprint(dp_table)


# def main():
#     global dp_table, usage, NUM
#     while True:
#         ma, p, q = maxnum()
#         if ma == 0:
#             break
#         else:
#             n = min(ma, 5)
#             mask_board(n, p, q)
#             # print("board")
#             # pprint(board)
#             if not update_usage(n):
#                 return -1
#             update_dptable()
#             # print("dp_table")
#             # pprint(dp_table)
#             # pprint(usage)
#     return sum(usage)


# print(main())
# # pprint(dp_table)

# # 0 0 0 0 0 0 0 0 0 0
# # 0 1 1 0 0 0 0 0 0 0
# # 0 1 2 1 0 0 0 0 0 0
# # 0 0 1 2 1 1 1 0 0 0
# # 0 0 0 1 2 2 2 0 0 0
# # 0 0 0 0 1 2 3 0 0 0
# # 0 0 1 0 0 0 0 0 0 0
# # 0 0 0 0 0 0 0 0 0 0
# # 0 0 0 0 0 0 0 0 0 0
# # 0 0 0 0 0 0 0 0 0 0

board = [list(map(int, input().split())) for _ in range(10)]
ans = 25
paper = [0] * 6


def is_possible(y, x, sz):
    if paper[sz] == 5:
        return False

    if y + sz > 10 or x + sz > 10:
        return False

    for i in range(sz):
        for j in range(sz):
            if board[y + i][x + j] == 0:
                return False
    return True


def mark(y, x, sz, v):
    for i in range(sz):
        for j in range(sz):
            board[y + i][x + j] = v

    if v:
        paper[sz] -= 1
    else:
        paper[sz] += 1


def backtracking(y, x):
    global ans
    if y == 10:
        ans = min(ans, sum(paper))
        return

    if x == 10:
        backtracking(y + 1, 0)
        return
    # print(y, x)
    if board[y][x] == 0:
        backtracking(y, x + 1)
        return

    for sz in range(1, 6):
        if is_possible(y, x, sz):
            mark(y, x, sz, 0)
            backtracking(y, x + 1)
            mark(y, x, sz, 1)


backtracking(0, 0)
print(-1 if ans == 25 else ans)
