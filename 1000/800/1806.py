# 부분합
from bisect import bisect_left, bisect_right
N, S = map(int, input().split())
array = list(map(int, input().split()))
partial_sum = [0] * N
partial_sum[0] = array[0]
for i in range(N - 1):
    partial_sum[i + 1] = partial_sum[i] + array[i + 1]
ret = 123_456
for i, x in enumerate(array):
    left = bisect_left(partial_sum, S - x + partial_sum[i], i, N)
    right = bisect_right(partial_sum, S - x + partial_sum[i], i, N)
    if left >= N:
        break
    if left == right:
        ret = min(ret, right - i + 1)
    else:
        ret = min(ret, right - i)
if ret == 123_456:
    print(0)
else:
    print(ret)
