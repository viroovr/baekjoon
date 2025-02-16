"""
이동할 칸이 파랑이거나 바깥일 때, 방향을 바꾸고 반대 칸으로 이동한다는 것을 간과했다.
"""

directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
import sys
input = sys.stdin.readline

def logging(chess_pieces_board):
    for i in range(N):
        print(*chess_pieces_board[i])
    print("=====")

def logging2(chess_pieces):
    directions_string = ["동", "서", "북", "남"]
    for i in range(K):
        r, c, d = chess_pieces[i]
        print(f"{i}:{directions_string[d]}, r{r},c{c}")
    print("=====")

def move_piece(chess_pieces_board, chess_pieces, k, r, c, nr, nc, nd, color):
    before_move_list = chess_pieces_board[r][c]
    ki = before_move_list.index(k)
    moving_pieces_list = before_move_list[ki:]
    if color == 0:
        chess_pieces_board[nr][nc].extend(moving_pieces_list)
    else:
        chess_pieces_board[nr][nc].extend(reversed(moving_pieces_list))
    
    for piece in moving_pieces_list[1:]:
        chess_pieces[piece] = (nr, nc, chess_pieces[piece][2])
    chess_pieces[k] = (nr, nc, nd)
    chess_pieces_board[r][c] = before_move_list[:ki]

    return False if len(chess_pieces_board[nr][nc]) < 4 else True

def get_ending_turn(chess_pieces, chess_pieces_board):
    for t in range(1, 1001):
        for k in range(K):
            r, c, d = chess_pieces[k]
            nr, nc = r + (directions[d])[0], c + (directions[d])[1]
            if not (0 <= nr < N and 0 <= nc < N) or chess_board[nr][nc] == 2:
                d = 1 - d if 0 <= d <= 1 else 5 - d
                nr, nc = r + directions[d][0], c + directions[d][1]
                if not (0 <= nr < N and 0 <= nc < N) or chess_board[nr][nc] == 2:
                    chess_pieces[k] = (r, c, d)
                    continue
            if move_piece(chess_pieces_board, chess_pieces, k, r, c, nr, nc, d, chess_board[nr][nc]):
                return t
    return -1

def sol():
    global N, K, chess_board
    N, K = map(int, input().split())
    chess_board = [list(map(int, input().split())) for _ in range(N)]
    chess_pieces = {}
    chess_pieces_board = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(K):
        r, c, d = map(int, input().split())
        chess_pieces[i] = (r - 1, c - 1, d - 1)
        chess_pieces_board[r - 1][c - 1].append(i)
    print(get_ending_turn(chess_pieces, chess_pieces_board))
sol()