from sys import stdin
input = stdin.readline


def main():
    N = int(input())
    stairs = [int(input()) for _ in range(N)]
    dp_table = [[0] * 2 for _ in range(N + 1)]
    dp_table[1][0] = stairs[0]
    if N > 1:
        dp_table[2][0], dp_table[2][1] = stairs[0] + stairs[1], stairs[1]
    for i in range(3, N + 1):
        n = stairs[i - 1]
        dp_table[i][0] = dp_table[i - 1][1] + n
        dp_table[i][1] = max(dp_table[i - 2]) + n
    print(max(dp_table[-1]))
        

main()
