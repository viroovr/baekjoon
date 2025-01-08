def logger(func):
    def wrapper(*args):
        func(*args)
        print(f"{func.__name__} is ended")
        return func
    return wrapper

def lastNum(a, b):
    p = a % 10
    memo = [p]
    for i in range(1, 10):
        u = (p * memo[i - 1]) % 10
        if u == p: break
        memo.append(u)
    k = b % len(memo)
    t = memo[k - 1]
    return t if t != 0 else 10

@logger
def test_lastNum001():
    a, b = 1, 6
    u = lastNum(a, b)
    expected = 1
    assert u == expected, f"{a, b} expected {expected} but {u}"

@logger
def test_lastNum002():
    a, b = 3, 7
    u = lastNum(a, b)
    expected = 7
    assert u == expected, f"{a, b} expected {expected} but {u}"


@logger
def test_lastNum021():
    a, b = 6, 2
    u = lastNum(a, b)
    expected = 6
    assert u == expected, f"{a, b} expected {expected} but {u}"

@logger
def test_lastNum003():
    a, b = 7, 100
    u = lastNum(a, b)
    expected = 1
    assert u == expected, f"{a, b} expected {expected} but {u}"

@logger
def test_lastNum004():
    a, b = 9, 635
    u = lastNum(a, b)
    expected = 9
    assert u == expected, f"{a, b} expected {expected} but {u}"

@logger
def test_lastNum005():
    a, b = 10, 2
    u = lastNum(a, b)
    expected = 10
    assert u == expected, f"{a, b} expected {expected} but {u}"

def solution():
    T = int(input())
    for _ in range(T):
        a, b = map(int, input().split())
        print(lastNum(a, b))

def test_func():
    test_lastNum001()
    test_lastNum002()
    test_lastNum021()
    test_lastNum003()
    test_lastNum004()
    test_lastNum005()

if __name__ == "__main__":
    test = 0
    if test == 1:
        test_func()
    else:
        solution()
