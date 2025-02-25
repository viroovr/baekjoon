"""
백조가 가려다 막힌 곳을 다음 움직일 swan_queue에 저장하고, 물이 다음 녹일 얼음을 녹이고 그 자리를
water_queue에 저장하는 방식으로 처음부터 계속 O(RC) 로 탐색하는게 아니라, 동적으로
녹을 빙하에 이어나가는 방식이다.
K를 빙하의 경계 개수라한다면 O(K log K)의 시간복잡도를 가지게 된다.

빙하가 녹을 때 각 단계에서 새로운 경계를 찾아야 하므로 log K의 비용이 추가됩니다.
즉, 단순한 O(K)가 아니라 O(K log K)로 본다.
"""

from collections import deque
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def can_meet(spaces, swan_queue, visited, target):
    next_queue = deque()
    while swan_queue:
        r, c = swan_queue.popleft()
        if (r, c) == target:
            return True, None
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0<=nr<R and 0<=nc<C and not visited[nr][nc]:
                visited[nr][nc] = True
                if spaces[nr][nc] == '.':
                    swan_queue.append((nr, nc))
                else:
                    next_queue.append((nr, nc))
    return False, next_queue

def melt(spaces, water_queue):
    next_queue = deque()
    while water_queue:
        r, c = water_queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0<=nr<R and 0<=nc<C and spaces[nr][nc] == "X":
                spaces[nr][nc] = "."
                next_queue.append((nr, nc))
    return next_queue

def get_meeting_days(spaces):
    water_queue = deque()
    swan_queue = deque()
    visited = [[False] * C for _ in range(R)]

    for r in range(R):
        for c in range(C):
            if spaces[r][c] == ".":
                water_queue.append((r, c))
    
    sr1, sc1 = swan_poses[0]
    sr2, sc2 = swan_poses[1]
    swan_queue.append((sr1, sc1))
    visited[sr1][sc1] = True

    day = 0
    while True:
        met, next_swan_queue = can_meet(spaces, swan_queue, visited, (sr2, sc2))
        if met:
            return day
        
        water_queue = melt(spaces, water_queue)

        swan_queue = next_swan_queue
        day += 1
    return day

def sol():
    global R, C, swan_poses
    R, C = map(int, input().split())
    spaces = []
    swan_poses = []
    for r in range(R):
        row = list(input())
        for c in range(C):
            if row[c] == "L":
                row[c] = "."
                swan_poses.append((r, c))
        spaces.append(row)
    
    print(get_meeting_days(spaces))

sol()