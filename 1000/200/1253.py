from time import time
from bisect import bisect_right, bisect_left
import sys
from random import randint
sys.setrecursionlimit(10**5)
N = int(input())
# N = 2000
numbers = list(map(int, input().split()))
# numbers = [randint(-100000000, 100000000) for _ in range(N)]

good = 0


def search(stindex):
    global good
    if stindex >= N:
        return

    for i in range(N):
        if i == stindex:
            continue
        left = bisect_left(numbers, numbers[stindex] - numbers[i], 0, N)
        right = bisect_right(numbers, numbers[stindex] - numbers[i], 0, N)
        if right - left > 2:
            good += 1
            search(stindex + 1)
            return
        else:
            k = [x for x in range(left, right) if x != i and x != stindex]
            if k:
                good += 1
                search(stindex + 1)
                return
        # for j in range(i + 1, N):
        #     if j == stindex:
        #         continue
        #     if numbers[i] + numbers[j] == numbers[stindex]:
        #         good += 1
        #         search(stindex + 1)
        #         return
    search(stindex + 1)


numbers.sort()
# st = time()
search(0)
print(good)
# end = time()
# print(end-st)
