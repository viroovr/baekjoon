"""
🔹 최적화 요약
1. BFS 탐색 중 depth 계산을 visited[y][x] + 1로 변경하여 불필요한 max 연산 제거.
2. visited[y][x] = True → 거리 저장을 위해 -1로 초기화한 후 거리값 저장.
3. zero_cnt = sum(row.count(0) for row in laboratory)로 0 개수 카운트 최적화.
4. virus_poses를 이중 for문 없이 리스트 컴프리헨션으로 변환.
✨ 기대 성능 향상
1. 더 빠른 BFS 수행 (거리값을 visited 배열에 저장하여 max 연산 제거).
2. 메모리 절약 (visited를 True/False 대신 거리값을 저장하는 방식으로 활용).
3. 더 간결한 코드 (이중 루프 제거, deque(list(poses)) → deque(poses) 등).
"""

from collections import deque
from itertools import combinations
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def get_spread_min_time(laboratory, zero_cnt, virus_poses):
    min_time = 50*50
    for poses in combinations(virus_poses, M):
        q = deque(poses)
        local_zero_cnt = zero_cnt

        visited = [[-1] * N for _ in range(N)]
        for y, x in poses:
            visited[y][x] = 0

        local_min_time = 0

        while q:
            y, x = q.popleft()

            for dy, dx in directions:
                cy, cx = y + dy, x + dx
                if not (0 <= cy < N and 0 <= cx < N) or visited[cy][cx] != -1 or laboratory[cy][cx] == 1:
                    continue
                
                visited[cy][cx] = visited[y][x] + 1
                q.append((cy, cx))
                if laboratory[cy][cx] == 0:
                    local_min_time = visited[cy][cx]
                    local_zero_cnt -= 1
        
        if local_zero_cnt <= 0:
            min_time = min(min_time, local_min_time)

    return min_time if min_time != 50 * 50 else -1

def sol():
    global N, M
    N, M = map(int, input().split())
    laboratory = [list(map(int, input().split())) for _ in range(N)]
    zero_cnt = sum(row.count(0) for row in laboratory)
    virus_poses = [(r, c) for r in range(N) for c in range(N) if laboratory[r][c] == 2]
    print(get_spread_min_time(laboratory, zero_cnt, virus_poses))
    
sol()