"""
점들이 주어질 때, 점들간의 거리가 최대인 거리를 구하는 문제다.
점들 간의 거리가 최대이려면 일단, 볼록 껍질에 있는 점들 사이의 거리이여야 한다.
볼록 껍질에 있지 않은 점이 최대 거리라면, 그것보다 큰 거리의 볼록껍질에 있는 점과의 거리가
존재하므로 모순이다.

첫번재 풀이는 이렇다.
볼록 껍질을 Graham Scan을 통해 각도를 기준으로 정렬한다.
그리고 맞은 편에 있는 점들이 최대 거리임을 이용해서 구했다.
62488	320

그러나 정석적인 풀이는 rotating calipers를 이용하는 풀이이다.
이번에는, 볼록 껍질을 Andrew's Monotone Chain을 이용해서 upper 껍질과 lower껍질을
각각 구해 합쳤다. 
그리고 투 포인터를 활용해, 현재 i 점과 k 점과 거리 최댓값을 투 포인터를 이용해 갱신한다.
45480	308
"""
import sys
input = sys.stdin.readline
from math import atan2


def get_dist(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

def ccw(a, b, c):
    return (b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0])

def rotating_calipers(convex_hull):
    n = len(convex_hull)
    if n == 2:
        return get_dist(convex_hull[0], convex_hull[1])

    k = 1
    max_dist = 0
    for i in range(n):
        while True:
            nxt = (k + 1) % n
            if get_dist(convex_hull[i], convex_hull[nxt]) > get_dist(convex_hull[i], convex_hull[k]):
                k = nxt
            else:
                break
        max_dist = max(max_dist, get_dist(convex_hull[i], convex_hull[k]))
    
    return max_dist


def get_max_distant(C, points):
    points.sort()
    upper, lower = [], []

    for p in points:
        while len(lower) > 1 and ccw(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    for p in reversed(points):
        while len(upper) > 1 and ccw(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    convex_hull = lower[:-1] + upper[:-1]
    print(f"{rotating_calipers(convex_hull):.7f}")

def sol():
    C = int(input())
    points = [tuple(map(int, input().rstrip().split())) for _ in range(C)]

    get_max_distant(C, points)

sol()