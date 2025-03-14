"""
이전에 푼 레이저 문제와 유사하게 풀었다. 0-1bfs. bfs가 시간초과가 안나게 하려면, 방문 처리를 제대로
해줘서 큐의 크기가 커지지 않게 해주는 것이다.

1. i // 2로 수평, 수직 인덱싱 조합
2. end 데이터 제거

35044	64
34984	60  1,2
"""

from collections import deque

def get_min_mirror(start):
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    visited = [[[False, False] for _ in range(N)] for _ in range(N)]

    sr, sc = start

    q = deque([(sr, sc, 0)])
    visited[sr][sc] = [True, True]

    result = 51*51
    while q:
        r, c, cnt = q.popleft()

        for i, (dr, dc) in enumerate(directions):
            nr, nc = r + dr, c + dc
            while 0<=nr<N and 0 <=nc<N and house[nr][nc] != "*" and not visited[nr][nc][i // 2]:
                if house[nr][nc] == "!":
                    q.append((nr, nc, cnt + 1))
                elif house[nr][nc] == "#":
                    result = min(result, cnt)
                visited[nr][nc][i//2] = True
                nr += dr
                nc += dc

    print(result)

def sol():
    global N, house
    N = int(input())
    house = [list(input()) for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if house[r][c] == "#":
                get_min_mirror((r, c))
                return

sol()