"""
1. visited 배열 제거
    dp에 그룹 번호를 직접 저장하여 방문 여부 체크
    -1이면 방문 안 한 곳, 그룹 번호이면 방문한 곳
2. BFS에서 set() 대신 list 사용 후 변환
    set은 해시 테이블 연산이 많아 list보다 느림
    coords.append() 후, set(coords) 변환이 더 빠름
3. 벽 주변 그룹 크기 합산 최적화
    set 대신 unique_groups으로 중복 체크
    group_sizes 배열을 만들어 O(1) 접근
4. 출력 최적화 (sys.stdout.write)
    print() 대신 sys.stdout.write() 사용
    문자열을 미리 만들어 한 번에 출력 (I/O 속도 개선)

211488	1780
113304	1176 1,2,3,4
"""

from collections import deque
import sys
input = sys.stdin.readline

def get_break_wall(N, M, grids):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    dp = [[-1] * M for _ in range(N)]
    group_sizes = []
    group_id = 0
    for i in range(N):
        for j in range(M):
            if dp[i][j] == -1 and grids[i][j] == 0:
                q = deque([(i, j)])
                coords = []
                dp[i][j] = group_id

                while q:
                    r, c = q.popleft()
                    coords.append((r, c))
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < N and 0 <= nc < M and grids[nr][nc] == 0 and dp[nr][nc] == -1:
                            q.append((nr, nc))
                            dp[nr][nc] = group_id
                
                group_sizes.append(len(coords) % 10)
                for r, c in coords:
                    dp[r][c] = group_id
                group_id += 1
    
    result = []
    for i in range(N):
        row = []
        for j in range(M):
            if grids[i][j] == 1:
                wall = 1
                vis = set()
                for dr, dc in directions:
                    nr, nc = i + dr, j + dc
                    if 0 <= nr < N and 0 <= nc < M and dp[nr][nc] != -1 and dp[nr][nc] not in vis:
                        wall += group_sizes[dp[nr][nc]]
                        vis.add(dp[nr][nc])
                
                row.append(str(wall % 10))
            else:
                row.append(str(grids[i][j]))
        result.append("".join(row))
    
    sys.stdout.write("\n".join(result) + "\n")
    
def sol():
    N, M = map(int, input().split())
    grids = [list(map(int, list(input().strip()))) for _ in range(N)]
    get_break_wall(N, M, grids)

sol()