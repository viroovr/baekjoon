# from math import log2 as log
from heapq import heappush, heappop
from sys import stdin
input = stdin.readline
N = int(input())
nums = []
# print(100_000 ** 2 * log2(100_000))
q = 1
leftHeap = []
rightHeap = []
L = []
for i in range(N):
    L.append(int(input()))
mid = L[0]
answer = [mid]
for i in range(1, N):
    num = L[i]
    if mid <= num:
        heappush(rightHeap, num)
    else:
        heappush(leftHeap, -num)

    if (i + 1) % 2 == 0:
        if len(leftHeap) > len(rightHeap):
            heappush(rightHeap, mid)
            mid = -heappop(leftHeap)
    else:
        if len(leftHeap) + 2 == len(rightHeap):
            heappush(leftHeap, -mid)
            mid = heappop(rightHeap)
    print(leftHeap, rightHeap)
    answer.append(mid)

for a in answer:
    print(a)
# for i in range(1, N + 1):
#     k = int(input())
#     heappush(nums, k)
#     if 2 ** (q + 1) - 1 > i >= 2 ** q - 1:
#         if i <= 2 ** q:
#             print(min(nums[2 ** (q - 1) - 1: 2 ** q - 1]))
#             # print(i, int(log(q)),  int(log(q * 2)), q)
#         else:
#             print(max(nums[2 ** (q - 1) - 1: 2 ** q - 1]))
#             # print(i, int(log(q)),  int(log(q * 2)), q)
#     elif i == 2 ** (q + 1) - 1:
#         q += 1
#         print(min(nums[2 ** (q - 1) - 1: 2 ** q - 1]))
#         # print(i, int(log(q)),  int(log(q * 2)), q)
