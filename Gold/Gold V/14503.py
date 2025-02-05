"""
최적화 포인트:
BFS 대신 반복문 활용:
    큐(deque)를 사용하지 않고, while True로 반복을 돌며 직접 이동하도록 변경하여 연산을 줄임.
불필요한 변수 제거:
    has_can_clean_room을 사용하지 않고, 청소 가능한 공간이 있으면 바로 이동.
    ret(청소한 칸 수)를 room 배열에 2로 표시하면서 직접 카운팅.
배열 접근 최적화:
    (y + dy, x + dx)를 매번 계산하는 대신, 반복문에서 dy, dx를 캐싱.
"""

from collections import deque

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
nesw = ["NORTH", 'EAST', 'SOUTH', 'WEST']
def get_cleaned_num(n, m, x, y, d, room):
    cleaned_count = 0

    while True:
        if room[y][x] == 0:
            room[y][x] = 2
            cleaned_count += 1
        # print(f"x : {x}, y {y}, {nesw[d]}")
        dy, dx = directions[d]
        for i in range(4):
            d = (d - 1) % 4
            ny, nx = y + directions[d][0], x + directions[d][1]
            if room[ny][nx] == 0:
                y, x = ny, nx
                break
        else:
            # print(f"{nesw[d]}, rear : {nesw[(d + 2) % 4]}")
            ny, nx = y - directions[d][0], x - directions[d][1]
            if room[ny][nx] == 1:
                return cleaned_count
            y, x = ny, nx

def sol():
    n, m = map(int, input().split())
    y, x, d = map(int, input().split())
    room = [list(map(int, input().split())) for _ in range(n)]
    print(get_cleaned_num(n,m,x,y,d,room))

if __name__ == "__main__":
    sol()