from time import time
from math import ceil
def test_logger(func):
    def wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        end = time()
        print(f"TEST: [{func.__name__}] finished in {end - start:.5f}sec")
        return func
    return wrapper


def getMinSup():
    global N, A, B, C
    minSup = 0
    for a in A:
        minSup += 1
        if a - B > 0:
            minSup += ceil((a - B) / C)

    return minSup

@test_logger
def test_getMinSup1():
    global N, A, B, C
    N = 3
    A = [3, 4, 5]
    B, C = 2, 2
    
    minSup = getMinSup()

    assert minSup == 7

@test_logger
def test_getMinSup2():
    global N, A, B, C
    N = 5
    A = [1000000, 1000000, 1000000,1000000,1000000]
    B, C =5, 7
    
    minSup = getMinSup()

    assert minSup == 714290

@test_logger
def test_getMinSup3():
    global N, A, B, C
    N = 5
    A = [10, 9, 10, 9, 10]
    B, C =7, 2
    
    minSup = getMinSup()

    assert minSup == 13

def take_input():
    global N, A, B, C
    N = int(input())
    A = list(map(int, input().split()))
    B, C = map(int, input().split())

@test_logger
def test_input():
    take_input()
    assert N == 3
    assert A == [3, 4, 5]
    assert B == 2 and C == 2

def solution():
    take_input()
    print(getMinSup())

def test_function():
    # test_input()
    test_getMinSup1()
    test_getMinSup2()
    test_getMinSup3()
    pass

if __name__ == "__main__":
    TEST = 0

    if TEST == 1:
        test_function()
    else:
        solution()
    