import sys
from pprint import pprint
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
# print(N, M)
miro = [[int(i) for i in input().strip()] for _ in range(N)]
# pprint(miro)

check = [[False for _ in range(M)] for _ in range(N)]
# pprint(check)
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(row, col):
    go = deque()
    go.append((row, col, 1))
    check[0][0] = True
    while go:
        y, x, z = go.popleft()
        if y == N-1 and x == M-1:
            print(z)
            break
        # pprint(f"y,x = {y} {x}")
        # pprint(check)
        for i in direction:
            try:
                if miro[y + i[0]][x + i[1]] == 0 or check[y + i[0]][x + i[1]] or y + i[0] < 0 or x + i[1] < 0:
                    continue
                check[y + i[0]][x + i[1]] = True
                go.append((y + i[0], x + i[1], z + 1))
            except IndexError:
                pass
    

bfs(0, 0)
