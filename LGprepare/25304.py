X = int(input())
N = int(input())
price_list = [tuple(map(int, input().split())) for _ in range(N)]
# print(X, N, price_list)
count = 0
for i in price_list:
    count += i[0] * i[1]
if count == X:
    print("Yes")
else:
    print("No")