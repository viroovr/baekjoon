K, N = map(int, input().split())
lans = [int(input()) for _ in range(K)]
lo = 1
hi = max(lans)
ans = 0
while lo <= hi:
    mid = (lo + hi) // 2
    if mid == 0:
        break
    count = sum(i // mid for i in lans)
    if count < N:
        hi = mid - 1
    else:
        lo = mid + 1
        ans = mid
    # print(lo, hi, mid, count, ans)
print(ans)
