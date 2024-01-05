import sys
input = sys.stdin.readline
N, M = map(int, input().split())
nums = list(map(int, input().split()))
sums = [0] * N
sums[0] = nums[0]
for i in range(1, N):
    sums[i] = nums[i] + sums[i - 1]
for _ in range(M):
    i, j = map(lambda x: x - 1, map(int, input().split()))
    if i - 1 < 0:
        print(sums[j])
    else:
        print(sums[j] - sums[i - 1])
