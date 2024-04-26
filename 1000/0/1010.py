from math import factorial

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(int(factorial(M) / (factorial(M - N) * factorial(N))))
