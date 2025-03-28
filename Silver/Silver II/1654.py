import sys
input = sys.stdin.readline

def count(number):
    return sum(cable // number for cable in cables)

def get_max_cable():
    left, right = 1, (1 << 31) - 1
    res = 0
    while left <= right:
        mid = (left + right) // 2
        if count(mid) >= N:
            res = mid
            left = mid + 1
        else:
            right = mid - 1
    print(res)

def sol():
    global K, N, cables
    K, N = map(int, input().split())
    cables = [int(input().rstrip()) for _ in range(K)]
    get_max_cable()

sol()