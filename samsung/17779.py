N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
print(board)


def separating(x, y, d1, d2):
    check = [[0] * N for _ in range(N)]
    for i in range(y, y - d1, -1):
        pass