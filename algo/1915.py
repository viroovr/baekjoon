# 5 5
# 01001
# 01111
# 11111
# 00111
# 11111
# 10 10
# 0000000000
# 0000000000
# 0000000000
# 0000000000
# 0000000000
# 0000000000
# 0000000000
# 0000000000
# 0000000000
# 0000000001
# 1^2 * 5^2
# 2^2 * 4^2
# 3^2 * 3^2
# print(sum(n ** 2 * (1000-n) ** 2 for n in range(1, 1001)))
# from sys import stdin
# input = stdin.readline
# n, m = map(int, input().split())
# board = []

# for i in range(n):
#     board.append({j for j, x in enumerate(map(int, list(input().strip()))) if x == 1})
#     # print(board)

# # print(board)

# def is_adjacent(q, k):
#     q = list(q)
#     for i in range(len(q) - k + 1):
#         end = False
#         for j in range(i, i + k - 1):
#             if q[j + 1] - q[j] != 1:
#                 end = True
#                 break
#         if not end:
#             return True
#     return False

# def get_num():
#     global board
#     for k in range(n, 0, -1):
#         for i in range(0, n - k + 1):
#             q = board[i]
#             if not q:
#                 continue
#             for j in range(i, i + k):
#                 q = q.intersection(board[j])
#             # print(f"k {k} q {q}")
#             if len(q) >= k and is_adjacent(q, k):
#                 return k
#     return 0

# print(get_num() ** 2)

# 5 5
# 01001
# 01111
# 11111
# 00111
# 11111
# 0 1 0 0 1
# 0 1 1 1 1
# 1 1 2 2 2
# 0 0 1 2 3
# 1 1 1 2 3
from sys import stdin
from copy import deepcopy
input = stdin.readline
n, m = map(int, input().split())
board = [[int(i) for i in input().strip()] for _ in range(n)]
# print(board)

dp_table = deepcopy(board)
for row in range(1, n):
    for col in range(1, m):
        if dp_table[row][col] == 1:
            dp_table[row][col] = min(
                dp_table[row - 1][col - 1], dp_table[row - 1][col], dp_table[row][col - 1]) + 1
        else:
            dp_table[row][col] = 0
print(max(dp_table[i][j] for i in range(n) for j in range(m)) ** 2)
