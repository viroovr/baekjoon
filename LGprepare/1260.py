from collections import deque

N, M, V = map(int, input().split())
adjmatrix = [[0] * N for _ in range(N)]
for _ in range(M):
    i, j = map(lambda x: x - 1, map(int, input().split()))
    adjmatrix[i][j] = 1
    adjmatrix[j][i] = 1
# print(adjmatrix)


def dfs(v):
    check[v - 1] = True
    visit.append(v - 1)
    for i in range(N):
        if adjmatrix[v - 1][i] == 1 and not check[i]:
            dfs(i + 1)
    return visit


def bfs(v):
    check = [False] * N
    q = deque()
    visit = [v - 1]
    check[v - 1] = True
    q.append(v - 1)
    while q:
        c = q.popleft()
        for i in range(N):
            if adjmatrix[c][i] == 1 and not check[i]:
                visit.append(i)
                check[i] = True
                q.append(i)
    return visit


check = [False] * N
visit = []
print(" ".join(map(str, map(lambda x: x + 1, dfs(V)))))
print(" ".join(map(str, map(lambda x: x + 1, bfs(V)))))
