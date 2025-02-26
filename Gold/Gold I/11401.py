"""
페르마의 소정리 활용
    페르마의 소정리에 따르면,
    어떤 소수 p에 대해 a가 p의 배수가 아니라면, 
    a^(p - 1) ≡ 1 (mod p)
    이 성질을 변형하면,
    a^-1 ≡ a^(p - 2) (mod p)
    즉, 모듈로 역원을 구할 때 거듭제곱을 이용해 역원을 계산할 수 있다는 의미이다.

1. pow사용
194400	656
192272	660 1
"""

from math import log2
DIVISOR = 1_000_000_007

def get_fact(k_dp, indexes, length):
    K_fact = 1
    for i in range(length):
        k_dp.append((k_dp[-1] ** 2) % DIVISOR)
    for i in indexes:
        K_fact = (K_fact * k_dp[i]) % DIVISOR
    return K_fact

def get_bionomial(N, K):
    dp = [1, 1]
    for i in range(2, N + 1):
        dp.append((dp[-1] * i) % DIVISOR)
    N_fact = dp[N]
    
    length = int(log2(DIVISOR))
    indexes = []
    for i, v in enumerate(reversed(bin(DIVISOR - 2)[2:])):
        if v == "1":
            indexes.append(i)

    K_fact = get_fact([dp[K]], indexes, length)
    N_K_fact = get_fact([dp[N-K]], indexes, length)

    return ((N_fact * K_fact) % DIVISOR * N_K_fact) % DIVISOR

def sol():
    N, K = map(int, input().split())
    print(get_bionomial(N, K))

sol()