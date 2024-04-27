N, K = map(int, input().split())
circle = list(map(str, range(1, N + 1)))
ret = []
index = K - 1

for _ in range(N):
    ret.append(circle.pop(index))
    index += K - 1
    if circle and index >= len(circle):
        index %= len(circle)

print(f'<{", ".join(ret)}>')
