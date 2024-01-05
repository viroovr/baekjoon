N, M = map(int, input().split())
trees = list(map(int, input().split()))
lo, hi = 0, max(trees)
ans = 0
while lo <= hi:
    mid = (lo + hi) // 2
    count = sum(i - mid for i in trees if i > mid)
    if count < M:
        hi = mid - 1
    else:
        lo = mid + 1
        ans = mid
print(ans)