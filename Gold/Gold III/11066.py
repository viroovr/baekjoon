"""
처음에 연속된 파일을 합치는 줄 모르고 항상 두 파일의 합 중 최소값을 찾아 더하는 방식 -> 틀림
Top-Down 방식의 DP로 해결 K^3 -> 시간초과
Prefix_sum 도 미리 저장해 DP 해결 K^3 시간초과
결국 gpt의 도움으로 knuth's optimaztion을 활용
-> opt배열을 선언해서 최소 비용 구간을 나누는 index를 저장. 이를 활용하여
Bottom-up으로 DP 생성. 
42556	648

일반적인 DP (모든 mid 탐색)	O(K³)   모든 구간에서 모든 분할점 탐색
Knuth's Optimization 적용	O(K³)보다 작음 (~ O(K² logK))	mid 탐색 범위 축소
Knuth's Optimization은 완벽한 O(K²)이 아니지만, O(K³)보다 훨씬 적은 연산을 수행할 수 있도록 최적화된 방법입니다.
따라서 O(K² logK) ~ O(K³) 정도의 복잡도를 가진다고 보는 것이 가장 적절함!
"""
def get_min_cost(K, files):
    dp_sum = [0] * (K + 1)
    for i in range(K):
        dp_sum[i + 1] = dp_sum[i] + files[i]
            
    dp = [[0] * K for _ in range(K)]
    opt = [[0] * K for _ in range(K)]

    for length in range(2, K + 1):
        for start in range(K - length + 1):
            end = start + length - 1
            dp[start][end] = float("inf")
            
            lo = opt[start][end - 1] if start < end -1 else start
            hi = opt[start + 1][end] if start + 1 < end else end

            for mid in range(lo, hi + 1):
                if mid + 1 >= end:
                    cost = dp[start][mid] + (dp_sum[end + 1] - dp_sum[start])
                else:
                    cost = dp[start][mid] + dp[mid + 1][end] + (dp_sum[end + 1] - dp_sum[start])
                if cost < dp[start][end]:
                    dp[start][end] = cost
                    opt[start][end] = mid
    # print("====")
    # for row in dp:
    #     print(*row)
    # print("====")              
    # for row in opt:
    #     print(*row)                    
    return dp[0][K - 1]

def sol():
    T = int(input())
    for _ in range(T):
        K = int(input())
        files = list(map(int, input().split()))
        print(get_min_cost(K, files))
sol()