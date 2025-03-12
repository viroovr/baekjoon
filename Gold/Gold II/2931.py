"""
너무 흐름을 한 번에 해석하면서 파이프 종류도 바로 결정하려 한게 오산이었다.
시간복잡도는 backtracking으로 충분했지만, 파이프를 결정하고 도달했는지 확인하는 과정이 복잡했다.
결국 아이디어적으로, bfs, dfs에 머물지말고, 파이프가 흘러가다가 빈 위치가 발견된다면 이곳이 결정해야할
부분임을 알아야했다.
그런데, 이게 M 근처나 Z근처가 비어있는 경우를 생각하느라 좀 골치아팠던 것 같다.
하지만 입력에서 M과 Z는 하나의 블록과 인접해 있는 입력만 주어진다했으므로, 무조건 파이프인 위치에서
시작함을 알 수 있다.

그냥 모든 "."에서 연결이 가능한 부분을 전부 탐색해서 풀어도 된다.
그러다 bfs로 파이프 시작점에서 연결이 불가능한 부분을 찾게 되면 그 부분을 중심으로 type을 결정하면 된다.
35028	60  O(RC) 전부 탐색
35084	56  O(RC) bfs 우선탐색
"""

from collections import deque
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

pipes = {
    "|" : [(-1, 0), (1, 0)],
    "-" : [(0, -1), (0, 1)],
    "+" : [(-1, 0), (1, 0), (0, -1), (0, 1)],
    "1" : [(1, 0), (0, 1)],
    "2" : [(-1, 0), (0, 1)],
    "3" : [(-1, 0), (0, -1)],
    "4" : [(1, 0), (0, -1)],
}

def bfs_find_missing(start_r, start_c):
    q = deque()
    visited = [[False] * C for _ in range(R)]
    visited[start_r][start_c] = True
    for dr, dc in directions:
        r, c = start_r + dr, start_c + dc
        if 0 <= r < R and 0 <= c < C and europe[r][c] in pipes:
            if (-dr, -dc) in pipes[europe[r][c]]:
                q.append((r, c))
                visited[r][c] = True
                break

    while q:
        r, c = q.popleft()
        
        for dr, dc in pipes.get(europe[r][c], []):
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                if europe[nr][nc] == ".":
                    return nr, nc
                if europe[nr][nc] in pipes and (-dr, -dc) in pipes[europe[nr][nc]]:
                    visited[nr][nc] = True
                    q.append((nr, nc))

def find_missing_pipe():
    connections = []
    for dr, dc in directions:
        nr, nc = mr + dr, mc + dc
        if 0 <= nr < R and 0 <= nc < C and (-dr, -dc) in pipes.get(europe[nr][nc], []):
            connections.append((dr, dc))
    
    return connections

def determine_type():
    for k, v in pipes.items():
        if set(connections) == set(v):
            return k

R, C = map(int, input().split())
europe = [list(input()) for _ in range(R)]
M, Z = 0, 0
for r in range(R):
    for c in range(C):
        if europe[r][c] == "M":
            M = (r, c)
        elif europe[r][c] == "Z":
            Z = (r, c)


mr, mc = bfs_find_missing(M[0], M[1])
connections = find_missing_pipe()

print(mr + 1, mc + 1, determine_type())