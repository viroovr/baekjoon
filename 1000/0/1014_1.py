from pprint import pprint
from copy import deepcopy
from itertools import combinations
import sys
input = sys.stdin.readline
M, N = 0, 0


def process_seats():
    # M rows N Colummns
    return [list(x for x in input().strip()) for _ in range(M)]


def get_possible_row(modified_seats, y):
    t = [x for x in range(N) if modified_seats[y][x] == '.']
    row_list = []
    for i in range(len(t) // 2, len(t) + 1):
        for k in combinations(t, i):
            li = modified_seats[y][:]
            for u in k:
                if is_possible_seat(modified_seats, y, u):
                    modified_seats[y][u] = 1
                else:
                    break
            else:
                row_list.append(modified_seats[y][:])
            modified_seats[y] = li
    return row_list


ret = 0


def solve_seats(seats, y):
    global ret
    if y >= M:
        return
    modified_seats = deepcopy(seats)
    pprint(modified_seats)
    row_list = get_possible_row(modified_seats, y)
    # pprint(row_list)
    for k in row_list:
        modified_seats[y] = k
        solve_seats(modified_seats, y + 1)
    ret = max(ret, sum(modified_seats[i].count(1) for i in range(M)))
    # k = sum(modified_seats[i].count(1) for i in range(M))
    # if k > ret:
    #     # pprint(modified_seats)
    #     ret = k
    # modified_seats = deepcopy(seats)
    # # print(y, x, "end")


def is_possible_seat(seats, y, x):

    Y = [y - 1, y, y - 1, y]
    X = [x - 1, x - 1, x + 1, x + 1]
    for i in range(4):
        if (Y[i] >= 0 and X[i] >= 0) and (Y[i] < M and X[i] < N):
            if seats[Y[i]][X[i]] == 1:
                return False
    return True


# def bt(seats, y, x):
#     if y >= M or x >= N:
#         return
#     if is_possible_seat(seats, y, x):
#         seats[y][x] = 1

#     if x == N - 1:
#         bt(seats, y + 1, 0)
#     bt(seats, y, x + 1)


def solution():
    global M, N, ret
    C = int(input())
    for _ in range(C):
        # print("M, N Start=====================")
        ret = 0
        M, N = map(int, input().split())
        seats = process_seats()
        solve_seats(seats, 0)
        print(ret)
        # print("M, N End=====================")


solution()
