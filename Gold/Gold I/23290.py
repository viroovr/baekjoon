"""
1. new_fish_sea를 global로 선언해서 backtracking하기
2. new_fish.pop((r,c,d), None) 사용하기
35100	72  2
35084	68  1,2
35084	68  1
35084	64
"""
from collections import defaultdict
directions = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
shark_directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def get_max_eating(r, c, d, cnt, movings, new_fish_sea):
    global max_cnt, max_movings
    if max_cnt > cnt + (3 - d) * 1000000:
        return
    if d == 3:
        if max_cnt < cnt:
            max_cnt = cnt
            max_movings = movings[:]
        return

    for dr, dc in shark_directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N:
            t = new_fish_sea[nr][nc]
            new_fish_sea[nr][nc] = 0
            movings.append((nr, nc))
            get_max_eating(nr, nc, d + 1, cnt + t, movings, new_fish_sea)
            movings.pop()
            new_fish_sea[nr][nc] = t

def get_fishes_count(fishes, sharks):
    global max_cnt, max_movings
    smells = [[-1] * N for _ in range(N)]
    for s in range(1, S + 1):
        new_fish_sea = [[0] * N for _ in range(N)]
        new_fishes = defaultdict(int)
        for (r, c, d), v in fishes.items():
            for i in range(8):
                dr, dc = directions[d - i]
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and (nr, nc) != sharks and smells[nr][nc] < s:
                    new_fishes[(nr, nc, (d - i) % 8)] += v
                    new_fish_sea[nr][nc] += v
                    break
            else:
                new_fishes[(r, c, d)] += v
                new_fish_sea[r][c] += v

        max_cnt, max_movings = -1, []
        sr, sc = sharks
        get_max_eating(sr, sc, 0, 0, [], new_fish_sea)

        sharks = max_movings[-1]
        for r, c in max_movings:
            for d in range(8):
                if (r,c,d) in new_fishes:
                    del new_fishes[(r,c,d)]
            if new_fish_sea[r][c] > 0:
                smells[r][c] = s + 2

        for (r, c, d), v in fishes.items():
            new_fishes[(r,c,d)] += v

        fishes = new_fishes
    return sum(fishes.values())
def sol():
    global N, M, S
    M, S = map(int, input().split())
    fishes = defaultdict(int)
    for _ in range(M):
        fx, fy, d = map(lambda x: int(x) - 1, input().split())
        fishes[(fx, fy, d)] += 1
    sharks = tuple(map(lambda x: int(x) - 1, input().split()))
    N = 4
    print(get_fishes_count(fishes, sharks))

sol()