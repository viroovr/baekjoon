"""
1.sysinput
2.3개의 하드코딩
33432	60  
33432	60  2  
33432	36  1,2
"""

import sys
input = sys.stdin.readline

def get_min_costs(N, costs):
    dp = [[0] * 3 for _ in range(N)]
    for i in range(3):
        dp[0][i] = costs[0][i]

    for i in range(1, N):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2]
    
    return min(dp[-1])

def sol():
    N = int(input())
    costs = [list(map(int, input().split())) for _ in range(N)]
    print(get_min_costs(N, costs))

sol()