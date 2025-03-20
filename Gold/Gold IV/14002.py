"""
기존 O(N^2) 코드를 짰다. dp[i]에 A[i]까지의 가장 긴 부분 수열의 길이를 저장하고
이를 다시 돌아가면서 dp 최댓값에서 시작해 값이 작으면서 수열길이도 1개적은 값을 골라 출력했다.
O(NlogN) 풀이를 이용해서, dp에 증가하는 수열을 이진탐색을 이용해 갱신하고, 
lis_index에 해당 dp 인덱스의 위치에 해당 값의 A 인덱스를 저장했다.
그리고 parent 도 두어 역추적이 가능하도록 했다.
32412	68
32412	40
"""

import sys
input = sys.stdin.readline
def bisect_left(A, x):
    left, right = 0, len(A)
    while left < right:
        mid = (left + right) // 2
        if A[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left

def get_lis(N, A):
    dp = []
    lis_index = [-1] * N
    parent = [-1] * N

    for i in range(N):
        idx = bisect_left(dp, A[i])
        if idx == len(dp):
            dp.append(A[i])
        else:
            dp[idx] = A[i]
        
        lis_index[idx] = i
        parent[i] = lis_index[idx - 1] if idx > 0 else -1

    lis_length = len(dp)
    print(lis_length)

    lis_sequence = []
    idx = lis_index[lis_length - 1]
    while idx != -1:
        lis_sequence.append(A[idx])
        idx = parent[idx]
    print(*reversed(lis_sequence))

def sol():
    N = int(input().strip())
    A = list(map(int, input().strip().split()))
    get_lis(N, A)

sol()