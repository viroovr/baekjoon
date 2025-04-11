"""
같은 변위에 있을 경우, 외적이 0이될 수 있음을 놓쳤다.
32412	36
"""

def can_eat(points):
    x3, y3 = points[4] - points[0], points[5] - points[1]
    x2, y2 = points[2] - points[0], points[3] - points[1]
    x4, y4 = points[6] - points[0], points[7] - points[1]

    d0 = x3*y2 - x2*y3
    d1 = x2*y4 - x4*y2
    if d0 * d1 <= 0:
        print(0)
    else:
        print(1)

def sol():
    points = list(map(int, input().split()))
    can_eat(points)

sol()