from copy import deepcopy
import sys
sys.setrecursionlimit(10 ** 8)
N = 4
board = [list(map(int, input().split())) for _ in range(N)]
number = [board[n][0::2] for n in range(N)]
direct = [board[n][1::2] for n in range(N)]
# print(number, "\n", direct)
direction = [0, (-1, 0), (-1, -1), (0, -1), (1, -1),
             (1, 0), (1, 1), (0, 1), (-1, 1)]


def find_fish(number, n):
    for i in range(N):
        try:
            x = number[i].index(n)
            y = i
            return (y, x)
        except ValueError:
            continue
    return -1


def fish_sort(number, direct):
    for i in range(1, N * N + 1):
        cur = find_fish(number, i)
        if cur == -1:
            continue
        k = direct[cur[0]][cur[1]]
        # print(i, cur, k)
        for j in range(8):
            t = k + j
            if t >= len(direction):
                t = t - len(direction) + 1
            y, x = cur[0] + direction[t][0], cur[1] + direction[t][1]
            if y < 0 or y >= N or x < 0 or x >= N or number[y][x] == -1:
                # print(y, x)
                continue
            # print(f"y, x ({y}, {x})")
            number[cur[0]][cur[1]
                           ], number[y][x] = number[y][x], number[cur[0]][cur[1]]
            direct[cur[0]][cur[1]], direct[y][x] = direct[y][x], t
            break
        # print(f"number is {number}")
        # print(f"direct is {direct}")


def shark_move(v):
    global global_total
    number, direct, shark, total = v
    if total == 0:
        # print(f"eaten fish = {number[shark[0]][shark[1]]}")
        total = total + number[shark[0]][shark[1]]
        number[shark[0]][shark[1]] = -1
        fish_sort(number, direct)
        return total
    k = direct[shark[0]][shark[1]]
    # print(f" shark {shark}, total {total} k {k}")
    eaten_fish = 0
    for c in range(1, N):
        n1 = deepcopy(number)
        d1 = deepcopy(direct)
        temp = total
        y, x = shark[0] + direction[k][0] * \
            c, shark[1] + direction[k][1] * c
        if y < 0 or y >= N or x < 0 or x >= N:
            break
        elif n1[y][x] == 0:
            continue
        eaten_fish = n1[y][x]
        # print(f"eaten fish = {eaten_fish}")
        n1[shark[0]][shark[1]], n1[y][x] = 0, -1
        d1[shark[0]][shark[1]] = 0
        # print(f"after shark n1 is {n1}")
        # print(f"after shark d1 is {d1}")
        fish_sort(n1, d1)
        temp = shark_move(
            (n1, d1, (y, x), temp + eaten_fish))
        global_total = max(global_total, temp)

    # print("shark moving done")
    return total


global_total = 0
global_total = shark_move((number, direct, (0, 0), global_total))
shark_move((number, direct, (0, 0), global_total))
print(global_total)
