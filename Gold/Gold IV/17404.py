"""
첫번쨰 컬러를 고정시켰을 때의 dp를 3개 생성해서 각각에 대해 마지막 집의 dp값 중
첫번째 컬러와 다른 값에 대해서만 결과 최솟값에 반영했다.

최적화 결과, 1개의 dp를 생성하고, 마지막 집에서만 start_color와 다른 값만 result와
갱신하도록 변경했다.

33432	56
33432	36  dp 1개 생성, input
"""
import sys
input = sys.stdin.readline

def get_min_cost(N, costs):
    INF = int(1e7)
    result = INF
    
    for start_color in range(3):
        dp = [[INF] * 3 for _ in range(N)]
        dp[0][start_color] = costs[0][start_color]

        for i in range(1, N):
            dp[i][0] = costs[i][0] + min(dp[i - 1][1], dp[i - 1][2])
            dp[i][1] = costs[i][1] + min(dp[i - 1][0], dp[i - 1][2])
            dp[i][2] = costs[i][2] + min(dp[i - 1][0], dp[i - 1][1])

        for end_color in range(3):
            if start_color != end_color:
                result = min(result, dp[N - 1][end_color])

    print(result)

def sol():
    N = int(input().strip())
    costs = [list(map(int, input().strip().split())) for _ in range(N)]
    get_min_cost(N, costs)

sol()