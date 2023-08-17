# 1 3
# 1 4
# 2 3
# 3 4
# 4 5
# 1 - 3 -2 
# 1 - 3
# 1 - 4
# 1 - 4 - 5
# 2 + 1 + 1 + 2
# 1 - 3
# | / |
# 4   2
# |
# 5
from collections import deque
from sys import stdin

input = stdin.readline

N, M = map(int, input().split())
adj = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    adj[a][b] = adj[b][a] = 1


def bfs(n):
    global N
    count = 0
    check = [False] * (N + 1)
    q = deque()
    q.append((n, 0))
    check[n] = True
    while q:
        now, d = q.popleft()
        # print(u)
        for i, v in enumerate(adj[now]):
            if v == 1 and not check[i]:
                check[i] = True
                q.append((i, d + 1))
                count += d + 1
    return count


k = [bfs(n) for n in range(1, N + 1)]
# print(k)
print(k.index(min(k)) + 1)
