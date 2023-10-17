N, M = map(int, input().split())
method = [tuple(map(int, input().split())) for _ in range(M)]
bucket = [0] * (N + 1)
for i in method:
    for j in range(i[0], i[1] + 1):
        bucket[j] = i[2]
print(" ".join(map(str, bucket[1:])))
