"""
중복 조합을 이용해서 O(K) 내에 구할 수 있다.
카테고리가 dp던데, dp로 풀면 dp[n][k] = dp[n - 1][k] + dp[n - 2][k - 1]를 이용해 풀게된다.
시간복잡도는 O(NK)

34536	40
"""

from math import comb
def H(p, q):
    return comb(p + q - 1, q)

def get_colors(N, K):
    DIV = 1_000_000_003
    if N // K < 2:
        return 0
    if K == 1:
        return N

    between = K - 1
    remain_use = N - between - K
    sub = H(between, remain_use)
    all_use = H(K + 1, remain_use)
    return (all_use - sub) % DIV


def sol():
    N = int(input())
    K = int(input())
    print(get_colors(N, K))

sol()