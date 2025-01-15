from time import time
from sys import stdin
input = stdin.readline

def logger(func):
    def wrapper(*args):
        s = time()
        func(*args)
        e = time()
        print(f"{func.__name__} is ended in {e - s:.5f}sec")
        return func
    return wrapper

def minS(n, a, b):
    return sum(x * y for x, y in zip(sorted(a), sorted(b, reverse=True)))

@logger
def test_minS(n, a, b, expected):
    actual = minS(n, a, b)
    assert actual == expected, f"expected {expected} but {actual}"

def sol():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(minS(N, A, B))

def parse_list(input_value):
    return list(map(int, input_value.split()))

def test_function():
    test_minS(5, [1, 1, 1, 6, 0], [2, 7, 8, 3, 1], 18)
    test_minS(3, [1, 1, 3], [10, 30, 20], 80)
    test_minS(9, parse_list("5 15 100 31 39 0 0 3 26"), parse_list("11 12 13 2 3 4 5 9 1"), 528)

if __name__ == "__main__":
    test = 0
    if test == 1:
        test_function()
    else:
        sol()