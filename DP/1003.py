# 0
# 1,0
# 1
# 0,1

# 2
# 1   0
# 1,1

# 3
# 2   1
# 1   0
# 1,2

# 4
# 3   2
# 2   1   1   0
# 1   0
# 2,3

# 5
# 4   3
# 3   2   2   1
# 2   1   1   0   1   0
# 1   0
# 3, 5
fibmat = [(-1, -1)] * 41
fibmat[0] = (1, 0)
fibmat[1] = (0, 1)

for i in range(2, 41):
    fibmat[i] = [sum(x) for x in zip(fibmat[i - 1], fibmat[i - 2])]
    # fibmat[i] = (fibmat[i - 1][0] + fibmat[i - 2][0], fibmat[i - 1][1] + fibmat[i - 2][1])

T = int(input())
for _ in range(T):
    N = int(input())
    print(*fibmat[N])
