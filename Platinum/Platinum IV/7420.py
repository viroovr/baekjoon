"""
볼록껍질 문제이고 기하학적으로 생각하면 쉽게 풀만하다.
34536	40
"""

import sys
input = sys.stdin.readline

def ccw(a, b, c):
    return (b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0])

def get_convex_hull(N, points):
    points.sort()
    lower, upper = [], []
    for p in points:
        while len(lower) > 1 and ccw(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    
    for p in reversed(points):
        while len(upper) > 1 and ccw(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    
    return lower[:-1] + upper[:-1]

def dist(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

from math import asin, acos

def theta(a, b, c):
    dp = (b[0] - a[0]) * (c[0] - b[0]) + (b[1] - a[1]) * (c[1] - b[1])
    return acos(dp / (dist(a, b) * dist(b, c)))

def circum(a, b, c, L):
    # t = asin(ccw(a, b, c) / (dist(a, b) * dist(b, c)))
    return L * theta(a, b, c)

def get_barrier(N, L, points):
    convex_hull = get_convex_hull(N, points)
    K = len(convex_hull)
    res = 0
    for i in range(K):
        nxt, nnxt = convex_hull[(i + 1) % K], convex_hull[(i + 2) % K]
        res += dist(convex_hull[i], nxt)
        res += circum(convex_hull[i], nxt, nnxt, L)
    print(f"{res:.0f}")
    
def sol():
    N, L = map(int, input().split())
    points = [tuple(map(int, input().split())) for _ in range(N)]
    get_barrier(N, L, points)

sol()