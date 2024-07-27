N, M = map(int, input().split())
numbers = [list(map(int, input().split())) for _ in range(N)]
min_number = [min(nums) for nums in numbers]
print(max(min_number))