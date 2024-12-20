from time import time

def test_logger(func):
    def wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        end = time()
        print(f"TEST {func.__name__} finished in {end-start:.5f}")
        return func
    return wrapper

def decreasingNum(N):
    nums = list(range(1, 10))
    index = 0
    while index < len(nums):
        u = nums[index]
        k = int(str(u)[-1])
        for i in range(k):
            nums.append(int(str(u) + str(i)))
        index += 1
        if len(nums) >= N:
            return nums[N - 1]
    return -1
    
@test_logger
def test_decreasingNum(N, expected_result):
    result = decreasingNum(N)
    assert result == expected_result, f"Expected {expected_result}, got {result}"
    print(f"Test passed for N = {N}, result = {result}")

def solution():
    N = int(input())
    if N < 10:
        print(N)
    else:
        print(decreasingNum(N))


def test_func():
    # [1,2,3,4,5,6,7,8,9,10
    # ,20,21,30,31,32,40,41,42,43,50
    # ,51,52,53,54,60,61,62,63,64,65
    # ,70,71,72,73,74,75,76,80,81,82
    # ,83,84,85,86,87,90,91,92,93,94
    # ,95,96,97,98,210,310,320,321,410,420]
    test_decreasingNum(1, 1)
    test_decreasingNum(10, 10)
    test_decreasingNum(18, 42)
    test_decreasingNum(50, 94)
    test_decreasingNum(60, 420)
    test_decreasingNum(500000, -1)

if __name__ == "__main__":
    TEST = 1
    if TEST == 1:
        test_func()
    else:
        solution()
