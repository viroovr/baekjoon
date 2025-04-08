"""
dp[node][0], dp[node][1]으로 부모가 포함되었을 때 / 포함되지 않았을 때 구분 → 2차원 DP.

dp_list도 마찬가지로 2차원 배열로 관리 → 중복 호출 제거.

조건문 간소화 및 리팩토링.

35480	64  input
38688	76  input, 최적화
"""

import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**5)
def get_independent_subset(N, weights, edges):
    dp = [[0, 0] for _ in range(N + 1)]
    dp_list = [[[], []] for _ in range(N + 1)]

    def dfs(parent, node):
        dp[node][1] = weights[node]
        dp_list[node][1] = [node]

        for child in edges[node]:
            if child == parent:
                continue

            dfs(node, child)

            dp[node][0] += max(dp[child][0], dp[child][1])
            if dp[child][0] > dp[child][1]:
                dp_list[node][0].extend(dp_list[child][0])
            else:
                dp_list[node][0].extend(dp_list[child][1])
            
            dp[node][1] += dp[child][0]
            dp_list[node][1].extend(dp_list[child][0])

    dfs(-1, 1)
    if dp[1][1] > dp[1][0]:
        print(dp[1][1])
        print(*sorted(dp_list[1][1]))
    else:
        print(dp[1][0])
        print(*sorted(dp_list[1][0]))
        
def sol():
    N = int(input())
    weights = [-1, *map(int, input().rstrip().split())]
    edges = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = map(int, input().rstrip().split())
        edges[a].append(b)
        edges[b].append(a)
    
    get_independent_subset(N, weights, edges)

sol()