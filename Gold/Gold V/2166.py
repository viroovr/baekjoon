"""
다각형이란 일반적으로 자기교차하지 않는 다각형을 말한다고 한다.
그리고 무게중심은 항상 다각형 내부에 존재하는 것이 아니다. 오목 다각형의 경우
외부에 존재할 수 있다.

따라서 외적으로 삼각형의 넓이를 더할 때 음수, 양수를 고려해 풀어야한다.
34456	44
"""
import sys
input = sys.stdin.readline

def get_area(N, points):
    wx, wy = map(lambda x: sum(x), zip(*points))
    res = 0
    for i in range(-1, N - 1):
        x1, y1 = (points[i][0] * N - wx, points[i][1] * N - wy)
        x2, y2 = (points[i + 1][0] * N - wx, points[i + 1][1] * N - wy)
        res += x1 * y2 - x2 * y1
    return f"{abs(res/(N**2 * 2)):.1f}"
def sol():
    N = int(input())
    points = [tuple(map(int, input().rstrip().split())) for _ in range(N)]
    print(get_area(N, points))

sol()