"""
✅ 최적화 포인트
1. map_direction 함수 제거
    +는 1, -는 -1로 변환하는 단순한 함수이므로, direction = 1 if direction == "+" else -1 로 인라인 처리.
2. rotate_side 함수 최적화
    - 회전 방향을 결정할 때 cnt % 4만큼만 반복.
    - zip(*matrix[::-1])을 활용해 90도 회전 최적화.
3. deque 활용 최소화
    - tmp를 deque 대신 리스트로 처리하고 직접 인덱스를 변경.
메모리(KB)	시간(ms)    구현차이
35084   	1300	    reversed/zip(*cubeside), deque.rotate, map_direction
32412       828         zip(*reversed(cube_side)), indexing
32412   	772         zip(*cube_side[::-1]), indexing
"""
def rotate_side(cube_side, cnt):
    for _ in range(cnt % 4):
        cube_side = [list(row) for row in zip(*cube_side[::-1])]
    return cube_side
    
def logging(cubes, side):
    for i in range(3):
        print("".join(cubes[side][i]))

def up_color(n, rotating_methods):
    cubes = {
        "U": [['w' for _ in range(3)] for _ in range(3)],
        "D": [['y' for _ in range(3)] for _ in range(3)],
        "F": [['r' for _ in range(3)] for _ in range(3)],
        "B": [['o' for _ in range(3)] for _ in range(3)],
        "L": [['g' for _ in range(3)] for _ in range(3)],
        "R": [['b' for _ in range(3)] for _ in range(3)]
    }

    # index 증가 반시계 방향 (-)
    rotating_map = {
        "U" : ["F", "R", "B", "L"],
        "D" : list(reversed(["F", "R", "B", "L"])),
        "B" : ["U", "R", "D", "L"],
        "F" : list(reversed(["U", "R", "D", "L"])),
        "L" : ["U", "B", "D", "F"],
        "R" : list(reversed(["U", "B", "D", "F"]))
    }

    rotating_counts = {
        "U": [0] * 4, 
        "D": [2] * 4, 
        "B": [0, 3, 2, 1], 
        "F": [3, 0, 1, 2], 
        "L": [1, 3, 1, 1], 
        "R": [3, 3, 1, 3]
    }

    for method in rotating_methods:
        side, direction = method[0], 1 if method[1] == "+" else -1

        cubes[side] = rotate_side(cubes[side], direction)

        tmp = []
        for i in range(4):
            cubes[rotating_map[side][i]] = rotate_side(cubes[rotating_map[side][i]], rotating_counts[side][i])
            tmp.append(cubes[rotating_map[side][i]][0][:])

        tmp = tmp[direction:] + tmp[:direction]

        for i in range(4):
            cubes[rotating_map[side][i]][0] = tmp[i]
            cubes[rotating_map[side][i]] = rotate_side(cubes[rotating_map[side][i]], 4 - rotating_counts[side][i])

    logging(cubes, "U")

def sol():
    T = int(input())
    for _ in range(T):
        n = int(input())
        rotating_methods = input().split()
        up_color(n, rotating_methods)

sol()