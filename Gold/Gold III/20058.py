"""
1. new_ices = [[0] * N for _ in range(N)]로 올바르게 초기화
2. sum(0 <= r+dr < N and 0 <= c+dc < N and new_ices[r+dr][c+dc] > 0 ...)를 활용하여 멜팅 조건 최적화
3. input = sys.stdin.readline
35068	2772
35092	2768    3
35200	4384    1,2
35076	4316    2,3
35100	2812    1,3
2가 느림. 1도 별로
"""

from collections import deque
import sys
input = sys.stdin.readline

def rotate(board):
    return [list(row) for row in zip(*board[::-1])]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def get_loaf(ices):
    visited = [[False] * N for _ in range(N)]

    max_loaf = 0
    for r in range(N):
        for c in range(N):
            if visited[r][c] or ices[r][c] == 0:
                continue

            q = deque([(r, c)])
            visited[r][c] = True
            cnt = 0
            while q:
                cr, cc = q.popleft()
                cnt += 1
                for dr, dc in directions:
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and ices[nr][nc] > 0:
                        q.append((nr, nc))
                        visited[nr][nc] = True
            
            max_loaf = max(max_loaf, cnt)

    return max_loaf

def get_remaining_ice_and_loaf(ices):
    for l in L:
        new_ices = [[] * N for _ in range(N)]

        for r in range(0, N, l):
            for c in range(0, N, l):
                rotated = rotate([row[c:c+l] for row in ices[r:r+l]])
                for nr in range(l):
                    new_ices[r + nr].extend(rotated[nr])

        melting_coords = []
        for r in range(N):
            for c in range(N):
                if new_ices[r][c] == 0:
                    continue
                cnt = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < N and new_ices[nr][nc] > 0:
                        cnt += 1
                if cnt < 3:
                    melting_coords.append((r, c))
        
        for r, c in melting_coords:
            new_ices[r][c] -= 1

        ices = new_ices
    
    return sum(map(sum, ices)), get_loaf(ices)
                    
def sol():
    global N, Q, L
    N, Q = map(int, input().split())
    N = 2 ** N
    ices = [list(map(int, input().split())) for _ in range(N)]
    L = [2 ** i for i in map(int, input().split())]
    u, t = get_remaining_ice_and_loaf(ices)
    print(u)
    print(t)
    
sol()