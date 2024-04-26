from collections import deque
N, K = map(int, input().split())
# N -> K


def solution():
    q = deque()
    q.append((N, 0))
    check = [False for _ in range(100001)]

    while q:
        cur, time = q.popleft()
        if cur == K:
            return time
        for i in [-1, cur, 1]:
            t = cur + i
            if t < 0 or t > 100000 or check[t]:
                continue
            check[t] = True
            if i == cur:
                q.append((t, time))
            else:
                q.append((t, time + 1))


print(solution())
