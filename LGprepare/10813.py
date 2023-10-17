N, M = map(int, input().split())
bucket = list(map(int, range(N + 1)))
# print(bucket)
for _ in range(M):
    i, j = map(int, input().split())
    bucket[i], bucket[j] = bucket[j], bucket[i]
print(" ".join(map(str, bucket[1:])))