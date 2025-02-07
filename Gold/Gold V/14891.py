"""
🔹 최적화 요약
1. 불필요한 .popleft() 제거
    - 기존 코드에서는 .popleft()를 통해 점수를 계산했지만, 이는 deque의 요소를 제거하는 비효율적인 방법이었음
    - 최적화 코드에서는 gears[i][0]을 직접 사용해 점수를 계산
2. rotate() 함수 분리
    - 기어 회전 기능을 별도 함수로 분리하여 가독성 향상 & 중복 코드 제거
3. moving_method를 deque 대신 list로 변경
    - 입력이 크지 않다면 deque보다는 리스트 순회가 더 빠름
    - deque.popleft()를 제거하고 for 루프에서 직접 순회하는 방식으로 변경
4. rotate(1), rotate(-1)를 활용해 append/pop 보다 빠르게 회전 적용

메모리(KB)  시간(ms)
35016	    68
34992	    64
"""
from collections import deque

RIGHT_TOUCHED_INDEX = 2
LEFT_TOUCHED_INDEX = 6
directions = ["", "시계방향", "반시계방향"]

def log_gears(gears):
    for i in range(4):
        print(*gears[i])

def rotate(gear, direction):
    if direction == 1:
        gear.rotate(-1)
    else:
        gear.rotate(1)

def get_gears_score(gears, k, moving_method):
    for gear_index, direction in moving_method:
        gear_index -= 1

        # log_gears(gears)
        # print(f"gear_index = {gear_index}, direction: {directions[direction]}")

        rotate(gears[gear_index], -direction)

        left, left_direction = gear_index - 1, direction
        while left >= 0 and gears[left][RIGHT_TOUCHED_INDEX] != gears[left + 1][LEFT_TOUCHED_INDEX + left_direction]:
            rotate(gears[left], left_direction)
            left_direction *= -1
            left -= 1
        
        right, right_direction = gear_index + 1, direction
        while right < 4 and gears[right - 1][RIGHT_TOUCHED_INDEX + right_direction] != gears[right][LEFT_TOUCHED_INDEX]:
            rotate(gears[right], right_direction)
            right_direction *= -1
            right += 1
        
    # print(f"end status {log_gears(gears)}")
    return sum(gears[i][0] * (2**i) for i in range(4))

def sol():
    gears = [deque(map(int, input())) for _ in range(4)]
    K = int(input())
    moving_method = [tuple(map(int, input().split())) for _ in range(K)]
    print(get_gears_score(gears, K, moving_method))


if __name__ == "__main__":
    sol()