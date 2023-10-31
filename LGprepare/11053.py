def main():
    N = int(input())
    sequence = list(map(int, input().split()))
    dp_table = [1] * N
    for i in range(len(sequence) - 2, -1, -1):
        max_num = -1
        for j in range(i + 1, len(sequence)):
            if sequence[j] > sequence[i] and dp_table[j] > max_num:
                max_num = dp_table[j]
                dp_table[i] = 1 + max_num
    print(max(dp_table))


main()
