T = int(input())
remain = [[] for _ in range(10)]
for i in range(10):
    k = i
    for j in range(2, 100):
        d = k % 10
        if d in remain[i]:
            break
        remain[i].append(d)
        k = i ** j
# print(remain)
for _ in range(T):
    a, b = map(int, input().split())
    i = a % 10
    j = b % len(remain[i]) - 1
    d = remain[i][j]
    print(d if d else 10)
