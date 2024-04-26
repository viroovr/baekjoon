import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 * 1000000)

T = int(input())


def mark(a, b, v):
    global check, stack
    m, n = a
    x, y = b
    check[n][m] = check[y][x] = 1
    if v == 1:
        stack += 1
    else:
        stack -= 1


# def bt(x, y):
#     global ans, stack, enemy
#     # print(f"x, y, stack. ans {x}, {y}, {stack}, {ans}")
#     if x >= N:
#         bt(0, y + 1)
#         return
#     if y >= 2:
#         ans = min(ans, stack)
#         return
#     if check[y][x]:
#         bt(x + 1, y)
#         return
#     k = y + 1 if y == 0 else y - 1
#     for m, n in [(x - 1, y), (x, k), (x + 1, y)]:
#         if enemy[y][x] + enemy[n][m] <= W and not check[n][m]:
#             mark((m, n), (x, y), 1)
#             bt(x + 1, y)
#             mark((m, n), (x, y), 0)
#     else:
#         mark((x, y), (x, y), 1)
#         bt(x + 1, y)

def bt(x, y):
    global ans, stack, enemy
    # print(f"x, y, stack. ans {x}, {y}, {stack}, {ans}")
    if x >= N:
        # bt(0, y + 1)
        return
    if y >= 2:
        return
    if check[y][x]:
        return
    k = y + 1 if y == 0 else y - 1
    q = 0 if x + 1 == N else x + 1
    found = False
    for m, n in [(x - 1, y), (x, k), (q, y)]:
        if not check[n][m] and enemy[y][x] + enemy[n][m] <= W:
            found = True
            mark((m, n), (x, y), 1)
            bt(x + 1, y)
            mark((m, n), (x, y), 0)
    if not found:
        mark((x, y), (x, y), 1)


def isPossible():
    return min(min(check[i]) for i in range(2)) == 1


for _ in range(T):
    N, W = map(int, input().split())
    stack = 0
    check = [[0] * N for _ in range(2)]
    ans = 2 * N + 1
    enemy = [list(map(int, input().split())), list(map(int, input().split()))]
    # enemy = [[1]*10000, [1]*10000]
    # print(N, W, check, enemy)
    for i in range(2):
        for j in range(N):
            print(i, j)
            bt(j, i)
            print(check, stack)
    ans = min(ans, stack)

    print(ans)
    # print(f"ans : {ans}")
    # print(stack)
