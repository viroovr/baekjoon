sum_table = [-1] * 11

sum_table[1] = 1
sum_table[2] = 2
sum_table[3] = 2 + 1 + 1


def count(n):
    if sum_table[n] != -1:
        return sum_table[n]
    sum_table[n] = count(n - 1) + count(n - 2) + count(n - 3)
    return sum_table[n]


T = int(input())
for _ in range(T):
    print(count(int(input())))
