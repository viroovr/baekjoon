"""
최적화 포인트 정리
1. 드래곤 커브 생성 최적화
    - 기존 코드에서 리스트 복사 후 역순으로 변환하는 대신, (dx, dy) → (-dy, dx) 공식을 적용해 간결하게 처리.
    - list의 reversed()를 활용해 가독성 유지.
2. direction_map 제거
    - 불필요한 direction_map을 제거하고, 방향 회전을 직접 계산.
3. 격자 업데이트 분리
    - draw_dragon_curve() 함수를 통해 코드 구조를 단순화.
4. 정사각형 개수 세기 최적화
    - sum()을 활용한 리스트 컴프리헨션 방식으로 불필요한 if 문을 제거하여 성능 향상
"""

from collections import defaultdict

# 동, 북, 서, 남
directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
dragon_map = defaultdict(list)

def make_dragon_map():
    for g in range(11):
        if g == 0:
            dragon_map[0].append((1, 0))
        else:
            prev_curve = dragon_map[g - 1]
            new_curve = prev_curve[:]
            new_curve.extend((dy, -dx) for dx, dy in reversed(prev_curve))

            dragon_map[g] = new_curve
    
def rotate_delta(dx, dy, d):
    rotate_map = [
        (dx, dy),
        (dy, -dx),
        (-dx, -dy),
        (-dy, dx)
    ]
    return rotate_map[d]

def draw_dragon_curves(grids, x, y, d, g):
    grids[y][x] = 1
    for dx, dy in dragon_map[g]:
        Dx, Dy = rotate_delta(dx, dy, d)
        x, y = x + Dx, y + Dy
        grids[y][x] = 1

def count_squares(grids):
    return sum(
        grids[i][j] and grids[i + 1][j] and grids[i][j + 1] and grids[i + 1][j + 1]
        for i in range(m - 1) for j in range(m - 1)
    )
             
def sol():
    global n, m, dragon_curves, grids
    n = int(input())
    m = 101
    dragon_curves = [list(map(int, input().split())) for _ in range(n)]
    grids = [[0] * m for _ in range(m)]

    make_dragon_map()

    for x, y, d, g in dragon_curves:
        draw_dragon_curves(grids, x, y, d, g)

    print(count_squares(grids))
    
sol()