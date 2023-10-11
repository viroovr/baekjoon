# from pprint import pprint


def tornado(dr, n):
    global cur
    if dr[1]:
        drc = {
            1: [(-1, -dr[1]), (1, -dr[1])],
            2: [(-2, 0), (2, 0)],
            5: [(0, dr[1] * 2)],
            7: [(-1, 0), (1, 0)],
            10: [(-1, dr[1]), (1, dr[1])],
            65: [(0, dr[1])],
        }
    else:
        drc = {
            1: [(-dr[0], -1), (-dr[0], 1)],
            2: [(0, -2), (0, 2)],
            5: [(2 * dr[0], 0)],
            7: [(0, -1), (0, 1)],
            10: [(dr[0], -1), (dr[0], 1)],
            65: [(dr[0], 0)],
        }
    out = 0
    for _ in range(n):
        cur = (cur[0] + dr[0], cur[1] + dr[1])
        # print(n, cur)
        tot = 0
        for i, v in drc.items():
            if i == 65:
                j = sand[cur[0]][cur[1]] - tot
            else:
                j = int(sand[cur[0]][cur[1]] * (0.01 * i))
            # print(i, v, tot, j)
            for k in v:
                tot += j
                coor = (cur[0] + k[0], cur[1] + k[1])
                if coor[0] < 0 or coor[0] >= N or coor[1] < 0 or coor[1] >= N:
                    out += j
                    continue
                sand[coor[0]][coor[1]] += j
        sand[cur[0]][cur[1]] = 0
        # pprint(sand)
    return out


N = int(input())
sand = [list(map(int, input().split())) for _ in range(N)]
direct = [(0, -1), (1, 0), (0, 1), (-1, 0)]
cur = (N // 2, N // 2)
# print("origin cur", cur)
out = 0
t = 0
for i in range(1, N):
    if i == N - 1:
        for k in range(3):
            j1 = direct[t]
            t += 1
            if t > 3:
                t = 0
            out += tornado(j1, i)
            # print("out", out)

    else:
        for k in range(2):
            j1 = direct[t]
            t += 1
            if t > 3:
                t = 0
            # print("out", out)
            out += tornado(j1, i)
print(out)
