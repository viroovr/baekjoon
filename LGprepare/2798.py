from sys import stdin
from itertools import combinations
input = stdin.readline
N, M = map(int, input().split())
cards = list(map(int, input().split()))
ans = 0
for comb in combinations(cards, 3):
    t = sum(comb)
    if t <= M:
        ans = max(ans, t)
print(ans)
