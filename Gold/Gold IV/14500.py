"""
🔹 1차 개선된 점
1. frozenset 사용
    불변 집합을 사용해 메모리 사용 최적화.
2. isIn 함수 제거
    if not (0 <= nx < m and 0 <= ny < n):를 바로 사용해 함수 호출을 줄임.
3. max()를 한 줄로 처리
    중첩 반복문을 한 줄로 정리하여 가독성 향상.
4. stdin.readline 사용
    내부적으로 표준 입력을 한 번에 여러 줄 버퍼에 저장한 후 처리하기 때문에 속도가 빠름.
    input()은 한 줄 입력이 들어올 때마다 표준 입력에서 직접 데이터를 가져오기 때문에 속도가 느림.
    input()은 Python 인터프리터 내부에서 추가적인 파싱 과정이 포함됨.
    input()은 입력을 받을 때 자동으로 개행 문자(\n)를 제거하는 등 추가적인 처리가 포함됨.

    메모리(KB)  시간(ms)
0차 38456	    2704
1차 38336       2140
"""
import sys
input = sys.stdin.readline

tetrominos = frozenset([
        ((1, 0), (2, 0), (3, 0)),

        ((0, 1), (0, 2), (0, 3)),
        ((1, 0), (0, 1), (1, 1)),

        ((0, 1), (0, 2), (1, 2)),
        ((1, 0), (1, -1), (1, -2)),
        ((1, 0), (2, 0), (2, -1)),
        ((0, 1), (1, 1), (2, 1)),
        ((1, 0), (1, 1), (1, 2)),
        ((0, 1), (0, 2), (1, 0)),
        ((1, 0), (2, 0), (0, 1)),
        ((1, 0), (2, 0), (2, 1)),

        ((0, 1), (1, 1), (1, 2)),
        ((0, 1), (1, 0), (1, -1)),
        ((1, 0), (1, -1), (2, -1)),
        ((1, 0), (1, 1), (2, 1)),

        ((1, 0), (1, 1), (2, 0)),
        ((1, 0), (1, -1), (1, 1)),
        ((1, 0), (1, -1), (2, 0)),
        ((0, 1), (0, 2), (1, 1))
    ])

def getSumByTetromino(x, y, m, n, tetromino):
    total = board[y][x]
    for dx, dy in tetromino:
        curx, cury = x + dx, y + dy
        if not (0 <= curx < m and 0 <= cury < n):
            return -1
        total += board[cury][curx]
    return total

def sol():
    global board
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    print(max(getSumByTetromino(x, y, m, n, tetromino)
            for y in range(n) for x in range(m) for tetromino in tetrominos))

if __name__ == "__main__":
    t = 0
    if t == 1:
        pass
    else:
        sol()