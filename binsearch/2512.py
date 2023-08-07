import sys

input = sys.stdin.readline
N = int(input())
budget = list(map(int, input().split()))
M = int(input())
# print(N, budget, M)

lo = 0
hi = max(budget)
mid = (lo + hi) // 2

ans = 0


def is_possible(mid):
    return sum(min(r, mid) for r in budget) <= M


while lo <= hi:
    # print(lo, mid, hi, ans)
    if is_possible(mid):
        lo = mid + 1
        ans = mid
    else:
        hi = mid - 1

    mid = (lo + hi) // 2

print(ans)
# 110, 120, 140, 150 / 485
