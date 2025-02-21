"""
1. nr, nc 없이 바로 r, c 대입
2. sys.stdin.readline
3. 종료 조건 단순화 c > 0
32412	192 
32412	192 1, 3
32412	184 1, 2, 3
"""

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
moving_directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
import sys
input = sys.stdin.readline

def moving_beads():
    beads = [0]
    r, c = shark_pos
    moving_idx = -1
    for s in range(1, N + 1):
        for _ in range(2):
            moving_idx = (moving_idx + 1) % 4
            for ds in range(1, s + 1):
                nr, nc = r + moving_directions[moving_idx][0], c + moving_directions[moving_idx][1]
                if nr == 0 and nc == -1:
                    return beads
                if grids[nr][nc] > 0:
                    beads.append(grids[nr][nc])
                r, c = nr, nc

    return beads

def push_beads(beads):
    beads.extend([0] * ((N ** 2) - len(beads)))
    r, c = shark_pos
    moving_idx = -1
    i = 1
    for s in range(1, N + 1):
        for _ in range(2):
            moving_idx = (moving_idx + 1) % 4
            for ds in range(1, s + 1):
                nr, nc = r + moving_directions[moving_idx][0], c + moving_directions[moving_idx][1]
                if nr == 0 and nc == -1:
                    return
                grids[nr][nc] = beads[i]
                i += 1
                r, c = nr, nc

def count_group(beads, exploded_beads):
    beads.append(0)
    new_beads = [0]
    first = beads[1]
    cnt = 1
    is_exploded = False
    for i in range(2, len(beads)):
        if beads[i] == first:
            cnt += 1
        else:
            if cnt < 4:
                new_beads.extend([first] * cnt)
            else:
                exploded_beads[first] += cnt
                is_exploded = True
            first = beads[i]
            cnt = 1

    return new_beads, is_exploded

def group_change(beads):
    beads.append(0)
    new_beads = [0]
    first = beads[1]
    cnt = 1
    for i in range(2, len(beads)):
        if beads[i] == first:
            cnt += 1
        else:
            new_beads.extend([cnt, first])
            first = beads[i]
            cnt = 1
    return new_beads

def get_exploded_beads(magics):
    exploded_beads = {i: 0 for i in range(1, 4)}
    for d, s in magics:
        dr, dc = directions[d]

        for ds in range(1, s + 1):
            nr, nc = ds * dr + shark_pos[0], ds * dc + shark_pos[1]
            if grids[nr][nc]> 0:
                grids[nr][nc] = 0
        
        beads = moving_beads()
        is_exploded = True
        while is_exploded: beads, is_exploded = count_group(beads, exploded_beads)

        beads = group_change(beads)
        push_beads(beads)

    return sum(exploded_beads[i] * i for i in range(1, 4))

def sol():
    global N, M, grids, shark_pos
    N, M = map(int, input().split())
    grids = [list(map(int, input().split())) for _ in range(N)]
    magics = [(int(x) - 1, int(y)) for (x, y) in (input().split() for _ in range(M))]
    shark_pos = ((N + 1)//2 - 1, (N + 1)//2 - 1)
    print(get_exploded_beads(magics))

sol()