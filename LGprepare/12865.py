from sys import stdin
input = stdin.readline


def main():
    N, K = map(int, input().split())
    valuables = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x: (x[0], -x[1]))
    dp_table = [[0] * (K + 1) for _ in range(len(valuables) + 1)]
    for iy in range(1, len(dp_table)):
        for ix in range(1, len(dp_table[0])):
            item_weight, item_value = valuables[iy - 1]
            if item_weight > ix:
                dp_table[iy][ix] = dp_table[iy - 1][ix]
            else:
                dp_table[iy][ix] = max(dp_table[iy - 1][ix], item_value + dp_table[iy - 1][ix - item_weight])
    print(dp_table[-1][-1])


main()
