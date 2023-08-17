from pprint import pprint

N, M = map(int, input().split())
board = [input() for _ in range(N)]
b = [[0] * M for _ in range(N)]
w = [[0] * M for _ in range(N)]
"""
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
one : W: 4 B: 4
total : 32 / 32
43 * 43 * 64
"""

# print(board, b, w)


def check(st, end, mat):
    """
    st = B, end = W mat = B
    BWBWBWBW
    WBWBWBWB
    BWBWBWBW
    WBWBWBWB
    BWBWBWBW
    WBWBWBWB
    BWBWBWBW
    WBWBWBWB
    Args:
        st (_type_): _description_
        end (_type_): _description_
        mat (_type_): _description_
    """
    def xline(st, end, mat):
        for x in range(0, M, 2):
            if board[y][x] == end:
                mat[y][x] = 1
        for x in range(1, M, 2):
            if board[y][x] == st:
                mat[y][x] = 1

    for y in range(0, N, 2):
        xline(st, end, mat)
    for y in range(1, N, 2):
        xline(end, st, mat)


def mincheck(mat):
    global M, N
    ret = 64
    for j in range(N - 8 + 1):
        for i in range(M - 8 + 1):
            k = sum((sum(mat[u][i: i + 8]) for u in range(j, j + 8)))
            if k < ret:
                ret = k
    return ret

check("B", "W", b)
check("W", "B", w)
# pprint(b)
# pprint(w)

print(min(mincheck(b), mincheck(w)))
