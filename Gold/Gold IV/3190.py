import time
from collections import deque

def test_logger(func):
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()
        print(f"Test {func.__name__} finished in { end - start:.5f}sec")
        return result
    return wrapper

def isIn(y, x):
    global N
    return 0 <= y < N and 0 <= x < N

@test_logger
def test_isIn():
    global N
    N = 6
    assert not isIn(6, 6)
    assert isIn(1, 1)
    assert isIn(2, 3)
    assert isIn(0, 0)
    assert not isIn(0, 7)
    assert not isIn(-1, 7)

def move(currentDirection):
    global currentPosition, lastPostion, directionStack, board
    dx, dy = directions[currentDirection]
    nextX, nextY = currentPosition[0] + dx, currentPosition[1] + dy
    if not isIn(nextY, nextX):
        return True
    if board[nextY][nextX] == 1:
        return True

    currentPosition = (nextX, nextY)
    directionStack.append(currentDirection)
    if board[nextY][nextX] == 0:
        dx, dy = directions[directionStack.popleft()]
        board[lastPostion[1]][lastPostion[0]] = 0
        lastPostion = (lastPostion[0] + dx, lastPostion[1] + dy)
    board[nextY][nextX] = 1

    return False

@test_logger
def test_move1():
    global currentPosition, lastPostion, board, N, directionStack
    N = 6
    currentPosition = (0, 0)
    lastPostion = (0, 0)
    directionStack = deque([0])
    board = [
        [1 , 0, 0, 0 ,0, 0],
        [0 , 0, 0, 0 ,2, 0],
        [0 , 0, 0, 2 ,0, 0],
        [0 , 0, 0, 0 ,0, 0],
        [0 , 0, 2, 0 ,0, 0],
        [0 , 0, 0, 0 ,0, 0],
    ]

    assert not move(0)
    assert currentPosition == (1, 0)
    assert lastPostion == (1, 0)
    assert directionStack == deque([0])
    assert board == [
        [0 , 1, 0, 0 ,0, 0],
        [0 , 0, 0, 0 ,2, 0],
        [0 , 0, 0, 2,0, 0],
        [0 , 0, 0, 0 ,0, 0],
        [0 , 0, 2, 0 ,0, 0],
        [0 , 0, 0, 0 ,0, 0],
    ]
    
@test_logger
def test_move2():
    global currentPosition, lastPostion, board, N, directionStack
    N = 6
    currentPosition = (3, 0)
    lastPostion = (3, 0)
    directionStack = deque([1])
    board = [
        [0 , 0, 0, 1 ,0, 0],
        [0 , 0, 0, 0 ,2, 0],
        [0 , 0, 0, 2 ,0, 0],
        [0 , 0, 0, 0 ,0, 0],
        [0 , 0, 2, 0 ,0, 0],
        [0 , 0, 0, 0 ,0, 0],
    ]

    assert not move(1)
    assert currentPosition == (3, 1)
    assert directionStack == deque([1])
    assert lastPostion == (3, 1)
    assert board == [
        [0 , 0, 0, 0 ,0, 0],
        [0 , 0, 0, 1 ,2, 0],
        [0 , 0, 0, 2,0, 0],
        [0 , 0, 0, 0 ,0, 0],
        [0 , 0, 2, 0 ,0, 0],
        [0 , 0, 0, 0 ,0, 0],
    ]

@test_logger
def test_move3():
    global currentPosition, lastPostion, board, N, directionStack
    N = 6
    currentPosition = (3, 1)
    lastPostion = (3, 1)
    directionStack = deque([1])
    board = [
        [0 , 0, 0, 0 ,0, 0],
        [0 , 0, 0, 1 ,2, 0],
        [0 , 0, 0, 2 ,0, 0],
        [0 , 0, 0, 0 ,0, 0],
        [0 , 0, 2, 0 ,0, 0],
        [0 , 0, 0, 0 ,0, 0],
    ]

    assert not move(1)
    assert currentPosition == (3, 2)
    assert directionStack == deque([1, 1])
    assert lastPostion == (3, 1)
    assert board == [
        [0 , 0, 0, 0 ,0, 0],
        [0 , 0, 0, 1 ,2, 0],
        [0 , 0, 0, 1, 0, 0],
        [0 , 0, 0, 0 ,0, 0],
        [0 , 0, 2, 0 ,0, 0],
        [0 , 0, 0, 0 ,0, 0],
    ]

