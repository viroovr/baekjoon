"""
개선된 점
1. is_walkable_road를 더 간결하고 직관적으로 변경
    - ramp_placed 리스트를 True/False로 관리하여 경사로 설치 여부를 체크
    - any()를 활용해 반복문 없이 설치 가능한지 검증
2. 중복 연산 최소화
    - sum()과 리스트 컴프리헨션을 사용해 get_walkable_road()를 단순화
"""

def is_walkable_road(road):
    ramp_placed = [False] * n
    # print(f"row {maps[row]}")
    for col in range(n - 1):
        # print(f"col {col}, puttables {puttables}")
        diff = road[col + 1] - road[col]

        if diff == 0:
            continue
        elif diff == 1:
            if col + 1 - l < 0 or any(ramp_placed[col - i] or road[col - i] != road[col] for i in range(l)):
                return False
            for i in range(l):
                ramp_placed[col - i] = True
        elif diff == -1:
            if col + l >= n or any(ramp_placed[col + i + 1] or road[col + i + 1] != road[col + 1] for i in range(l)):
                return False
            for i in range(1, l + 1):
                ramp_placed[col + i] = True
        else:
            return False

    return True

def get_walkable_road():
    count = sum(is_walkable_road(road) for road in maps)
    transposed_maps = list(zip(*maps))
    count += sum(is_walkable_road(road) for road in transposed_maps)
    return count

def sol():
    global n, l, maps
    n, l = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(n)]
    print(get_walkable_road())

if __name__ == "__main__":
    sol()
    