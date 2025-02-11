"""
✅ 최적화 포인트
1. visited 초기화 최적화
    - visited = [[False] * N for _ in range(N)]로 변경하여 리스트 컴프리헨션을 활용해 더 빠르게 초기화합니다.
2. 인구 이동 연산 최적화
    - (nr, nc) 리스트에 좌표를 추가하는 과정에서 리스트 크기를 매번 len()으로 확인하는 대신, 개수를 추적하는 변수를 사용합니다.
3. N, L, R 지역 변수화
    - 지역 변수 (Local Variable)
        지역 변수는 함수의 스택 프레임(Stack Frame) 내에서 직접 참조됩니다.
        이는 CPU의 캐시에 더 가깝고 빠르게 접근할 수 있음을 의미합니다.
    - 전역 변수 (Global Variable)
        전역 변수는 globals() 딕셔너리에서 검색해야 합니다.
        즉, 딕셔너리 조회 연산이 추가적으로 필요하므로 속도가 느립니다.
메모리  시간
34992	4084
35016	4076
"""
from collections import deque
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def get_population_moving_days(countries, N, L, R):
    days = 0
    while True:
        visited = [[False] * N  for _ in range(N)]
        is_move = False
        for r in range(N):
            for c in range(N):
                if visited[r][c]:
                    continue

                q = deque()
                q.append((r, c))
                visited[r][c] = True

                stored_coordinate = [(r, c)]
                total_population = countries[r][c]

                while q:
                    cr, cc = q.popleft()
                    for dc, dr in directions:
                        nr, nc = dr + cr, dc + cc
                        if not (0 <= nr < N and 0 <= nc < N) or visited[nr][nc]:
                            continue
                        if L <= abs(countries[cr][cc] - countries[nr][nc]) <= R:
                            is_move = True

                            visited[nr][nc] = True
                            q.append((nr, nc))

                            stored_coordinate.append((nr, nc))
                            total_population += countries[nr][nc]

                new_population = total_population // len(stored_coordinate)
                for nr, nc in stored_coordinate:
                    countries[nr][nc] = new_population
        if not is_move:
            return days
        days += 1
                         
def sol():
    N, L, R = map(int, input().split())
    countries = [list(map(int, input().split())) for _ in range(N)]
    print(get_population_moving_days(countries, N, L, R))

sol()