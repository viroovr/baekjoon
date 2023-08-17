from math import dist
from sys import stdin

input = stdin.readline

T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = dist((x1, y1), (x2, y2))

    if d == 0:
        if abs(r1 - r2) == 0:
            print(-1)
        else:
            print(0)
    else:
        if d == abs(r1 + r2) or d == abs(r1 - r2):
            print(1)
        elif d > abs(r1 + r2) or d < abs(r1 - r2):
            print(0)
        else:
            print(2)
    
