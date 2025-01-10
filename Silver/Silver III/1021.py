from collections import deque
from time import time
def logger(func):
    def wrapper(*args):
        s = time()
        func(*args)
        e = time()
        print(f"test({args}) is ended in {(e - s) * 10 ** 3:.6f}msec")
        return func
    return wrapper

def minOperation(n, m, positions):
    q = deque(range(1, n + 1))
    count = 0
    for i in positions:
        p = q.index(i)
        direction = 1
        if p <= len(q) // 2:
            direction = -1
        while q[0] != i:
            if direction == -1:
                q.append(q.popleft())
            else:
                q.appendleft(q.pop())
            count += 1
        q.popleft()
    return count

@logger
def test_minOperation(N, M ,positions, expected):
    actual = minOperation(N, M, positions)
    assert expected == actual, f"{N, M , positions} {expected} expected but {actual}"

def sol():
    N, M = map(int, input().split())
    positions = list(map(int, input().split()))
    print(minOperation(N, M, positions))

def test_func():
    test_minOperation(10, 3, [1,2,3], 0)
    # 1 2 3 4 5 6 7 8 9 10
    test_minOperation(10, 3, [2,9,5], 8)
    # 1 2 3 4 5 6 7 8 9 10
    # 2 3 4 5 6 7 8 9 10 1  2
    # 3 4 5 6 7 8 9 10 1    
    # 1 3 4 5 6 7 8 9 10    3
    # 10 1 3 4 5 6 7 8 9    3
    # 9 10 1 3 4 5 6 7 8    3
    # 10 1 3 4 5 6 7 8
    # 8 10 1 3 4 5 6 7      2
    # 7 8 10 1 3 4 5 6      2
    # 6 7 8 10 1 3 4 5      2
    # 5 6 7 8 10 1 3 4      2
    # 6 7 8 10 1 3 4      
    test_minOperation(32, 6, [27,16,30,11,6,23], 59)
    test_minOperation(10, 10, [1,6,3,2,7,9,8,4,10,5], 14)

if __name__ == "__main__":
    test = 0
    if test == 1:
        test_func()
    else:
        sol()