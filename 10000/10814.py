N = int(input())
ans = []
for _ in range(N):
    age, name = input().split()
    ans.append((int(age), name))
ans.sort(key=lambda x: x[0])
for i in range(N):
    print(ans[i][0], ans[i][1])
