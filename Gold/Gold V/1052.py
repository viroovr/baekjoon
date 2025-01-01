from time import time
def test_logger(func):
    def wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        end = time()
        print(f"{func.__name__} is finished in {end - start:.5f}")
        return func
    return wrapper

def pour(nums):
    s = 0
    for i in range(len(nums) - 1):
        nums[i + 1] = nums[i] // 2 + nums[i + 1]
        nums[i] = nums[i] % 2
        s += nums[i]
    s += nums[-1] 
    return s

def findIndex(nums:list):
    for i in range(len(nums)):
        if nums[i] != 0:
            return i

def move(N, K, nums):
    count = 0
    s = pour(nums)
    while s > K:
        t = findIndex(nums)
        nums[t] += 1
        count += 2 ** t
        s = pour(nums)
    return count
    
    
@test_logger
def test_move1():
    N, K = 3, 1
    nums = [0] * 30
    nums[0] = N
    # 1, 1, 1
    # 2 1
    # 2 1 1
    # 2 2
    # 4
    assert move(N, K, nums) == 1

@test_logger
def test_move2():
    N, K = 4, 1
    nums = [0] * 30
    nums[0] = N
    # 1, 1, 1, 1
    assert move(N,K, nums) == -1

@test_logger
def test_move3():
    N, K = 13, 2
    nums = [0] * 30
    nums[0] = N
    # 1 1 1 1 1 1 1 1 1 1 1 1 1
    # 2 2 2 2 2 2 1
    # 4 4 4 1
    # 8 4 1
    # 8 4 1 1 1 1
    # 8 4 2 2
    # 8 4 4
    # 8 8
    u = move(N,K, nums)
    assert  u == 3, f"3 expected but {u}"

@test_logger
def test_move4():
    N, K = 1000000, 5
    nums = [0] * 30
    nums[0] = N
    # 1 1 1 1 1 1 1 1 1 1 1 1 1
    # 2 2 2 2 2 2 1
    # 4 4 4 1
    # 8 4 1
    # 8 4 1 1 1 1
    # 8 4 2 2
    # 8 4 4
    # 8 8
    u = move(N,K, nums)
    assert  u == 15808, f"15808 expected but {u}"

def solution():
    N, K = map(int, input().split())
    nums = [0] * 30
    nums[0] = N
    print(move(N, K, nums))

def test_func():
    test_move1()
    test_move2()
    test_move3()
    test_move4()

if __name__ == "__main__":
    TEST = 0
    if TEST == 1:
        test_func()
    else:
        solution()