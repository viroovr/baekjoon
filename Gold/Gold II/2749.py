"""
1. 리스트 제거: dp 리스트를 제거하고, 두 개의 변수 (a, b) 만 사용하여 메모리를 절약했습니다.
2. CYCLE 하드 코딩
92284	340
32412	320 1
32412	164 1,2
"""
DIVISOR = 1_000_000
CYCLE = 1_500_000
def fib(n):
    a, b = 0, 1
    n %= CYCLE
    for _ in range(n):
        k = (a + b) % DIVISOR
        a, b = b, k

    return a

def sol():
    n = int(input())
    print(fib(n))

sol()