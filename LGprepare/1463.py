N = int(input())
nums = [0] * (10 ** 6 + 1)
nums[2] = 1
nums[3] = 1
for i in range(4, N + 1):
    # l = []
    # if i % 3 == 0:
    #     l.append(nums[i // 3])
    # elif (i - 1) % 3 == 0:
    #     l.append(nums[(i - 1) // 3] + 1)
    # else:
    #     l.append(nums[(i - 1) // 3] + 2)
    # if i % 2 == 0:
    #     l.append(nums[i // 2])
    # elif (i - 1) % 2 == 0:
    #     l.append(nums[(i - 1) // 2] + 1)
    nums[i] = 1 + min(nums[i // 3] + i % 3, nums[i // 2] + i % 2)
    # print(nums[:(i + 1)])
print(nums[N])