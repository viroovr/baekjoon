N = int(input())
P = sorted(list(map(int, input().split())))
p_sum = 0
for i, x in enumerate(P):
    p_sum += (N - i) * x
print(p_sum)
