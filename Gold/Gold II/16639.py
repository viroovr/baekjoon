"""
이전에 덧셈의 최댓값을 구하는 문제를 떠올리며 dp를 적용해 풀었다.
이 문제는 +, -, * 이 모두 존재하기 때문에, 최솟값도 따로 dp를 두어야 최댓값을
구할 수 있다.

결국 순차적으로 a 와 b를 계산하기 때문에 부분 최적해가 최적해를 이루게된다.

32412	40
"""

def op(a, b, e):
    if e == "+":
        return a + b
    elif e == "*":
        return a * b
    return a - b

def get_max_result(N, expression):
    n = N // 2 + 1
    dp = [[0] * n for _ in range(n)]
    min_dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = int(expression[i * 2])
        min_dp[i][i] = int(expression[i * 2])
    
    for length in range(1, n):
        for start in range(n - length):
            end = start + length
            
            max_val = float("-inf")
            min_val = float("inf")
            for i in range(length):
                e = expression[(end - length + i) * 2 + 1]
                a, b = dp[start][end - length + i], dp[start + i + 1][end]
                a_, b_ = min_dp[start][end - length + i], min_dp[start + i + 1][end]
                max_val = max(op(a, b, e), op(a_, b_, e), op(a_, b, e), op(a, b_, e), max_val)
                min_val = min(op(a, b, e), op(a_, b_, e), op(a_, b, e), op(a, b_, e), min_val)

            dp[start][end] = max_val
            min_dp[start][end] = min_val

    print(dp[0][n - 1])

def sol():
    N = int(input())
    expression = list(input())
    get_max_result(N, expression)

sol()