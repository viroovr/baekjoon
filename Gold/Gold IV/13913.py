"""
bfs문제

44220	136
48752	116 sys input, output
"""
import sys
from collections import deque
input = sys.stdin.readline

def get_min_time(N, K):
    M = 100_000
    q = deque([N])

    visited = [-1] * (M + 1)
    visited[N] = 0

    parent = [-1] * (M + 1)

    while q:
        x = q.popleft()

        if x == K:
            break

        for y in [x - 1, x + 1, 2 * x]:
            if 0 <= y <= M and visited[y] == -1:
                parent[y] = x
                visited[y] = visited[x] + 1
                q.append(y)

    i = K
    result = []
    while i >= 0:
        result.append(str(i))
        i = parent[i]
    
    sys.stdout.write(f"{len(result) - 1}\n" + " ".join(reversed(result)) + "\n")

def sol():
    N, K = map(int, input().strip().split())
    get_min_time(N, K)

sol()