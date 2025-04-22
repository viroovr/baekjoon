"""
3차원 방문 배열을 선언해서 이동거리를 n, m, k에 따라 넣었다.
이는 직관적이고 정확한 방법이지만 공간복잡도가 O(NMK)인 문제가 있어 느린 시간에 통과했다.

2차원 방문 배열을 선언해서, k값을 n, m에 따라 넣었다. 이동거리는 q에서 관리한다.
최단거리는 결국 bfs로 N, M까지 가는 경우이므로, 거리값에서 최솟값을 관리하지 않아도 된다.
대신 k값에 따라 재방문 여부를 판별한다.

335072	4096    3차원
226360	1712    2차원
"""

import sys
input = sys.stdin.readline
from collections import deque

def get_shortest_path(N, M, K, grids):
    visited = [[11] * M for _ in range(N)]
    q = deque([(0, 0, 1)])
    visited[0][0] = 0

    directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
    while q:
        x, y, count = q.popleft()
        if x == M - 1 and y == N - 1:
            return count
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N:
                k = visited[y][x] + grids[y][x]

                if visited[ny][nx] > k and k <= K:
                    q.append((nx, ny, count + 1))
                    visited[ny][nx] = k

    return -1

def sol():
    N, M, K = map(int, input().split())
    grids = [list(map(int, list(input().rstrip()))) for _ in range(N)]

    print(get_shortest_path(N, M, K, grids))

sol()