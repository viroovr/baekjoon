from collections import deque

adj = [[0] * 13 for _ in range(13)]
adj[0][1] = adj[0][2] = 1
adj[1][3] = adj[1][4] = 1
adj[2][5] = adj[2][6] = 1
adj[4][9] = 1
adj[3][7] = adj[3][8] = 1
adj[5][10] = adj[5][11] = adj[5][12] = 1


def bfs():
    dq = deque()
    dq.append(0)
    while dq:
        now = dq.popleft()
        print(now)
        for nxt in range(13):
            if adj[now][nxt]:
                dq.append(nxt)


bfs()
