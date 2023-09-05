from itertools import combinations
from math import dist
import sys

input = sys.stdin.readline
# import math
# a, b,     c, d,   e, f,  g, h
# a-c b-d, e-g f-h
# a+g-c-e, b+f-d-h

# a-e b-f, c-g d-h
# a+c-g-e, b+h-f-d

# a-g b-h, c-e d-f
# a+e-g-c, b+f-d-h
# print(sum(1 for _ in combinations(range(20), 10)))
from random import randint
T = int(input())
for _ in range(T):
    N = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]
    # points = [tuple(map(int, [randint(-10,10), randint(-10,10)])) for _ in range(N)]
    ans = dist((-100_000, -100_000), (100_000, 100_000))
    for c1 in combinations(points, len(points) // 2):
        x = tuple(map(sum, zip(*c1)))
        y = tuple(map(sum, zip(*[a for a in points if a not in c1])))
        # x, y = (sum(x)-sum(y) for x, y in zip(*c1), zip(*[a for a in points if a not in c1]))
        # ans = min(ans, dist((c1x, c1y), (c2x, c2y)))
        ans = min(ans, dist(x, y))
    print(ans)
    # print(points)
