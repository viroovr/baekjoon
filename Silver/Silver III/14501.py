def get_max_profit(n, T, P):
    dp = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        time, pay = T[i], P[i]
        end_day = time + i
        if end_day > n:
            dp[i] = dp[i + 1]
        else:
            dp[i] = max(dp[end_day] + pay, dp[i + 1])
    return dp[0]
        
def sol():
    n = int(input())
    T, P = [], []
    for _ in range(n):
        t, p = map(int, input().split())
        T.append(t)
        P.append(p)
    print(get_max_profit(n, T, P))
    
if __name__ == "__main__":
    t = 0
    if t == 1:
        test_fun()
    else:
        sol()