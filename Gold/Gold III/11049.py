"""
pypy로 제출해야 하기.. knuth optimazation이 적용이 안되는 문제다.
마지막 비용 계산이 어느 mid를 선택하는지에 따라 다르기 때문에,
opt내 mid값이 이후 range계산 사용에 안된다.

1.side 미리 계산
2.sol 함수제거
3.input
4.min_val로 dp 최종 업데이트
113988	976
112812	460 1,3,4
112812	452 1,2,3,4
"""
import sys
INF = sys.maxsize
input = sys.stdin.readline

def get_min_operation(N, matrixes):
    dp = [[0] * N for _ in range(N)]

    for length in range(2, N + 1):
        for start in range(N - length + 1):
            end = start + length - 1
            min_val = INF
            side = matrixes[start][0] * matrixes[end][1]

            for mid in range(start, end):
                min_val = min(dp[start][mid] + dp[mid + 1][end] + matrixes[mid][1] * side, min_val)
                
            dp[start][end] = min_val

    return dp[0][N - 1]


def sol():
    N = int(input())
    matrixes = [tuple(map(int, input().split())) for _ in range(N)]
    print(get_min_operation(N, matrixes))

sol()