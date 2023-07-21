from itertools import combinations
import sys
input = sys.stdin.readline
height = [int(input()) for _ in range(9)]
for i in combinations(height, 7):
    if sum(i) == 100:
        for k in sorted(i):
            print(k)
        break
