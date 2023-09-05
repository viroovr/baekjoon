import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

T = int(input())


def dp(n):
    if time[n] == -1:
        if adj[n]:
            time[n] = max(dp(i) for i in adj[n]) + D[n - 1]
        else:
            time[n] = D[n - 1]
    return time[n]


for i in range(T):
    N, K = map(int, input().split())
    time = [-1] * (N + 1)
    D = list(map(int, input().split()))
    adj = [[] for _ in range(N + 1)]
    for _ in range(K):
        n, m = map(int, input().split())
        adj[m].append(n)
    # print(adj)
    W = int(input())
    print(dp(W))
    # print(N, K, D, adj, W)

# 8 8
# 10 20 1 5 8 7 1 43
# 1 2
# 1 3
# 2 4
# 2 5
# 3 6
# 5 7
# 6 7
# 7 8
# 7

# 1   2   4
#         5   7   8
#     3   6  /
# 10 + 20 + 8 + 1 + 7 + 1