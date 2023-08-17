from math import dist
import sys
input = sys.stdin.readline


def is_inside(point, circle):
    return dist((circle[0], circle[1]), (point[0], point[1])) < circle[2]


T = int(input())
for _ in range(T):
    count = 0
    x1, y1, x2, y2 = map(int, input().split())
    planet = [tuple(map(int, input().split())) for _ in range(int(input()))]
    for c in planet:
        t1 = is_inside((x1, y1), c)
        t2 = is_inside((x2, y2), c)
        if (t1 and not t2) or (not t1 and t2):
            count += 1
    print(count)
    # print(planet)
