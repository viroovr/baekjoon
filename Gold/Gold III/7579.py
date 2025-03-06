"""
첫 시도로 최댓값 10*4 크기의 배열에 대해 모든 입력값들을 처리했다.
70028	276

두번째 시도로 sum(costs)를 max값으로 정해 처리했다.
49940	232

세번째 시도는 gpt에게서 도움을 받아, 1차원 배열로 풀이가 가능함을 확인했다.
각 index는 자신보다 낮은 비용에는 넣을 수 없으므로, 최댓값 비용부터 역순으로 자신의 비용까지 루프를 돈다.
그리고 넣을 경우네는, 현재 비용의 dp값에 자신의 메모리 값을 더한값과 넣지 않았을 때 dp 값 중 최대값을 해당 dp에
저장한다.
32412	96
"""

def get_min_costs(N, M, active_bytes, active_costs):
    MAX_COST = sum(active_costs)

    dp = [-1] * (MAX_COST + 1)
    dp[0] = 0
    for i in range(N):
        c, m = active_costs[i], active_bytes[i]
        for cost in range(MAX_COST, c - 1, -1):
            if dp[cost - c] != -1:
                dp[cost] = max(dp[cost], dp[cost - c] + m)

    for i in range(MAX_COST + 1):
        if dp[i] >= M:
            return i

f = lambda: map(int, input().split())
N, M = f()
active_bytes = list(f())
active_costs = list(f())

print(get_min_costs(N, M, active_bytes, active_costs))