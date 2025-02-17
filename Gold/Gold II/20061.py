"""
연속된 두개 이상 행 또는 열이 사라질 때, 한개씩 복사처리해서 제거되지 않는 문제해결
-> while문
1. input = sys.stdin.readline일때, 시간 단축. (sys 못쓰면 의미없음)
2. map(sum, board)로 가독성 및 계산 속도 증가
3. pop, insert 내장 함수 사용
33432	320 2,3
33432	68  1,2,3
"""
import sys
input = sys.stdin.readline
def logging(board):
    for row in board:
        print(*row)
    print("===========")
    
def move_block(t, x, board):
    score = 0
    if t == 1:
        for y in range(1, 5):
            if board[y + 1][x]:
                board[y][x] = 1
                break
        else:
            board[5][x] = 1
    elif t == 2:
        for y in range(1, 5):
            if board[y + 1][x] or board[y + 1][x + 1]:
                board[y][x], board[y][x + 1] = 1, 1
                break
        else:
            board[5][x], board[5][x + 1] = 1, 1
    elif t == 3:
        for y in range(4):
            if board[y + 2][x]:
                board[y][x], board[y + 1][x] = 1 , 1
                break
        else:
            board[4][x], board[5][x] = 1 , 1
    
    for i in range(5, 1, -1):
        while sum(board[i]) == 4:
            score += 1
            board.pop(i)
            board.insert(0, [0] * 4)

    for i in range(2):
        if sum(board[i]) > 0:
            board.pop()
            board.insert(0, [0] * 4)

    return score

def get_scores(N, blocks, green_board, blue_board):
    score = 0
    for t, x, y in blocks:
        x, y = y, x
        score += move_block(t, x, green_board)

        score += move_block(
            t if t == 1 else 5 - t,
            3 - (y + 1) if t == 3 else 3 - y,
            blue_board
        )
    return score

def get_gb_tiles_cnt(green_board, blue_board):
    return sum(map(sum, green_board)) + sum(map(sum, blue_board))

def sol():
    N = int(input())
    blocks = [tuple(map(int, input().split())) for _ in range(N)]
    green_board = [[0] * 4 for _ in range(6)]
    blue_board = [[0] * 4 for _ in range(6)]
    print(get_scores(N, blocks, green_board, blue_board))
    print(get_gb_tiles_cnt(green_board, blue_board))
sol()