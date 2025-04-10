"""
처음엔 첫 직선을 기반으로 세번 째 점의 위치에 따라 부호를 나눴는데,
기울기를 이용할 때, float 연산 정밀도와 0일 때 처리에 에러가 있었다.
따라서 theta에 대해 알아보려는데, 내적은 스칼라 값이므로 방향에 대한 정보를 얻을 수 없었다.
sin을 이용할 텐데, 외적이 생각났다. 외적구하는 방법을 구글링 해서 계산

32412	44
"""

def get_ccw(dots):
    x1, y1 = (dots[1][0] - dots[0][0], dots[1][1] - dots[0][1])
    x2, y2 = (dots[2][0] - dots[1][0], dots[2][1] - dots[1][1])

    s = x1 * y2 - x2 * y1
    return s // abs(s) if s != 0 else 0

def sol():
    dots = [tuple(map(int, input().split())) for _ in range(3)]
    print(get_ccw(dots))
sol()