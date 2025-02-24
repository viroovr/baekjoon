"""
1. left_walls, right_walls 
    1. 검색 속도 개선
        - 기존 set 방식은 O(1)~O(N) (hash 충돌 발생 가능)
        - 이차원 배열을 활용하면 O(1)로 벽 정보 즉시 조회
    2. 가독성 향상
        - walls[0], walls[1] 대신 right_wall, down_wall을 사용하여 코드 이해가 쉬워짐
    3. 유지보수 용이
        - 벽이 있는지 체크할 때 if not has_wall(r, c, nr, nc):만 사용하면 돼서 로직이 간결해짐
2. edge decrement, 범위 값 하드코딩
3. input
35968	136
35368	132 1, 2
35296	128 1, 2, 3
"""
import sys
from collections import defaultdict
input = sys.stdin.readline
def logging_spread(warmers_with_coords):
    for k, v in warmers_with_coords.items():
        temp_map = [[0] * C for _ in range(R)]
        for s, u in v.items():
            for r, c in u:
                temp_map[r][c] = s
        for row in temp_map:
            print(*row)
        print("++++++++")

def logging_rooms(rooms):
    for row in rooms:
        print(*row)
    print("++++++++")

def has_walls(r, c, nr, nc):
    if r == nr:
        return right_walls[r][min(c, nc)]
    if c == nc:
        return up_walls[max(r, nr)][c]

## t가 0이면 (r,c) (r-1,c), t가 1이면 (r,c) (r,c+1) 벽
directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
def get_spread_coords(cr, cc, d):
    spreading_coords = defaultdict(set)
    dr, dc = directions[d]
    spreading_coords[5].add((cr + dr, cc + dc))

    for i in range(4, 0, -1):
        for r, c in spreading_coords[i + 1]:

            if 0 <= d <= 1 and 0 <= c + dc < C:
                if 0 <= r - 1 and not (has_walls(r, c, r - 1, c) or has_walls(r - 1, c, r - 1, c + dc)):
                    spreading_coords[i].add((r - 1, c + dc))
                if not (has_walls(r, c, r, c + dc)):
                    spreading_coords[i].add((r, c + dc))
                if r + 1 < R and not (has_walls(r, c, r + 1, c) or has_walls(r + 1, c, r + 1, c + dc)):
                    spreading_coords[i].add((r + 1, c + dc))

            elif 2 <= d <= 3 and 0 <= r + dr < R:
                if 0 <= c - 1 and not (has_walls(r, c, r, c - 1) or has_walls(r, c - 1, r + dr, c - 1)):
                    spreading_coords[i].add((r + dr, c - 1))
                if not (has_walls(r, c, r + dr, c)):
                    spreading_coords[i].add((r + dr, c))
                if c + 1 < C and not (has_walls(r, c, r, c + 1) or has_walls(r, c + 1, r + dr, c + 1)):
                    spreading_coords[i].add((r + dr, c + 1))
                
    return spreading_coords

def adjust_temp(rooms):
    deltas = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if rooms[r][c] == 0:
                continue
            cur_temp = rooms[r][c]
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < R and 0 <= nc < C and rooms[nr][nc] < cur_temp:
                    if not has_walls(r, c, nr, nc):
                        delta = (cur_temp - rooms[nr][nc]) // 4
                        deltas[nr][nc] += delta
                        deltas[r][c] -= delta

    for r in range(R):
        for c in range(C):
            rooms[r][c] += deltas[r][c]

def edge_decrement(rooms):
    for r in [0, R - 1]:
            for c in range(1, C - 1):
                if rooms[r][c] > 0:
                    rooms[r][c] -= 1
    for c in [0, C - 1]:
        for r in range(1, R - 1):
            if rooms[r][c] > 0:
                rooms[r][c] -= 1

    for r in [0, R - 1]:
        for c in [0, C - 1]:
            if rooms[r][c] > 0:
                rooms[r][c] -= 1

def get_chocolate_amount(rooms):
    warmers_with_coords = {(r, c): get_spread_coords(r, c, i) for i in range(4) for r, c in warmers[i]}

    for eat in range(1, 101):
        for warmer_coord, temp_spread_coords_dict in warmers_with_coords.items():
            for temp, coords in temp_spread_coords_dict.items():
                for r, c in coords:
                    rooms[r][c] += temp

        adjust_temp(rooms)

        edge_decrement(rooms)

        if all(rooms[r][c] >= K for r, c in inspect_grid):
            return eat
    return 101

def sol():
    global R, C, K, W, warmers, inspect_grid, right_walls, up_walls
    R, C, K = map(int, input().split())
    rooms = [list(map(int, input().split())) for _ in range(R)]
    W = int(input())
    right_walls = [[False] * C for _ in range(R)]
    up_walls = [[False] * C for _ in range(R)]
    for _ in range(W):
        x, y, t = map(int, input().split())
        if t == 0:
            up_walls[x - 1][y - 1] = True
        elif t == 1:
            right_walls[x - 1][y - 1] = True

    warmers = [[] for _ in range(4)]
    inspect_grid = []
    for r in range(R):
        for c in range(C):
            if rooms[r][c] == 0:
                continue
            elif 1 <= rooms[r][c] <= 4:
                warmers[rooms[r][c] - 1].append((r, c))
            elif rooms[r][c] == 5:
                inspect_grid.append((r, c))
            rooms[r][c] = 0
    
    print(get_chocolate_amount(rooms))

sol()

