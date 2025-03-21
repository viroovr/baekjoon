"""
최단거리 bfs를 이용하기 위해, 각 번호마다의 이동이아니라, 타일간에 이동이어야한다.
한 타일에 왔을 때, 2개의 번호를 모두 queue에 넣어 작동시키니 돌아갔다.
그전까지 계속 왜틀리지 고민했다.
120712	1032
"""

from collections import deque
import sys
input = sys.stdin.readline

def get_min_tiles(N, tiles):
    grids = [[] for _ in range(N)]
    offset = 1
    for i in range(N):
        if i % 2 == 0:
            for j in range(N):
                grids[i].append([offset + j, tiles[offset - 1 + j][0], False])
                grids[i].append([offset + j, tiles[offset - 1 + j][1], False])
            offset += N
        else:
            grids[i].append((-1,-1))
            for j in range(N - 1):
                grids[i].append([offset + j, tiles[offset - 1 + j][0], False])
                grids[i].append([offset + j, tiles[offset - 1 + j][1], False])
            grids[i].append((-1,-1))
            offset += N - 1
    
    parent = [-1] * (N * N - N // 2 + 1)
    parent[1] = 0

    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    grids[0][0][2] = True
    grids[0][1][2] = True

    q = deque([(0, 0), (0, 1)])

    last = 1
    while q:
        r, c = q.popleft()
        
        cur_tile, cur_cnt, _ = grids[r][c]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < N and 0 <= nc < N * 2 and grids[nr][nc][0] != -1 and not grids[nr][nc][2]:
                tile_num, tile_cnt, _ = grids[nr][nc]
                if tile_num != cur_tile and tile_cnt == cur_cnt:
                    if last < tile_num:
                        last = tile_num
                    
                    q.append((nr, nc))
                    parent[tile_num] = cur_tile
                    grids[nr][nc][2] = True

                    if 0 <= nc - 1 and grids[nr][nc - 1][0] == tile_num:
                        q.append((nr, nc - 1))
                        grids[nr][nc - 1][2] = True
                    elif nc + 1 < N * 2 and grids[nr][nc + 1][0] == tile_num:
                        q.append((nr, nc + 1))
                        grids[nr][nc + 1][2] = True

    result = []
    while last > 0:
        result.append(last)
        last = parent[last]
    
    print(len(result))
    print(*reversed(result))


def sol():
    N = int(input().strip())
    tiles = [tuple(map(int, input().strip().split())) for _ in range(N**2-N//2)]
    get_min_tiles(N, tiles)
sol()