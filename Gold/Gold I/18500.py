"""
시행착오가 계속있어 시도 10번만에 해결했다.

예전 문제를 기억하며, 떨어지는 클러스트에 맨 아래부분만 고려하여 클러스터를 내려가게 했다.
하지만 중간이 비어있는 클러스트의 경우 삐져나온 클러스트에 걸릴 수 있으므로, 클러스트 요소의 아래가 비어있는
모든 요소에대해 떨어지는 높이를 구해야한다.

이를 고려하고도 시간초과가 나는데,  cluster를 sort하고 bottom과 group을 생성하는데 있어 O(N * C) * O(RC log RC)이기 때문이다.
또한 구현에 있어서도 메모리와 복잡도 차원에서 문제가 있다. cluster를 한번에 union-find로 dijoint set이 되도록 하는것에서
구현 복잡도가 올라갔다.
pypy3로 제출하여 통과했지만 기존의 메모리들을 재사용하는 방법을 고려해 다시 풀어봤다.
122556	1348

q의 원소들을 그대로 이용해 clustering을 반환하고, visited도 부서진 곳을 중심으로 4방향에서 순차적으로 실행하여
재사용이 가능했다. bottom을 따로 구하지 않고도 group의 원소들로부터 바로 fall을 구할 수 있었다.
35084	596

구현 문제는 상황에 대한 철저한 이해가 바탕이 되어야 올바르게 풀 수 있다.
테스트 케이스를 직접 생각해 보는 연습이 필요하다.
"""

from collections import deque
import sys
input = sys.stdin.readline

def throw(R, C, cave, h, i):
    line = cave[R - h]
    r = range(C) if i % 2 == 0 else range(C - 1, -1, -1)
    for c in r:
        if line[c] == "x":
            line[c] = "."
            return (R - h, c)

    return None

directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def clustering(sr, sc, R, C, cave, visited):
    q = deque([(sr, sc)])
    visited[sr][sc] = -1
    i = 0
    is_bottom = False
    while i < len(q):
        r, c = q[i]
        i += 1
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and cave[nr][nc] == "x":
                if not visited[nr][nc]:
                    visited[nr][nc] = visited[r][c]
                    q.append((nr, nc))
                elif visited[r][c] > 0:
                    return False, None
            elif R <= nr:
                is_bottom = True
    
    if is_bottom:
        return False, None
    return True, set(q)

def falling(broken_coord, R, C, cave):
    visited = [[0] * C for _ in range(R)]
    for dr, dc in directions:
        nr, nc = broken_coord[0] + dr, broken_coord[1] + dc
        if 0 <= nr < R and 0 <= nc < C and cave[nr][nc] == "x" and not visited[nr][nc]:
            isbottom, groups = clustering(nr, nc, R, C, cave, visited)
            if not isbottom:
                continue
            fall = R - 1
            for br, bc in groups:
                f = 0
                while True:
                    br += 1
                    if br == R:
                        break
                    if cave[br][bc] == "x" and (br, bc) not in groups:
                        break
                    if cave[br][bc] == ".":
                        f += 1
                fall = min(f, fall)
            for r, c in groups:
                cave[r][c] = "."
            for r, c in groups:
                cave[r + fall][c] = "x"

def get_shape(R, C, cave, heights):
    for i, h in enumerate(heights):
        broken_coord = throw(R, C, cave, h, i)
        if broken_coord:
            falling(broken_coord, R, C, cave)

    for row in cave:
        print("".join(row))        
        
def sol():
    R, C = map(int, input().split())
    cave = [list(input().rstrip()) for _ in range(R)]
    _ = int(input())
    heights = list(map(int, input().split()))
    get_shape(R, C, cave, heights)

sol()