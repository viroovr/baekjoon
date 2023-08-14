import sys
sys.setrecursionlimit(10000)
N, K = map(int, input().split())
L = [[1] * i for i in range(1, N + 2)]
"""
nck = n-1ck-1 + n-1ck
[1], [1,1], [1,1,1], [1,1,1,1], , [1,1,1,1,1], [1,1,1,1,1,1] 
1   1   1   1   1
1   2   3   4   5
1   3   6   10  15
1   4   10  20  25
1   5   15  35  60
0,0 1,1 2,2 3,3 4,4 5,5
1,0 2,1 3,2 4,3 5,4
2,0 3,1 4,2 5,3
3,0 4,1 5,2 
4.0 5,1
5,0
"""
# print(L)


def nck(n, k):
    if k == 0 or k == n or n < 2:
        return 1
    if L[n-1][k] == 1:
        L[n-1][k] = nck(n-1, k)
    if L[n-1][k-1] == 1:
        L[n-1][k-1] = nck(n-1, k-1)

    return L[n-1][k] + L[n-1][k-1]


t = nck(N, K)
print(t % 10007)
# print(L)
