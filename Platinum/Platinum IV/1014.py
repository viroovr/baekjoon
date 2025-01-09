# 1시간 정도 고민 후 gpt에게서 masking과 dp힌트를 얻음
from time import time

def logger(func):
    def wrapper(*args):
        start = time()
        func(*args)
        end = time()
        print(f"{func.__name__} ended in {end-start:.5f}sec")
        return func
    return wrapper

def isPossibleLine(y, mask, classroom):
    for i in range(len(mask)):
        if mask[i] == '1' and classroom[y][i] == 'x':
            return False
        if i != 0 and mask[i] == '1' and mask[i - 1] == '1':
            return False
    return True

def isPossibledp(prevMask, currentMask):
    size = len(currentMask)
    for i in range(size):
        if currentMask[i] == '0':
            continue
        if i == 0:
            if prevMask[i + 1] == '1':
                return False
        elif i == size - 1:
            if prevMask[i - 1] == '1':
                return False
        else:
            if prevMask[i - 1] == '1' or prevMask[i + 1] == '1':
                return False
    return True

def getReversedBinNum(m, num):
    t = bin(num)[2:].zfill(m)
    return "".join(reversed(t))

def maxStudent(n, m, classroom):
    prev = [-1] * (2 ** m)
    current = [-1] * (2 ** m)

    for i in range(2 ** m):
        mask = getReversedBinNum(m, i)
        if isPossibleLine(0, mask, classroom):
            prev[i] = mask.count('1')

    for i in range(1, n):
        for j in range(2 ** m):
            if prev[j] == -1:
                continue
            prevMask = getReversedBinNum(m, j)
            for k in range(2 ** m):
                mask = getReversedBinNum(m, k)
                if not isPossibleLine(i, mask, classroom):
                    continue
                if not isPossibledp(prevMask, mask):
                    continue
                cnt = mask.count('1')
                current[k] = max(prev[j] + cnt, current[k])

        prev, current = current, [-1] * (2 ** m)
    
    return max(prev)

@logger
def test_maxStudent01():
    n, m = 2, 3
    print(getReversedBinNum(2, 10))
    classroom = [
        ['.', '.', '.'],
        ['.', '.', '.']
    ]
    actual = maxStudent(n, m, classroom)
    expected = 4
    assert expected == actual, f"{n,m,classroom} expected {expected} but {actual}"

@logger
def test_maxStudent02():
    n, m = 2, 3
    classroom = [
        ['x', '.', 'x'],
        ['x', 'x', 'x']
    ]
    actual = maxStudent(n, m, classroom)
    expected = 1
    assert expected == actual, f"{n,m,classroom} expected {expected} but {actual}"

@logger
def test_maxStudent03():
    n, m = 10, 10
    classroom =[
        ['.', '.', '.', '.', 'x', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', 'x', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['x', '.', '.', '.', 'x', '.', 'x', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'x'],
        ['.', '.', '.', 'x', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', 'x', '.'],
        ['.', 'x', '.', '.', '.', 'x', '.', '.', '.', '.']]

    actual = maxStudent(n, m, classroom)
    expected = 46
    assert expected == actual, f"{n,m,classroom} expected {expected} but {actual}"

@logger
def test_maxStudent04():
    n, m = 10, 10
    classroom =[
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]

    actual = maxStudent(n, m, classroom)
    expected = 50
    assert expected == actual, f"{n,m,classroom} expected {expected} but {actual}"

def sol():
    C = int(input())
    for _ in range(C):
        N, M = map(int, input().split())
        classroom = [list(input()) for _ in range(N)]
        print(maxStudent(N, M, classroom))
            
def test_func():
    test_maxStudent01()
    test_maxStudent02()
    test_maxStudent03()
    test_maxStudent04()

if __name__ == "__main__":
    test = 0
    if test == 1:
        test_func()
    else:
        sol()