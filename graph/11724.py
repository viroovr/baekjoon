# 1<= N <= 1000, 0 <= M <= N(N-1)/2
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
link = [set() for _ in range(N+1)]

for _ in range(M):
    i, k = map(int, input().split())
    link[i].add(k)
    link[k].add(i)


# print(link)
check = [False] * (N+1)
# print(check)


def bfs(now):
    q = deque()
    q.append(now)
    while q:
        now = q.popleft()
        for i in link[now]:
            if not check[i]:
                check[i] = True
                q.append(i)
        # print(q)
    # print(i)


conn = 0
for i in range(1, N+1):
    if not check[i]:
        check[i] = True
        bfs(i)
        conn += 1
# print(check)
print(conn)
