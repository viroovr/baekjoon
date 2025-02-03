ewns = [(0, 1), (0, -1), (-1, 0), (1, 0)]
dice = [1, 5, 3]
mapDice = {i : 0 for i in range(1, 7)}

def roll_dice(direction):
    """주어진 방향으로 주사위 굴리기. 정육면체의 위, 앞, 오른면 순"""
    global dice
    if direction == 0:
        dice[0], dice[2] = dice[2], 7 - dice[0]
    elif direction == 1:
        dice[0], dice[2] = 7 - dice[2], dice[0]
    elif direction == 2:
        dice[0], dice[1] = dice[1], 7 - dice[0]
    else:
        dice[0], dice[1] = 7 - dice[1], dice[0]

def move(n, m, x, y, board, direction, i):
    """이동 및 주사위 값 갱신"""
    dx, dy = ewns[direction[i]]
    curx, cury = x + dx, y + dy

    if 0 <= curx < n and 0 <= cury < m:
        roll_dice(direction[i])
        bottom = 7 - dice[0]

        if board[curx][cury] == 0:
            board[curx][cury] = mapDice[bottom]
        else:
            mapDice[bottom] = board[curx][cury]
            board[curx][cury] = 0
        
        return curx, cury, mapDice[dice[0]]
    return -1, -1, -1


def sol():
    n, m, x, y, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    direction = list(map(lambda x: int(x) - 1, input().split()))
    for i in range(k):
        dx, dy, top_value = move(n, m, x, y, board, direction, i)
        if top_value != -1:
            x, y = dx, dy
            print(top_value)

def test_fun():
    pass

if __name__ == "__main__":
    test = 0
    if test == 1:
        test_fun()
    else:
        sol()
