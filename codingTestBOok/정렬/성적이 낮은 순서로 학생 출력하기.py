N = int(input())
array = []
for _ in range(N):
    array.append(tuple(input().split()))
array.sort(key=lambda x: int(x[1]))
for i in range(N):
    print(array[i][0], end=" ")
