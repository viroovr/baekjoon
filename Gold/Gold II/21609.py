"""
무지개블록을 사용한 뒤 visited 처리를 False로 되돌려 줘야한다. 다른 일반 블록에서 재사용가능하니깐.
1. max()에서 불필요한 연산을 최소화하여 그룹 선택 속도 개선
2. rotate_left()에서 zip()을 활용한 리스트 회전 방식으로 성능 향상
3. gravity()에서 조건문 구조를 최적화하여 불필요한 연산 감소
4. get_score()에서 불필요한 함수 매개변수 제거로 호출 비용 절감
	35100	76  sorting
    35208	72  1 max(key),2,3,4
    35220	68  1 max(key, default),2,3,4
"""
from collections import deque

def find_biggest_group():
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = [[False] * N for _ in range(N)]
    
    groups = []
    for r in range(N):
        for c in range(N):
            if visited[r][c] or blocks[r][c] <= 0:
                continue
            
            color = blocks[r][c]
            q = deque([(r, c)])
            visited[r][c] = True

            group = [(r, c)]
            rainbow_pos = []
            
            while q:
                cr, cc = q.popleft()
                for dr, dc in directions:
                    nr, nc = cr + dr, cc + dc
                    if (0 <= nr < N and 0 <= nc < N) and not visited[nr][nc]:
                        if blocks[nr][nc] == color or blocks[nr][nc] == 0:
                            group.append((nr, nc))
                            q.append((nr, nc))
                            visited[nr][nc] = True
                            if blocks[nr][nc] == 0:
                                rainbow_pos.append((nr, nc))
            
            if len(group) >= 2:
                groups.append((len(group), len(rainbow_pos), r, c, group))

            for nr, nc in rainbow_pos:
                visited[nr][nc] = False
    
    return max(groups, key=lambda x: (x[0], x[1], x[2], x[3]), default=(0, 0, 0, 0, []))[4]

def rotate_left():
    global blocks
    blocks = list(map(list, zip(*blocks)))[::-1]

def gravity():
    global blocks
    for c in range(N):
        empty_idx = -1
        for r in range(N - 1, -1, -1):
            if blocks[r][c] == -1:
                empty_idx = -1
            elif blocks[r][c] == -2:
                if empty_idx == -1:
                    empty_idx = r
            elif empty_idx != -1:
                blocks[empty_idx][c], blocks[r][c] = blocks[r][c], -2
                empty_idx -= 1

def get_score():
    score = 0
    while True:
        max_group = find_biggest_group()
        if not max_group:
            return score
        score += len(max_group) ** 2
        for r, c in max_group:
            blocks[r][c] = -2
        
        gravity()
        rotate_left()
        gravity()

def sol():
    global N, M, blocks
    N, M = map(int, input().split())
    blocks = [list(map(int, input().split())) for _ in range(N)]
    print(get_score())

sol()