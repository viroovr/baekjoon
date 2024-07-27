N, M, K = map(int, input().split())
numbers = list(map(int, input().split()))

numbers = sorted(numbers)

first = numbers[N - 1]
second = numbers[N - 2]
# 5 9 3
# 2 4 5 4 6
# 6 6 6 5 6 6 6 5 6 
answer = 0
count = (M // (K + 1)) * K + M % (K + 1)
answer += first * count
answer += second * (M - count)
print(answer)
# i = M
# while i // (K + 1) != 0:
#     i = i - (K + 1)
#     answer += numbers[0] * K + numbers[1]
# print(i, answer)
# if i % (K + 1) != 0:
#     answer += numbers[0] * (i % (K + 1)) + numbers[1] * (i - i % (K + 1))
# print(answer)