@test_logger
def test_move4():
    global currentPosition, lastPostion, board, N, directionStack
    N = 6
    currentPosition = (3, 2)
    lastPostion = (3, 1)
    directionStack = deque([1, 1])
    board = [
        [0 , 0, 0, 0 ,0, 0],
        [0 , 0, 0, 1 ,2, 0],
        [0 , 0, 0, 1 ,0, 0],
        [0 , 0, 0, 0 ,0, 0],
        [0 , 0, 2, 0 ,0, 0],
        [0 , 0, 0, 0 ,0, 0],
    ]

    assert not move(1)
    assert currentPosition == (3, 3)
    assert lastPostion == (3, 2)
    assert directionStack == deque([1, 1])
    assert board == [
        [0 , 0, 0, 0 ,0, 0],
        [0 , 0, 0, 0 ,2, 0],
        [0 , 0, 0, 1, 0, 0],
        [0 , 0, 0, 1 ,0, 0],
        [0 , 0, 2, 0 ,0, 0],
        [0 , 0, 0, 0 ,0, 0],
    ]

@test_logger
def test_move5():
    global currentPosition, lastPostion, board, N, directionStack
    N = 6
    currentPosition = (3, 5)
    lastPostion = (3, 4)
    directionStack = deque([1, 1])
    board = [
        [0 , 0, 0, 0 ,0, 0],
        [0 , 0, 0, 0 ,2, 0],
        [0 , 0, 0, 0 ,0, 0],
        [0 , 0, 0, 0 ,0, 0],
        [0 , 0, 2, 1 ,0, 0],
        [0 , 0, 0, 1 ,0, 0],
    ]

    assert move(1)
    assert currentPosition == (3, 5)
    assert lastPostion == (3, 4)
    assert directionStack == deque([1 , 1])
    assert board == [
        [0 , 0, 0, 0 ,0, 0],
        [0 , 0, 0, 0 ,2, 0],
        [0 , 0, 0, 0, 0, 0],
        [0 , 0, 0, 0 ,0, 0],
        [0 , 0, 2, 1 ,0, 0],
        [0 , 0, 0, 1 ,0, 0],
    ]

@test_logger
def test_move6():
    global currentPosition, lastPostion, board, N, directionStack
    N = 6
    currentPosition = (2, 3)
    lastPostion = (3, 4)
    directionStack = deque([1, 2, 3, 3, 3])
    board = [
        [0 , 0, 0, 0 ,0, 0],
        [0 , 0, 0, 0 ,2, 0],
        [0 , 0, 0, 0 ,0, 0],
        [0 , 0, 1, 0 ,0, 0],
        [0 , 0, 1, 1 ,0, 0],
        [0 , 0, 1, 1 ,0, 0],
    ]

    assert not move(3)
    assert currentPosition == (2, 2)
    assert lastPostion == (3, 5)
    assert directionStack == deque([2, 3, 3, 3, 3])
    assert board == [
        [0 , 0, 0, 0 ,0, 0],
        [0 , 0, 0, 0 ,2, 0],
        [0 , 0, 1, 0, 0, 0],
        [0 , 0, 1, 0 ,0, 0],
        [0 , 0, 1, 0 ,0, 0],
        [0 , 0, 1, 1 ,0, 0],
    ]

@test_logger
def test_move7():
    global currentPosition, lastPostion, board, N, directionStack
    N = 6
    currentPosition = (2, 4)
    lastPostion = (3, 4)
    directionStack = deque([1, 2, 3, 3])
    board = [
        [0 , 0, 0, 0 ,0, 0],
        [0 , 0, 0, 0 ,2, 0],
        [0 , 0, 0, 0 ,0, 0],
        [0 , 0, 0, 0 ,0, 0],
        [0 , 0, 1, 1 ,0, 0],
        [0 , 0, 1, 1 ,0, 0],
    ]

    assert move(0)

@test_logger
def test_move8():
    global currentPosition, lastPostion, board, N, directionStack
    N = 6
    currentPosition = (0, 0)
    lastPostion = (0, 0)
    directionStack = deque([0])
    board = [
        [1 , 2, 2, 2 ,2, 2],
        [0 , 0, 0, 0 ,0, 0],
        [0 , 0, 0, 0 ,0, 0],
        [0 , 0, 0, 0 ,0, 0],
        [0 , 0, 0, 0 ,0, 0],
        [0 , 0, 0, 0 ,0, 0],
    ]

    assert not move(0)
    assert currentPosition == (1, 0)
    assert lastPostion == (0, 0)
    assert directionStack == deque([0, 0])
    assert board == [
        [1 , 1, 2, 2 ,2, 2],
        [0 , 0, 0, 0 ,0, 0],
        [0 , 0, 0, 0 ,0, 0],
        [0 , 0, 0, 0 ,0, 0],
        [0 , 0, 0, 0 ,0, 0],
        [0 , 0, 0, 0 ,0, 0],
    ]

# @test_logger
# def test_move9():
#     global currentPosition, lastPostion, board, N, directionStack
#     N = 6
#     currentPosition = (5, 0)
#     lastPostion = (0, 0)
#     directionStack = deque([0, 1, 1, 1, 1, 1])
#     board = [
#         [0 , 0, 0, 0 ,0, 1],
#         [0 , 0, 0, 0 ,0, 1],
#         [0 , 0, 0, 0 ,0, 1],
#         [0 , 0, 0, 0 ,0, 1],
#         [0 , 0, 0, 0 ,0, 1],
#         [0 , 0, 0, 0 ,0, 1],
#     ]

