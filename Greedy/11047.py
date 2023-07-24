import sys
input = sys.stdin.readline
N, K = map(int, input().split())
coin = sorted([int(input()) for _ in range(N)], reverse=True)
num = 0
for i in coin:
    if K == 0:
        break
    num += K // i
    K %= i
print(num)

