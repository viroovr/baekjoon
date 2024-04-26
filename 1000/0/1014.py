# import sys
# from collections import deque
# from pprint import pprint
# input = sys.stdin.readline

# direct = [(-1, 1), (-1, 0), (1, 1), (1, 0)]
# notdirect = [(-1, -1), (-1, 0), (1, -1), (1, 0)]


# def bfs(x, y):
#     global ans
#     # q = deque()
#     # q.append((x, y))
#     # while q:
#         # x, y = q.popleft()
#         # mark[y][x] = True
#         # ans += 1
#         # if y + 1 >= N:
#         #     continue
#         # if not mark[y + 1][x] and sit[y + 1][x]:
#             # q.append((x, y + 1))
#     mark[y][x] = True
#     ans += 1
# # 10 10
# # ....x.....
# # ..........
# # ..........
# # ..x.......
# # ..........
# # x...x.x...
# # .........x
# # ...x......
# # ........x.
# # .x...x....

# def isPossible(x, y):
#     if not sit[y][x] or mark[y][x]:
#         return False
#     for coor in notdirect:
#         a, b = x + coor[0], y + coor[1]
#         if a >= M or a < 0 or b >= N or b < 0:
#             continue
#         if mark[b][a]:
#             return False
#     return True


# C = int(input())
# for _ in range(C):
#     N, M = map(int, input().split())
#     sit = [[True] * M for _ in range(N)]
#     mark = [[False] * M for _ in range(N)]
#     ans = 0
#     for i in range(N):
#         for j, x in enumerate(input()):
#             if x == 'x':
#                 sit[i][j] = False
#     # print(sit)
#     # pprint(sit)
#     for i in range(M):
#         for j in range(N):
#             if isPossible(i, j):
#                 # print("### start ###")
#                 # print(f"i, j {i}, {j}")
#                 # pprint(mark)
#                 # print(ans)
#                 bfs(i, j)
#                 # pprint(mark)
#                 # print(ans)
#                 # print("### end ###")
#     # pprint(mark)
#     mark = [[False] * M for _ in range(N)]
#     even_ans = ans
#     ans = 0
#     for j in range(N):
#         for i in range(1, M):
#             if isPossible(i, j):
#                 bfs(i, j)
    
#     # pprint(mark)
#     # print(even_ans, ans)
#     print(max(even_ans, ans))
import sys
from collections import deque
from pprint import pprint
input = sys.stdin.readline

notdirect = [(-1, -1), (-1, 0), (1, -1), (1, 0), (1, 1), (-1, 1)]


def marking(x, y):
    global ans
    mark[y][x] = True
    ans += 1

def isPossible(x, y):
    if not sit[y][x] or mark[y][x]:
        return False
    for coor in notdirect:
        a, b = x + coor[0], y + coor[1]
        if a >= M or a < 0 or b >= N or b < 0:
            continue
        if mark[b][a]:
            return False
    return True


C = int(input())
for _ in range(C):
    N, M = map(int, input().split())
    ans_sheet = []
    sit = [[True] * M for _ in range(N)]
    mark = [[False] * M for _ in range(N)]
    ans = 0
    for i in range(N):
        for j, x in enumerate(input()):
            if x == 'x':
                sit[i][j] = False

    for i in range(M):
        for j in range(N):
            if isPossible(i, j):
                marking(i, j)
    ans_sheet.append(ans)

    mark = [[False] * M for _ in range(N)]
    ans = 0
    for j in range(N):
        for i in range(1, M):
            if isPossible(i, j):
                marking(i, j)
    ans_sheet.append(ans)

    mark = [[False] * M for _ in range(N)]
    ans = 0
    for j in range(N):
        for i in range(M-1, 0, -1):
            if isPossible(i, j):
                marking(i, j)
    ans_sheet.append(ans)

    mark = [[False] * M for _ in range(N)]
    ans = 0
    for j in range(N):
        for i in range(M - 2, 0, -1):
            if isPossible(i, j):
                marking(i, j)
    ans_sheet.append(ans)

    print(ans_sheet, max(ans_sheet))