NUM = 100_000


def main():
    N, K = map(int, input().split())
    dp_table = [-1] * (NUM + 1)

    dp_table[N] = 0
    # temp = N
    # for i in range(1, NUM):
    #     temp *= 2
    #     if temp >= NUM:
    #         break
    #     dp_table[temp] = i

    for i in range(1, NUM):
        left = N - i
        if left < 0:
            break
        dp_table[left] = i

    for i in range(1, NUM + 1):
        right = N + i
        if right > NUM:
            break
        compare = []
        if right - 1 >= 0 and dp_table[right - 1] != -1:
            compare.append(dp_table[right - 1] + 1)
        if right + 1 <= NUM and dp_table[right + 1] != -1:
            compare.append(dp_table[right + 1] + 1)
        if right % 2 == 0 and dp_table[right // 2] != -1:
            compare.append(dp_table[right // 2] + 1)
        if right % 2 != 0:
            if (right + 1) // 2 >= 0 and dp_table[(right + 1) // 2] != -1:
                compare.append(dp_table[(right + 1)// 2] + 2)
            if (right - 1) // 2 >= 0 and dp_table[(right - 1) // 2] != -1:
                compare.append(dp_table[(right - 1)// 2] + 2)
        dp_table[right] = min(compare)
    # print(dp_table)
    print(dp_table[K])
    

main()
