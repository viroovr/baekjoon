"""
뭔가 다양한 방법을 생각하며 풀어본 문제.
처음에 bruteforth 방법으로 풀었을 때 O(N!)이라서 실패

N! 을 줄이기 위해 TSP 문제를 떠올렸고, N의 범위도 15라 2 ^ 15 커버가 될것같았다.
하지만, 이전에 나온 숫자의 자릿수 까지 계산된 나머지를 어떻게 계산해야 할까 고민을 계속 했다.
이전에 나온 수들의 자리 정보도 포함시키면 결국 N! 의 메모리가 포함되기 때문에 이는 어불성설이었다.

결국, gpt의 도움을 받았다. dp[mask][reminder] 로 두어서. 각 인덱스에는 해당 루트의 remainder 개수를 집어넣는다.
나도 이건 생각을 했었는데, 그렇다면 이전 정보들은 어떻게 해줄까?

현재 mask에서 1인 위치들의 인덱스 값의 합으로 나타낸다. 이전 1의 위치들의 순서와 상관없이 결국
해당 길이들의 합이 이전 정보이므로, 이를 이용해 집어넣을 수의 길이를 구할 수 있게 된다.
사실 이게 dp의 원리인데. 부분 문제가 이후 문제의 최적해가 되는. 이 원리를 소홀히 생각했다.
그리고, 순서라는 정보에 매몰된 것 같다.

112088	3388
"""
from math import gcd

def get_K_divided_up(N, numbers, K):
    M = len(numbers)
    dp = [[0] * K for _ in range(1 << M)]

    dp[0][0] = 1
    mods = [i % K for i in numbers]
    degree = list(map(lambda x: len(str(x)), numbers))

    for mask in range(1 << M):
        used_length = (10 ** sum(degree[i] for i in range(N) if mask & (1 << i))) % K
        for i in range(N):
            if mask & (1 << i):
                continue
            
            new_mask = mask | (1 << i)
            for k in range(K):
                if dp[mask][k]:
                    new_rem = (mods[i] * used_length + k) % K
                    dp[new_mask][new_rem] += dp[mask][k]

    p = dp[-1][0]
    q = sum(dp[-1])

    if p == q:
        return "1/1"
    elif p == 0:
        return "0/1"
    else:
        g = gcd(p, q)
        return f"{p // g}/{q // g}"

def sol():
    N = int(input())
    numbers = [int(input()) for _ in range(N)]
    K = int(input())
    print(get_K_divided_up(N, numbers, K))
    
sol()


    
