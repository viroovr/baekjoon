N = int(input())
M = int(input())
adj = [[0] * N for _ in range(N)]
for _ in range(M):
    i, j = map(lambda x: x - 1, map(int, input().split()))
    adj[i][j] = 1
    adj[j][i] = 1


def bfs(v):
    check = [False] * N
    check[0] = True
    q = [v]
    while q:
        j = q.pop(0)
        for i in range(N):
            if adj[j][i] == 1 and not check[i]:
                check[i] = True
                q.append(i)
    return check


t = bfs(0).count(True) 
print(t - 1 if t > 0 else 0)
