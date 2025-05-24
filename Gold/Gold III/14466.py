"""
bfs와 union find를 합친 문제. 아이디어는 간단했다.

결괏값을 도출할 때, 조합을 이용해서 기존 O(K^2)에서 O(K) (K는 그룹 개수)시간복잡도로 변경했다.
35084	68
"""
from collections import deque
import sys
input = sys.stdin.readline

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def has_wall(r, c, dr, dc):
    return min(c + dc, c) in r_wall[r] if dr == 0 else min(r + dr, r) in c_wall[c]
            
def find(x):
    if parent[x] < 0:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if a == b:
        return
    if parent[a] < parent[b]:
        parent[a] += parent[b]
        parent[b] = a
    else:
        parent[b] += parent[a]
        parent[a] = b

def bfs(sr, sc, ci, visited):
    q = deque([(sr, sc)])
    visited[sr][sc] = True
    while q:
        r, c = q.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if not has_wall(r, c, dr, dc):
                    if meadow[nr][nc] > -1:
                        union(ci, meadow[nr][nc])
                    visited[nr][nc] = True
                    q.append((nr, nc))

def get_cannot_meet(cow_pos):
    global parent
    visited = [[False] * N for _ in range(N)]
    parent = [-1] * (K)
    for i, (r, c) in enumerate(cow_pos):
        if not visited[r][c]:
            bfs(r, c, i, visited)

    lis = [-i for i in parent if i < 0]
    total = sum(lis)
    total_pairs = total * (total - 1) // 2
    meetable_pairs = sum(s * (s - 1) // 2 for s in lis)
    print(total_pairs - meetable_pairs)

def sol():
    global N, K, R, c_wall, r_wall, meadow
    N, K, R = map(int, input().split())
    c_wall, r_wall = [set() for _ in range(N)], [set() for _ in range(N)]
    for _ in range(R):
        r, c, r_, c_ = map(int, input().rstrip().split())
        if r == r_:
            r_wall[r - 1].add(min(c, c_) - 1)
        else:
            c_wall[c - 1].add(min(r, r_) - 1)
    
    cow_pos = []
    meadow = [[-1] * N for _ in range(N)]
    for i in range(K):
        r, c = map(lambda x: int(x) - 1, input().rstrip().split())
        cow_pos.append((r, c))
        meadow[r][c] = i

    get_cannot_meet(cow_pos)

sol()