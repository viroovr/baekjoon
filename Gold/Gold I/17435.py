"""
이전에 tree에서 공통 조상을 찾는 문제를 풀 때, 희소 배열을 이용했었다.
2의 n승 형태로 트리 조상을 탐색하며 logN의 시간복잡도로 찾는데, 그걸 이 문제에도 이용했다.

dp의 행열을 바꿔서 dp를 선언해 이전 인덱스에서 값들을 채우도록 변경했다.

101864	2220
83848	1468
"""

import sys
input = sys.stdin.readline

def build_dp(parent):
    dp = [parent]

    for j in range(18):
        dp.append([dp[-1][x] for x in dp[-1]])
    
    return dp

def get_fn_x(n, x):
    i = 0
    while n > 0:
        if n & 1:
            x = dp[i][x]
        
        n >>= 1
        i += 1

    return x
            
def sol():
    global dp
    m = int(input())
    parent = [-1] + list(map(int, input().rstrip().split()))
    Q = int(input())

    dp = build_dp(parent)

    result = []
    for _ in range(Q):
        result.append(get_fn_x(*map(int, input().rstrip().split())))
    
    print("\n".join(map(str, result)))

sol()
