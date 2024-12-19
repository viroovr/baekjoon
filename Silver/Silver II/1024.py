from time import time
def test_logger(func):
    def wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        end = time()
        print(f"TEST [{func.__name__}] complete in {end - start:.5f}")
        return func
    return wrapper

def makeList(i, N):
    ret = []
    k = N // i
    if i % 2 == 0:
        for j in range(i // 2):
            if k - j < 0:
                return -1
            ret.append(k - j)
            ret.append(k + j + 1)
    else:
        ret.append(k)
        for j in range(1, (i - 1) // 2 + 1):
            if k - j < 0:
                return -1
            ret.append(k - j)
            ret.append(k + j)
    return sorted(ret)

@test_logger
def test_makeList1():
    ret = makeList(4, 10)
    assert ret == [1,2,3,4]

@test_logger
def test_makeList2():
    ret = makeList(3, 18)
    assert ret == [5,6,7]

@test_logger
def test_makeList3():
    ret = makeList(4, 18)
    assert ret == [3, 4, 5,6]

@test_logger
def test_makeList4():
    ret = makeList(10, 45)
    assert ret == [0,1,2,3,4,5,6,7,8,9]

@test_logger
def test_makeList5():
    ret = makeList(5, 1000000000)
    assert ret == [199999998,199999999,200000000,200000001,200000002]

def getSumLIntegerList():
    global N, L
    for i in range(L, 101):
        if i % 2 == 0:
            if N % i == 0:
                continue
            elif N % i == i / 2:
                return makeList(i, N)
        else:
            if N % i == 0:
                return makeList(i, N)
            else:
                continue
    return -1

@test_logger
def test_getSumIntegerList1():
    global N, L
    N = 18
    L = 2
    ret = getSumLIntegerList()
    assert ret != -1
    assert ret != [9, 10]
    assert ret != [8, 9]
    assert ret == [5, 6, 7]
    #짝수로 나눌때, 나머지=0 안됨. 홀수로 나눌때, 나머지=0 정답

@test_logger
def test_getSumIntegerList2():
    global N, L
    N = 10
    L = 2
    ret = getSumLIntegerList()
    assert ret != -1
    assert ret != [5, 6]
    assert ret != [4, 5]
    assert ret != [2,3,4]
    assert ret == [1,2,3,4]
    #짝수로 나눌때, 나머지=0 안됨. 홀수로 나눌때, 나머지!=0 안됨
    #짝수로 나눌떄, x.5형식이면 됨.

@test_logger
def test_getSumIntegerList3():
    global N, L
    N = 11
    L = 2
    ret = getSumLIntegerList()
    assert ret != -1
    assert ret == [5, 6]
    # 2로나눌 떄, 5.5 됨

@test_logger
def test_getSumIntegerList4():
    global N, L
    N = 11
    L = 3
    ret = getSumLIntegerList()
    assert ret != [2, 3, 4]
    assert ret != [1,2,3,4]
    assert ret != [1,2,3,4]
    assert ret != [1,2,3,4,5]
    assert ret == -1

def take_input():
    global N, L
    N, L = map(int, input().split())

def solution():
    take_input()
    ret = getSumLIntegerList()
    if ret == -1:
        print(ret)
    else:
        print(*ret)

def test_function():
    test_getSumIntegerList1()
    test_getSumIntegerList2()
    test_getSumIntegerList3()
    test_getSumIntegerList4()
    test_makeList1()
    test_makeList2()
    test_makeList3()
    test_makeList4()
    test_makeList5()

if __name__ == "__main__":
    TEST = 0
    if TEST == 1:
        test_function()
    else:
        solution()
