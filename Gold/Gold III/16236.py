"""
최적화 포인트
1. visited 배열을 리스트가 아닌 set으로 관리
    - visited[y][x] 대신 set을 사용하면 탐색 시 속도를 줄일 수 있습니다.
    - visited.add((x, y)) 형태로 관리.
2. deque 대신 heapq를 활용한 BFS 탐색
    - 현재 deque를 사용하지만, BFS 탐색 과정에서 heapq를 적극 활용하면 더 빠른 최적 경로를 찾을 수 있습니다.
    - heapq는 자동 정렬되어, 가장 가까운 물고기를 찾는 과정에서 더 효율적.
3. heapq에서 한 번에 정렬하여 최소값을 찾음
    - 기존 코드에서는 heapq.heappop()을 여러 번 호출하는데, 한 번에 heapq.heappop()을 사용하면 불필요한 반복을 줄일 수 있습니다.
4. 딕셔너리(defaultdict) 대신 Counter 활용
    - defaultdict(int) 대신 collections.Counter를 사용하면 더 간결하고 성능도 개선될 수 있습니다.
36528	68
36720	64
"""

from collections import Counter
import heapq
import sys

directions = [(0, -1), (-1, 0), (1, 0), (0, 1)]
input = sys.stdin.readline

def get_eating_times(spaces, fish_numbers, x, y):
    time, baby_size, eating = 0, 2, 0
    while any((k < baby_size and v > 0) for k, v in fish_numbers.items()):
        # print("=========")
        # print(f"time : {time}, baby_size = {baby_size}, eating : {eating}, x, y: ({x}, {y})")
        # for i in range(N):
        #     print(*spaces[i])
        # print("========")
        q = [(0, y, x)]
        visited = set()
        visited.add((y, x))
        found_fish = []
        while q:
            depth, cy, cx = heapq.heappop(q)

            if found_fish and depth > found_fish[0][0]:
                break

            if 0 < spaces[cy][cx] < baby_size:
                heapq.heappush(found_fish, (depth, cy, cx))

            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if not (0 <= nx < N and 0 <= ny < N) or (ny, nx) in visited:
                    continue
                if spaces[ny][nx] <= baby_size:
                    heapq.heappush(q, (depth + 1, ny, nx))
                    visited.add((ny, nx))

        if not found_fish:
            return time

        d, y, x = heapq.heappop(found_fish)
        time += d
        eating += 1

        if eating == baby_size:
            baby_size += 1
            eating = 0
        
        fish_numbers[spaces[y][x]] -= 1
        spaces[y][x] = 0

    return time
    
def sol():
    global N
    N = int(input())
    spaces = [list(map(int, input().split())) for _ in range(N)]
    fish_numbers = Counter()
    x, y = 0, 0
    for r in range(N):
        for c in range(N):
            if spaces[r][c] == 0:
                continue
            elif spaces[r][c] == 9:
                x, y = c, r
                spaces[r][c] = 0
            else:
                fish_numbers[spaces[r][c]] += 1
    t = get_eating_times(spaces, fish_numbers, x , y)
    print(t)

sol()