from collections import deque
from sys import stdin

input = stdin.readline


def in_mine(y, x):
    return 0 <= y < R and 0 <= x < C


def is_one(y, x):
    return mine[y][x] == '1'


def bfs(y, x, direct):
    if not is_one(y, x):
        return 0
    q = deque()
    q.append((y, x, -1, 1))
    ret = 0
    flag = False
    while q:
        y, x, direct, num = q[-1]

        if not flag and direct == -1:
            y1, y2 = y + 1, y + 1
            x1, x2 = x - 1, x - 1 + 2 * num
            if in_mine(y1, x1) and is_one(y1, x1) and in_mine(y2, x2) and is_one(y2, x2):
                q.append((y1, x1, direct, num + 1))
            else:
                ret = num
                flag = True
                # print(q)
                q.append((y, x, -direct, num))
        elif flag:
            y, x, direct, num = q.pop()
            # print(y, x, direct, num, ret)
            # print(q)
            y1, y2 = y + 1, y + 1
            x1, x2 = x + 1, x + 1 + 2 * (num - len(q))
            if in_mine(y1, x1) and is_one(y1, x1) and in_mine(y2, x2) and is_one(y2, x2):
                if x1 == x2:
                    return num
                q.append((y1, x1, direct, num - 1))
            else:
                ret = num
    return ret


ret = 0
R, C = map(int, input().split())
mine = [input() for _ in range(R)]
for y in range(R):
    for x in range(C):
        # print("y, x", y, x)
        ret = max(ret, bfs(y, x, 0))
print(ret)
