"""
처음에는 Kruksal 알고리즘을 사용해서, 접근했지만, edge가 메모리초과를 일으켰다.
prim을 사용해서 구했다.

다시 알고리즘을 떠올리며 구현해본 좋은 복습시간이었다.
33432	872
"""

import sys
input = sys.stdin.readline

def dist(p, q):
    return (p[0] - q[0])**2 + (p[1] - q[1])**2

def get_minimum_amount(N, C, points):
    INF = int(1e7)
    ans = 0

    visited = [False] * N
    distance = [INF] * N
    distance[0] = 0
    for _ in range(N):
        min_edge, min_v = INF, -1
        for nxt in range(N):
            if not visited[nxt] and min_edge > distance[nxt]:
                min_edge = distance[nxt]
                min_v = nxt
        
        if min_v == -1:
            print(-1)
            return
        
        # print(min_v, min_edge, distance)
        ans += min_edge
        visited[min_v] = True

        for nxt in range(N):
            if not visited[nxt]:
                d = dist(points[min_v], points[nxt])
                if distance[nxt] > d >= C:
                    distance[nxt] = d

    print(ans)

def sol():
    N, C = map(int, input().split())
    points = [tuple(map(int, input().rstrip().split())) for _ in range(N)]
    get_minimum_amount(N, C, points)

sol()