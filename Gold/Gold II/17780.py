"""
처음에는 예전 풀이의 움직이려는 말을 기준으로 그 위에 말들과 함께 이동하는 줄
알았지만, 맨 아래만 움직이는 것이었다.
그리고 움직이려는 말이 있는 곳에 맨 아래 말이 움직이려는 것인줄 알았지만
움직이려는 말이 맨 아래 있지 않다면 아무 행동도 하지 않는 것이다.

예전 기억대로 바로 접근하려 한게 문제였다. 그림을 보고 상황을 제대로 파악한 뒤
풀어야 겠다.

32412	44
"""
def play_game(N, K, board, pieces, pos):

    def isin(r, c):
        return 0 <= r < N and 0 <= c < N
    
    def set_pos(lis, r, c):
        for i in lis:
            pos[i] = (r, c, pos[i][2])
            
    def blue(i, pr, pc, pd):
        ipd = pd ^ 1
        inr, inc = pr + directions[ipd][0], pc + directions[ipd][1]
        pos[i] = (pr, pc, ipd)
        if isin(inr, inc) and board[inr][inc] != 2:
            move(i, pr, pc, ipd)

    def move(i, pr, pc, pd):
        nr, nc = pr + directions[pd][0], pc + directions[pd][1]
        lis = pieces[pr][pc]
        if 0 <= nr < N and 0 <= nc < N:
            if board[nr][nc] == 0:
                set_pos(lis, nr, nc)
                pieces[nr][nc].extend(lis)
                pieces[pr][pc].clear()
            elif board[nr][nc] == 1:
                set_pos(lis, nr, nc)
                pieces[nr][nc].extend(reversed(lis))
                pieces[pr][pc].clear()
            else:
                blue(i, pr, pc, pd)
        else:
            blue(i, pr, pc, pd)
    
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    for turn in range(1, 1001):
        for i in range(K):
            pr, pc, pd = pos[i]
            if i != pieces[pr][pc][0]:
                continue
            move(i, pr, pc, pd)
            nr, nc, _ = pos[i]
            if len(pieces[nr][nc]) >= 4:
                return turn
    return -1

def sol():
    N, K = map(int, input().split())
    board = [tuple(map(int, input().split())) for _ in range(N)]
    pieces = [[[] for _ in range(N)] for _ in range(N)]
    pos = [0] * K
    for i in range(K):
        r, c, d = map(int, input().split())
        pieces[r - 1][c - 1].append(i)
        pos[i] = (r - 1, c - 1, d - 1)
    
    print(play_game(N, K, board, pieces, pos))

sol()
