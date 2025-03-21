"""
O(N^2)풀이만 알고 있었다면 고민을 오래 했을 문제.
216784	1020
"""

from bisect import bisect_left
import sys
input = sys.stdin.read

def get_lis(N, A):
    dp = []
    lis_index = [-1] * N
    parent = [-1] * N

    for i in range(N):
        pos = bisect_left(dp, A[i])
        if pos == len(dp):
            dp.append(A[i])
        else:
            dp[pos] = A[i]
        
        lis_index[pos] = i
        parent[i] = lis_index[pos - 1] if pos - 1 >= 0 else -1

    print(len(dp))
    idx = lis_index[len(dp) - 1]
    result = []
    while idx >= 0:
        result.append(A[idx])
        idx = parent[idx]
    
    print(*reversed(result))

def sol():
    data = input().strip().split()
    N = int(data[0])
    A = list(map(int, data[1:]))
    get_lis(N, A)

sol()