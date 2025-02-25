"""
1. rotate_right_tanks() 개선
    horizon과 vertical 증가 로직 개선
1. make_one_line_tanks() 개선
    extend()를 직접 활용하여 성능을 향상시킵니다.
3. 불필요한 리스트 변환 제거
    list(deque) 변환을 최소화하여 deque의 성능을 유지합니다.
4. deltas 제거
    tanks 복사 배열에서 delta값 바로 적용
"""
from collections import deque

def rotate_right_tanks(tanks):
    stacks = deque([[i] for i in tanks])
    horizon, vertical = 1, 1
    # 1,1 1,2 2,2 2,3 3,3
    while len(stacks) - horizon >= vertical:
        new_st = [deque() for _ in range(vertical)]

        for _ in range(horizon):
            st = stacks.popleft()
            for v in range(vertical):
                new_st[v].append(st[v])

        for v in range(vertical):
            stacks[v].extend(reversed(new_st[v]))

        if horizon == vertical:
            vertical += 1
        else:
            horizon += 1
    return stacks, list(map(len, stacks))


directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def adjust_fishes(rotated_tanks, degrees):
    R = len(degrees)
    deltas = [[0] * degrees[r] for r in range(R)]

    for r in range(R):
        for c in range(degrees[r]):
            cur_temp = rotated_tanks[r][c]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < degrees[nr] and cur_temp > rotated_tanks[nr][nc]:
                    diff = (cur_temp - rotated_tanks[nr][nc]) // 5
                    if diff > 0:
                        deltas[r][c] -= diff
                        deltas[nr][nc] += diff
    
    for r in range(R):
        for c in range(degrees[r]):
            rotated_tanks[r][c] += deltas[r][c]

    return rotated_tanks

def make_one_line_tanks(tanks):
    return [fish for row in tanks for fish in row]

def rotate_right_horizontally(tanks):
    stacks = deque([[i] for i in tanks])
    for i in [2, 4]:
        for j in range(len(tanks) // i):
            stacks[-1 - j].extend(reversed(stacks.popleft()))
    return stacks, list(map(len, stacks))

# print(rotate_right_tanks([5,3,3,14,9,3,11,8]))
# print(adjust_fishes([[9, 14, 3], [3, 5, 3], [11], [8]], [3, 3, 1, 1]))
# print(make_one_line_tanks([[9, 10, 5], [5, 6, 3], [10], [8]]))
# N = 8
# print(rotate_right_horizontally([9, 10, 5, 5, 6, 3, 10, 8]))

def get_difference(tanks):
    count = 0
    while True:
        min_val, max_val = min(tanks), max(tanks)
        if max_val - min_val <= K:
            return count

        for i in range(len(tanks)):
            if min_val == tanks[i]:
                tanks[i] += 1
        
        rotated_tanks, degrees = rotate_right_tanks(tanks)
        adjusted_tanks = adjust_fishes(rotated_tanks, degrees)
        rotated_tanks, degrees = rotate_right_horizontally(make_one_line_tanks(adjusted_tanks))
        adjusted_tanks = adjust_fishes(rotated_tanks, degrees)
        tanks = make_one_line_tanks(adjusted_tanks)

        count += 1

def sol():
    global N, K
    N, K = map(int, input().split())
    tanks = list(map(int, input().split()))
    print(get_difference(tanks))

sol()