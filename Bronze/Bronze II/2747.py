def fib(n):
    dp = [0, 1]
    for _ in range(n):
        dp.append(dp[-1] + dp[-2])
    return dp[n]

print(fib(int(input())))