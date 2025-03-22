"""
dp임을 알고 기억을 더듬으면서 푼듯. 점화식이 왜 그런지 생각해봤다. 해당 문자가
포함되고 안되고 차이로 결정된다.
"""

def get_lcs(s1, s2):
    N, M = len(s1), len(s2)

    dp = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        ch = s1[i - 1]
        for j in range(1, M + 1):
            if ch == s2[j - 1]:
                dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i][j - 1], dp[i - 1][j])
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    # for row in dp:
    #     print(*row)

    result = []
    cnt = dp[-1][-1]
    print(cnt)
    i = N
    j = M
    while i > 0 and j > 0:
        cur = dp[i][j]
        if cur - 1 == dp[i - 1][j - 1] == dp[i - 1][j] == dp[i][j - 1]:
            result.append(s1[i - 1])
            i -= 1
            j -= 1
            continue
        elif cur == dp[i - 1][j]:
            i -= 1
        elif cur == dp[i][j - 1]:
            j -= 1
    print("".join(reversed(result)))

def sol():
    s1 = input()
    s2 = input()
    get_lcs(s1, s2)
sol()