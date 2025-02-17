"""
1. 회전 연산 감소 → for i in range(2, N + 1) → for i in range(x, N + 1, x)
    - 원래 2, 3, 4, ..., N까지 반복하던 것을 x의 배수만 처리하도록 변경하여 불필요한 반복을 줄였습니다.
2. remaining_num을 딕셔너리 대신 리스트로 변경하여 더 빠른 연산 수행
그 외 total_sum, total_count를 O(1) 으로 반영하는 코드는 반복문내에서 수동으로 계산해서 일까. 더 느렸다.

35068	208 
35044	204 1,2
"""
from collections import deque

def loggin_planes(circular_planes):
    for i in range(N):
        print(*circular_planes[i])

def get_plane_sum(circular_planes, rotating_methods):
    bfs_directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    remaining_num = [M] * N
    for x, d, k in rotating_methods:
        for i in range(x, N + 1, x):
            circular_planes[i - 1].rotate(-k if d else k)
        is_adj_same = False
    
        for r in range(N):
            if remaining_num[r] == 0:
                continue
            for c in range(M):
                if circular_planes[r][c] == 0:
                   continue
                is_find = False
                find_num = circular_planes[r][c]

                q = deque()
                q.append((r, c))
                circular_planes[r][c] = 0
                remaining_num[r] -= 1
                while q:
                    cr, cc = q.popleft()
                    for dr, dc in bfs_directions:
                        nr, nc = cr + dr, (cc + dc) % M
                        if nr < 0 or nr >= N or circular_planes[nr][nc] != find_num:
                            continue
                        q.append((nr, nc))
                        circular_planes[nr][nc] = 0
                        remaining_num[nr] -= 1
                        is_find = True
                if is_find:
                    is_adj_same = True
                else:
                    circular_planes[r][c] = find_num
                    remaining_num[r] += 1
                            
        if is_adj_same:
            continue

        total_remaining = sum(i for i in remaining_num.values())
        if total_remaining == 0:
            return 0

        avg = sum(sum(row) for row in circular_planes) / total_remaining

        for i in range(N):
            if remaining_num[i] > 0:
                for j in range(M):
                    finding_num = circular_planes[i][j]
                    if finding_num == 0:
                        continue
                    if finding_num > avg:
                        circular_planes[i][j] -= 1
                    elif finding_num < avg:
                        circular_planes[i][j] += 1

    return sum(sum(row) for row in circular_planes)

def sol():
    global N,M,T
    N, M, T = map(int, input().split())
    circular_planes = [deque(map(int, input().split())) for _ in range(N)]
    rotating_methods = [tuple(map(int, input().split())) for _ in range(T)]
    s = get_plane_sum(circular_planes, rotating_methods)
    print(s)

sol()