from bisect import bisect_left, bisect_right

N = int(input())
card = sorted(list(map(int, input().split())))
M = int(input())
comparecard = list(map(int, input().split()))
# print(N, card, M, comparecard)
ans = []

for x in comparecard:
    r = bisect_right(card, x)
    l = bisect_left(card, x)
    ans.append(1 if r - l else 0)
    # if n == 1:
    #     print(1, end=" ")
    # else:
    #     print(0, end=" ")
print(*ans)
