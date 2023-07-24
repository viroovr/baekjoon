N, L = map(int, input().split())
coord = [False] * 1001
for i in map(int, input().split()):
    coord[i] = True

ans = 0
x = 0
while x < 1001:
    if coord[x]:
        ans += 1
        x += L
    else:
        x += 1

print(ans)