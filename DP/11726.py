N = int(input())
met = [0] * 1001

met[1] = 1
met[2] = 2

# bottom up
# Tabulation, iteration
# for i in range(1, N+1):
#     if not met[i]:
#         met[i] = met[i-1] + met[i-2]
#         met[i] %= 10007
#     # print(i, met[i])
# print(met[N])


# Top down
# Memoization, recursion
def f(n):
    if not met[n]:
        met[n] = f(n - 1) + f(n - 2)
        met[n] %= 10007
    return met[n]


print(f(N))
