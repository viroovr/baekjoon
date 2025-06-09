"""
시간을 1씩 더하며 진행상태를 만들었지만,
규칙이 있음을 알았다.

"""
import sys
input = sys.stdin.readline


def bomb(R, C, board):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    new_board = [["O"] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if board[r][c] == "O":
                new_board[r][c] = "."
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C:
                        new_board[nr][nc] = "."
    
    return new_board

def get_grids(R, C, N, board):
    if N == 1:
        for row in board:
            print("".join(row))
    elif N % 2 == 0:
        for _ in range(R):
            print("O" * C)
    else:
        after_bomb = bomb(R, C, board)
        if N % 4 == 3:
            for row in after_bomb:
                print("".join(row))
        else:
            after_second_bomb = bomb(R, C, after_bomb)
            for row in after_second_bomb:
                print("".join(row))

def sol():
    R, C, N = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(R)]

    get_grids(R, C, N, board)

sol()