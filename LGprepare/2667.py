from sys import stdin
input = stdin.readline
N = int(input())
village = []
for i in range(N):
    k = input()
    village.append([int(k[j]) for j in range(N)])

direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]
check = [[False] * N for _ in range(N)]


def bfs(y, x):
    if check[y][x]:
        return -1
    count = 1
    q = [(y, x)]
    check[y][x] = True
    while q:
        b, a = q.pop()
        for dx, dy in direction:
            c = (b + dy, a + dx)
            if 0 <= c[0] < N and 0 <= c[1] < N and village[c[0]][c[1]] and not check[c[0]][c[1]]:
                check[c[0]][c[1]] = True
                count += 1
                q.append(c)
    return count


ans = []
for i in range(N):
    for j in range(N):
        if village[i][j]:
            t = bfs(i, j)
            if t != -1:
                ans.append(t)

print(len(ans))
ans.sort()
for i in ans:
    print(i)
