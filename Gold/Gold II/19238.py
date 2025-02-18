"""
개선된 점
1. 우선순위 큐 (heapq) 활용
    - 손님을 찾을 때 (거리, r, c) 형태로 관리하여 자동 정렬됨 → 최적의 손님을 빠르게 선택 가능
2. 탐색 과정 최적화
    - 손님을 찾을 때 BFS 탐색을 줄이기 위해 heapq를 사용하여 최단 거리 손님을 즉시 선택
    - 목적지까지의 거리를 구하는 과정에서 별도로 visited 배열을 초기화하여 사용
3. 불필요한 변수 제거 및 가독성 향상
    - remaining_customer를 제거하고, while customers: 방식으로 반복을 단순화
    - find_nearest_customer와 find_shortest_path를 별도 함수로 분리하여 재사용 가능하게 구성
4. 코드 구조 개선
    - find_nearest_customer: 가장 가까운 손님 찾기 (BFS + heapq)
    - find_shortest_path: 최단 거리 찾기 (BFS)
    - get_remaining_oil: 전체 연료 관리 및 이동 처리
35100	124 
35692	124 1,2,3,4
"""
from collections import deque
from heapq import heappop, heappush

directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def find_nearest_customer(oil, board, taxi_pos, customers):
    q = [(0, *taxi_pos)]
    visited = [[False] * N for _ in range(N)]
    visited[taxi_pos[0]][taxi_pos[1]] = True
    while q:
        dist, r, c = heappop(q)
        if (r, c) in customers:
            return dist, (r, c), customers[(r, c)]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (0 <= nr < N and 0 <= nc < N) and not visited[nr][nc] and board[nr][nc] != 1:
                visited[nr][nc] = True
                heappush(q, (dist + 1, nr, nc))
    return -1, None, None

def find_shortest_path(start, end, board):
    visited = [[-1] * N for _ in range(N)]
    q = deque([start])
    visited[start[0]][start[1]] = 0
    while q:
        r, c = q.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (0 <= nr < N and 0 <= nc < N) and visited[nr][nc] == -1 and board[nr][nc] == 0:
                q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1
                if (nr, nc) == end:
                    return visited[nr][nc]
    return -1


def get_remaining_oil(oil, board, taxi_pos, customers):
    while customers:
        dist_to_customer, customer_pos, destination = find_nearest_customer(oil, board, taxi_pos, customers)
        if dist_to_customer == -1 or oil <= dist_to_customer:
            return -1

        oil -= dist_to_customer
        dist_to_dest = find_shortest_path(customer_pos, destination, board)
        if dist_to_dest == -1 or oil < dist_to_dest:
            return -1
        
        oil += dist_to_dest
        taxi_pos = destination
        del customers[customer_pos]

    return oil

def sol():
    global N, M
    N, M, oil = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    taxi_pos = tuple(map(lambda x : int(x) - 1, input().split()))
    customers = {}
    for _ in range(M):
        r, c, dr, dc = map(lambda x : int(x) - 1, input().split())
        customers[(r, c)] = (dr, dc)

    print(get_remaining_oil(oil, board, taxi_pos, customers))

sol()
    