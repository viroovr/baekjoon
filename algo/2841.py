from sys import stdin
input = stdin.readline
N, P = map(int, input().split())
cache = [[] for _ in range(P+1)]

count = 0
for _ in range(N):
    i, j = map(int, input().split())
    while cache[i] and cache[i][-1] > j:
        count += 1
        cache[i].pop()
    if cache[i] and cache[i][-1] == j:
        continue
    else:
        cache[i].append(j)
        count += 1
# print(count)
print(count)
# print(cache)
    