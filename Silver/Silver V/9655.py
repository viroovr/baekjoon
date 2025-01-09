n = int(input())
dp = [0] * 1001
dp[1] = 1
dp[2] = 2
dp[3] = 1
dp[4] = 2
dp[5] = 1
for i in range(6, 1001):
    if dp[i - 1] != dp[i - 3]:
        dp[i] = 1
    else:
        if dp[i - 1] == 1:
            dp[i] = 2
        else:
            dp[i] = 1
print("SK" if dp[n] == 1 else "CY")
