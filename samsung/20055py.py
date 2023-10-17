import sys
# from time import time
# from random import randint
input = sys.stdin.readline
N, K = map(int, input().split())
q = list(map(int, input().split()))
# q = [1000] * 2 * N
# st = time()

r = [-1] * (2 * N)
s = []
x = 2 * N
robot_id = 0
zero_count = 0


def robot():
    global robot_id, s, zero_count, x
    x -= 1
    x = x % (2 * N)
    # print(x)
    for i in s[:]:
        g = r.index(i)
        rq1 = (g + 1) % (2 * N)
        rq2 = (g) % (2 * N)
        k = 2 * N - x + g + 1 if g - x < 0 else g - x + 1
        # print(g, k)
        if k >= N * 2:
            k = 0
        elif k == N:
            s.remove(i)
            r[rq2] = -1
            continue
        if q[rq1] <= 0 or r[rq1] != -1:
            continue
        elif k == N - 1:
            s.remove(i)
            r[rq2] = -1
            q[rq1] -= 1
            if q[rq1] == 0:
                zero_count += 1
            continue
        r[rq1], r[rq2] = r[rq2], -1
        q[rq1] -= 1
        if q[rq1] == 0:
            zero_count += 1
    if r[x] == -1 and q[x] != 0:
        q[x] -= 1
        if q[x] == 0:
            zero_count += 1
        s.append(robot_id)
        r[x] = robot_id
        robot_id += 1


lvl = 0
while True:
    lvl += 1
    robot()
    # print(lvl, zero_count, q, r, s)
    if zero_count >= K:
        break
# print( time() - st)
print(lvl)