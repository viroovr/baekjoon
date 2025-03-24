"""
1. 중복 장애물 제거: x1, y1, x2, y2를 따로 처리할 필요 없이 visited_path를 장애물로 활용.
2. 거리 행렬 및 부모 행렬 최적화: 필요할 때만 값을 갱신하도록 변경.
3. dijkstra() 호출 최적화: A → B / B → A 두 가지 경우를 좀 더 깔끔하게 처리.
4. 경로 복원 최적화: parent를 활용해 직관적으로 경로 추적.

시간
1. [::-1] 과 reverse 중 reverse가 더빠름 -> 메모리 사용량이 증가하고, 할당 과정 때문에 속도가 조금 더 느림.
2. queue 탐색과정에서 if문에 조건문 추가는 시간 증가 요소임

35508	68
35508	64  1,2,3,4
"""

from heapq import heappop, heappush

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dijikstart(start_x, start_y, end_x, end_y, obstacles):
    INF = int(2e3)
    distance = [[INF] * N for _ in range(M)]
    parent = [[None] * N for _ in range(M)]

    for x, y in obstacles:
        distance[y][x] = -1

    if distance[start_y][start_x] == -1:
        return []

    distance[start_y][start_x] = 0
    q = [(0, start_x, start_y)]

    while q:
        cost, x, y = heappop(q)
        if (x, y) == (end_x, end_y):
            break

        if cost > distance[y][x]:
            continue

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                new_cost = cost + 1
                if distance[ny][nx] > new_cost:
                    distance[ny][nx] = new_cost
                    heappush(q, (new_cost, nx, ny))
                    parent[ny][nx] = (x, y)
    
    path = []
    x, y = end_x, end_y
    while x is not None:
        path.append((x, y))
        x, y = parent[y][x] if parent[y][x] is not None else (None, None)
    path.reverse()
    return path if path[0] == (start_x, start_y) else []

def get_min_cost(N, M):
    INF = int(2e3)
    path_A = dijikstart(A1_x, A1_y, A2_x, A2_y, [(B1_x, B1_y), (B2_x, B2_y)])
    path_B = dijikstart(B1_x, B1_y, B2_x, B2_y, path_A)

    first_len = len(path_A) + len(path_B) - 2 if path_A and path_B else INF

    path_B = dijikstart(B1_x, B1_y, B2_x, B2_y, [(A1_x, A1_y), (A2_x, A2_y)])
    path_A = dijikstart(A1_x, A1_y, A2_x, A2_y, path_B)

    second_len = len(path_A) + len(path_B) - 2 if path_A and path_B else INF
    
    result = min(first_len, second_len)
    print(result if result != INF else "IMPOSSIBLE")

def sol():
    global A1_x, A1_y,  A2_x, A2_y,  B1_x, B1_y,  B2_x, B2_y, N, M
    f = lambda : map(int, input().split())
    N, M = map(lambda x : int(x) + 1, input().split())
    A1_x, A1_y = f()
    A2_x, A2_y = f()
    B1_x, B1_y = f()
    B2_x, B2_y = f()

    get_min_cost(N, M)

sol()
