from pprint import pprint
from copy import deepcopy
import sys
sys.setrecursionlimit(10**9)
T = int(input())

dir_x = [-1, 0, 1, 0]
dir_y = [0, 1, 0, -1]


def bt(x, y):
    if check[y][x]:
        return
    check[y][x] = True
    st = []
    for coor in zip(dir_x, dir_y):
        a = x + coor[0]
        b = y + coor[1]
        if a < 0 or b < 0 or a >= M or b >= N:
            continue
        if not farm[b][a]:
            continue
        if not check[b][a]:
            st.append((a, b))
    # print("st : ",st)
    for coor in st:
        bt(coor[0], coor[1])


for _ in range(T):
    M, N, K = map(int, input().split())
    farm = [[0] * M for _ in range(N)]
    check = [[False] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        farm[y][x] = 1
    cnt = 0
    # pprint(farm)
    # pprint(check)
    for y in range(N):
        for x in range(M):
            if farm[y][x] and not check[y][x]:
                cnt += 1
                bt(x, y)
                # pprint(check)
    # print("cnt : ", cnt)
    print(cnt)
    # pprint(copyfarm)
