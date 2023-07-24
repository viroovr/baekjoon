import sys
input = sys.stdin.readline
N, L = map(int, input().split())
water = sorted(list(map(int, input().split())))
# print(water)
num = 0
i = 0
while i < N:
    j = i + 1
    while j < N:
        # print(f"i : {i}, j : {j}")
        k = 1
        if water[j] - water[i] < L:
            k += 1
            j += 1
        
        elif water[j] - water[i] == L:
            if k == L:
                num += 1
                if j == N-1:
                    num += 1
                break
        if k > 1:
            num += 1
            break
    i = j
print(num)
        