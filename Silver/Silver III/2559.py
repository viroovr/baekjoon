import sys
input = sys.stdin.readline

# O(N)/ O(N)
def sol():
    N, K = map(int, input().split())
    temps = list(map(int, input().split()))
    
    prefix = [temps[0]]
    # prefix sum 리스트 생성
    for i in range(1, len(temps)):
        prefix.append(prefix[i - 1] + temps[i])

    maxValue = prefix[K - 1]

    for i in range(K, N):
        maxValue = max(maxValue, prefix[i] - prefix[i - K])
    
    print(maxValue)

sol()


