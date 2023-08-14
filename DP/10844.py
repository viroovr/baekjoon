"""
    1   0   1
        2   1
            3
    2   1   0
            2
        3   2
            4
    3   2   1
            3
        4   3
            5
    4   3   2
            4
        5   4
            6
    5   4   3
            5
        6   5
            7
    6   5   4
            6
        7   6
            8
    7   6   5
            7
        8   7
            9
    8   7   6
            8
        9   8
    9   8   7
            9
"""

N = int(input())
MOD = 1_000_000_000
st = [[0] * 10 for _ in range(101)]

for i in range(1, 10):
    st[1][i] = 1

for i in range(1, N):
    st[i + 1][1] = st[i][0]
    st[i + 1][8] = st[i][9]
    for j in range(1, 9):
        u = st[i][j]
        st[i + 1][j - 1] += u
        st[i + 1][j + 1] += u

# print(st[N])
print(sum(st[N]) % MOD)
