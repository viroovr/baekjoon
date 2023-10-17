N, M = map(int, input().split())
bucket = list(map(int, range(N + 1)))
order = [tuple(map(int, input().split())) for _ in range(M)]
for i in order:
    t = bucket[i[0]: i[1] + 1]
    t.reverse()
    bucket = bucket[:i[0]] + t + bucket[i[1] + 1:]
print(" ".join(map(str, bucket[1:])))