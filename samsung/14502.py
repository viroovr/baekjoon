from time import time
import sys
from itertools import combinations
from copy import deepcopy
from collections import deque


direct = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def emit(walled_area):
    q = deque(virus)
    while q:
        coor = q.popleft()
        for d in direct:
            v = (coor[0] + d[0], coor[1] + d[1])
            if 0 <= v[0] < N and 0 <= v[1] < M and walled_area[v[0]][v[1]] == 0:
                q.append(v)
                walled_area[v[0]][v[1]] = 2
        if safeNum(walled_area) == 0:
            return 0

    return safeNum(walled_area)


def safeNum(a):
    return sum(row.count(0) for row in a)


input = sys.stdin.readline
N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]
start = time()
# pprint(area)

virus = []
coords = []
for i, v in enumerate(area):
    for k, w in enumerate(v):
        if w == 2:
            virus.append((i, k))
        elif w == 0:
            coords.append((i, k))

count = 0
for i in combinations(coords, 3):
    walled_area = deepcopy(area)
    for k in i:
        walled_area[k[0]][k[1]] = 1
    count = max(count, emit(walled_area))
    # print(i)

print(count)
end = time()
print(end - start)
# bt(0, 0)
# emit()