#     assert not move(1)
#     assert currentPosition == (5, 1)
#     assert lastPostion == (1, 0)
#     assert directionStack == deque([0, 0, 0, 0, 0, 1])
#     assert board == [
#         [0 , 1, 1, 1 ,1, 1],
#         [0 , 0, 0, 0 ,0, 1],
#         [0 , 0, 0, 0 ,0, 0],
#         [0 , 0, 0, 0 ,0, 0],
#         [0 , 0, 0, 0 ,0, 0],
#         [0 , 0, 0, 0 ,0, 0],
#     ]

def setDirection(time):
    global currentDirection, dirInfo
    if dirInfo and time == int(dirInfo[0][0]):
            _, direction = dirInfo.popleft()
            if direction == "D":
                currentDirection = (currentDirection + 1) % 4
            else:
                currentDirection = (currentDirection - 1) % 4

@test_logger
def test_setDirection1():
    global currentDirection, dirInfo
    dirInfo = deque(
        [("3", "D"), ("15", "L"), ("17", "D")]
    )
    currentDirection = 0
    setDirection(1)

    assert currentDirection == 0

@test_logger
def test_setDirection2():
    global currentDirection, dirInfo
    dirInfo = deque(
        [("3", "D"), ("15", "L"), ("17", "D")]
    )
    currentDirection = 0
    setDirection(3)

    assert currentDirection == 1

@test_logger
def test_setDirection3():
    global currentDirection, dirInfo
    dirInfo = deque(
        [("15", "L"), ("17", "D")]
    )
    currentDirection = 1
    setDirection(15)

    assert currentDirection == 0

@test_logger
def test_setDirection4():
    global currentDirection, dirInfo
    dirInfo = deque(
        [("17", "L")]
    )
    currentDirection = 0
    setDirection(17)

    assert currentDirection == 3

@test_logger
def test_setDirection5():
    global currentDirection, dirInfo
    dirInfo = deque(
        []
    )
    currentDirection = 3
    setDirection(18)

    assert currentDirection == 3

@test_logger
def test_setDirection6():
    global currentDirection, dirInfo
    dirInfo = deque(
        [("17", "D")]
    )
    currentDirection = 3
    setDirection(17)

    assert currentDirection == 0

@test_logger
def test_setDirection7():
    global currentDirection, dirInfo
    dirInfo = deque(
        [("17", "L")]
    )
    currentDirection = 3
    setDirection(17)

    assert currentDirection == 2

def make_board():
    global board, N, apples
    board = [[0] * N for _ in range(N)]
    for apple in apples:
        board[apple[0] - 1][apple[1] - 1] = 2
    board[0][0] = 1

@test_logger
def test_board():
    global N, apples
    apples = [
        [3, 4], [2, 5], [5, 3]
    ]
    make_board()
    N = 6
    assert board == [
        [1 , 0, 0, 0 ,0, 0],
        [0 , 0, 0, 0 ,2, 0],
        [0 , 0, 0, 2,0, 0],
        [0 , 0, 0, 0 ,0, 0],
        [0 , 0, 2, 0 ,0, 0],
        [0 , 0, 0, 0 ,0, 0],
    ]

def game():
    global N,dirInfo, currentPosition, currentDirection,lastPostion, directionStack
    make_board()
    time = 0
    while True:
        time += 1
        if move(currentDirection):
            return time
        setDirection(time)

def take_input():
    global N, apples, dirInfo, currentPosition, currentDirection,lastPostion, directionStack
    lastPostion = (0, 0)
    currentPosition = (0, 0)
    currentDirection = 0
    directionStack = deque([])
    N = int(input())
    K = int(input())
    apples = [list(map(int, input().split())) for _ in range(K)]
    L = int(input())
    dirInfo = deque(tuple(input().split()) for _ in range(L))

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)] #동, 남, 서, 북

def solution():
    take_input()
    print(game())

def test_function():
    # test_input()
    test_setDirection1()
    test_setDirection2()
    test_setDirection3()
    test_setDirection4()
    test_setDirection5()
    test_setDirection6()
    test_setDirection7()
    test_isIn()
    test_board()
    test_move1()
    test_move2()
    test_move3()
    test_move4()
    test_move5()
    test_move6()
    test_move7()
    test_move8()


@test_logger
def test_input():
    take_input()
    assert N == 6
    assert K == 3
    assert apples == [
        [3, 4], [2, 5], [5, 3]
    ]
    assert L == 3
    assert dirInfo == deque(
        [("3", "D"), ("15", "L"), ("17", "D")]
    )

if __name__ == "__main__":
    TEST = 0

    if TEST == 1:
        test_function()
    else:
        solution()