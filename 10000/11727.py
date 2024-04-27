# 2×n 타일링 2
# 11727
DIV = 10_007
n = int(input())
tiling = [-1] * 1001
tiling[0] = 0
tiling[1] = 1
tiling[2] = 3


def count(n):
    if tiling[n] != -1:
        return tiling[n]
    tiling[n] = (count(n - 1) + 2 * count(n - 2)) % DIV
    return tiling[n]


print(count(n))
