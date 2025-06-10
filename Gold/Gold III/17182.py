"""
masking을 n번 호출해야 답이나온다. 왜지?
33432	92

masking() 함수는 1번 호출 시 단계별로 한 번씩 상태 전이만 수행합니다. 
그런데 비트마스크 기반 DP에서는 이전의 여러 경로에서 상태가 파생되어야 최적값이 도달할 수 있습니다.

큐 기반 상태 전이(BFS 방식)로 최적값 전파
34952	72
"""
from collections import deque
import sys
input = sys.stdin.readline

def get_minimum_time(N, K, g):
    INF = int(1e6)
    size = 1 << N
    dp = [[INF] * N for _ in range(size)]

    dp[1 << K][K] = 0
    queue = deque()
    queue.append((1 << K, K))

    while queue:
        mask, u = queue.popleft()
        for v in range(N):
            if u == v:
                continue
            
            new_mask = mask | (1 << v)
            next_cost = dp[mask][u] + g[u][v]
            if dp[new_mask][v] > next_cost:
                dp[new_mask][v] = next_cost
                queue.append((new_mask, v))

    
    return min(dp[size - 1])

def sol():
    N, K = map(int, input().split())
    g = [list(map(int, input().split())) for _ in range(N)]

    print(get_minimum_time(N, K, g))

sol()