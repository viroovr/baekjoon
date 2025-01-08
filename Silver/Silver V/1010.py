from math import comb, factorial
from time import time

def logger(func):
    def wrapper(*args):
        start = time()
        func(*args)
        end = time()
        print(f"{end - start:.9f} elapsed. {func.__name__}")
        return func
    return wrapper


def factoSolv(M, N):
    return int(factorial(M) / (factorial(M - N) * factorial(N)))

def combSol(M, N):
    return comb(M, N)

@logger
def test_factoSolv():
    N, M = 13, 29
    u = factoSolv(M, N)
    expected = 67863915
    assert u == expected

@logger
def test_combSolv():
    N, M = 13, 29
    u = combSol(M, N)
    expected = 67863915
    assert u == expected

def sol():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        print(combSol(M, N))

def test_func():
    test_combSolv()
    test_factoSolv()

if __name__ == "__main__":
    test = False
    if test:
        test_func()
    else:
        sol()
        