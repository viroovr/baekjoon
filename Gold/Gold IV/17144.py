"""
1. 딕셔너리(Counter) vs 리스트의 메모리 할당 방식 차이
    - Counter는 내부적으로 해시 테이블을 사용해서 키-값을 저장해.
    - 하지만 해시 테이블은 충돌 방지를 위한 추가 연산이 필요하기 때문에, 리스트보다 약간 더 느릴 수 있어.
    - 반면, 2D 리스트는 미리 할당된 메모리 공간에 직접 접근하기 때문에 연산이 더 빠름.
2. Counter는 동적 해시 연산이 필요함
    - Counter[(x, y)] += value 를 실행하면:
        - (x, y)라는 튜플 해싱 연산이 수행됨. (추가적인 CPU 연산 발생)
        - 내부적으로 키 충돌을 해결하는 과정이 있을 수 있음.
    - 반면 diffuse[x][y] += value는 인덱스 연산만 수행하므로 해시 충돌을 걱정할 필요가 없음.
3. 리스트는 캐시 적중률(Cache Hit Rate)이 높음
    - 2D 리스트는 연속된 메모리 블록에 저장되어 있어서 CPU 캐시를 더 효율적으로 사용할 수 있음.
    - 하지만 Counter는 해시 테이블이기 때문에 메모리가 랜덤하게 할당되며, CPU 캐시 효율이 떨어짐.
"""

from sys import stdin
input = stdin.readline
directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def logging(room):
    for r in range(R):
        print(*room[r])
    print("=========")

def get_remaining_dusts(room, filter_first_row, T):
    filter_second_row = filter_first_row + 1
    diffuse = [[0] * C for _ in range(R)]
    while T > 0:
        T -= 1
        for r in range(R):
            for c in range(C):
                if room[r][c] <= 0:
                    continue
                new_diffusion_amount = room[r][c] // 5
                if new_diffusion_amount > 0:
                    cnt = 0
                    for dc, dr in directions:
                        nc, nr = dc + c, dr + r
                        if 0 <= nc < C and 0 <= nr < R and room[nr][nc] != -1:
                            diffuse[nr][nc] += new_diffusion_amount
                            cnt += 1
                    room[r][c] -= new_diffusion_amount * cnt

        for r in range(R):
            for c in range(C):
                room[r][c] += diffuse[r][c]
                diffuse[r][c] = 0
                
        # print("after diffusing")
        # logging(room)

        for r in range(filter_first_row - 1, -1, -1):
            room[r][0] = room[r - 1][0]
        for c in range(C - 1):
            room[0][c] = room[0][c + 1]
        for r in range(filter_first_row):
            room[r][C - 1] = room[r + 1][C - 1]
        for c in range(C - 1, 1, -1):
            room[filter_first_row][c] = room[filter_first_row][c - 1]
        room[filter_first_row][1] = 0

        for r in range(filter_second_row + 1, R - 1):
            room[r][0] = room[r + 1][0]
        for c in range(C - 1):
            room[R - 1][c] = room[R - 1][c + 1]
        for r in range(R - 1, filter_second_row, -1):
            room[r][C - 1] = room[r - 1][C - 1]
        for c in range(C - 1, 1, -1):
            room[filter_second_row][c] = room[filter_second_row][c - 1]
        room[filter_second_row][1] = 0

        # print("after filtering")
        # logging(room)

    return sum(sum(row) for row in room) + 2

def sol():
    global R, C
    R, C, T = map(int, input().split())
    room = [list(map(int, input().split())) for _ in range(R)]
    
    for r in range(R):
        if room[r][0] == -1:
            print(get_remaining_dusts(room, r, T))
            break

sol()
