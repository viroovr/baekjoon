"""
시작점을 0으로 고정해도, 한번 방문한 곳을 다시 방문하지 않고 싸이클이란 특성에 기반해서
동일한 정답이 나온다.
이를 적용해 시작점을 dp에 저장하지 않고 다시 풀었다.

tuple 인덱싱 연산과 조건문이 줄어들어 시간이 단축 되고, 메모리 사용량이 절반 줄어든다.

129216	1808    i!=j일때 W[i][j] = INF로 초기화
129216	1936    INF초기화 없애고 W[i][j] > 0로 갈 수 있는지 조건확인
53440	704     0을 시작점으로 두고 풂. 다른 시작점들에서도 출발했을때의 연산들이 제거됨.
"""
import sys
input = sys.stdin.readline

def get_min_cost(N, W):
    INF = int(1e8)
    dp = [[INF] * N for _ in range(1 << N)]
    dp[1][0] = 0

    for mask in range(1, 1 << N):
        for start in range(N):
            if dp[mask][start] == INF:
                continue

            for end in range(N):
                if mask & (1 << end) == 0 and W[start][end] > 0:
                    next_mask = 1 << end | mask
                    dp[next_mask][end] = min(dp[next_mask][end], dp[mask][start] + W[start][end])
    
    result = INF
    final_mask = (1 << N) - 1
    for start in range(N):
        if W[start][0] > 0:
            result = min(dp[final_mask][start] + W[start][0], result)
    
    print(result)

def sol():
    N = int(input())
    W = [list(map(int, input().split())) for _ in range(N)]
    get_min_cost(N, W)

sol()