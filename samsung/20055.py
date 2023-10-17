import sys
from copy import deepcopy
# from time import time
# from random import randint
input = sys.stdin.readline
N, K = map(int, input().split())
q = list(map(int, input().split()))
q.insert(0, 1)
r = [-1] * (2 * N)
s = []


def rotate_robot_index():
    global s, r, q
    n = q.pop()
    q.insert(1, n)

    new_index = []
    r = [-1] * (2 * N)
    for i in s:
        new = i + 1
        if new < N:
            new_index.append(new)
            r[new] = 0
    s = deepcopy(new_index)


def robot():
    global robot_id, s
    rotate_robot_index()

    new_index = []
    for i in s:
        next_index = i + 1
        if r[next_index] == 0 or q[next_index] < 1:
            new_index.append(i)
        else:
            q[next_index] -= 1
            r[i] = -1
            if next_index != N:
                new_index.append(next_index)
                r[next_index] = 0
    s = deepcopy(new_index)

    if q[1] != 0:
        s.append(1)
        q[1] -= 1
        r[1] = 0


def is_finish():
    return q.count(0) >= K


lvl = 0
while not is_finish():
    lvl += 1
    robot()
print(lvl)
