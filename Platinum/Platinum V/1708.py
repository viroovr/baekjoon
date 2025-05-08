"""
볼록 껍질을 알아내는 문제. 아이디어는 각으로 접근하고 차례차례 해야하는것은 알았지만
단순한 적용법에 접근하지 못했다.

각 순서대로 정렬하고 같은 각이면 가까운 점들을 정렬하도록 한다.
이후에, 순서대로 stack에 담겨있는 볼록 껍질 점들을 기준으로 ccw를 판단하며 접근한다.

64296	364
"""

from math import atan2
import sys
input = sys.stdin.readline

def ccw(x1, y1, x2, y2, x3, y3):
    res = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    if res < 0:
        return -1
    elif res > 0:
        return 1
    return 0

def get_convex_hull(N, grids):
    x0, y0 = min(grids, key = lambda p : (p[1], p[0]))
    sg = list(sorted(grids, key=lambda p: (atan2(p[1] - y0, p[0] - x0), (p[0] - x0)**2 + (p[1] - y0)**2)))
    convex_points = [sg[0], sg[1]]
    for i in range(2, N):
        while len(convex_points) > 1 and ccw(*convex_points[-2], *convex_points[-1], *sg[i]) <= 0:
            convex_points.pop()
        convex_points.append(sg[i])
    
    print(len(convex_points))

def sol():
    N = int(input())
    grids = [tuple(map(int, input().rstrip().split())) for _  in range(N)]
    get_convex_hull(N, grids)

sol()