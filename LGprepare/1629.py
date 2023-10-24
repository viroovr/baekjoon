MAX_SIZE = 31


def solution():
    A, B, C = map(int, input().split())
    remainder_list = [-1] * MAX_SIZE
    remainder_list[0] = A % C
    for i in range(1, MAX_SIZE):
        remainder_list[i] = remainder_list[i - 1] ** 2 % C
    ans = 1
    temp = B
    index2base = []
    while temp > 1:
        index2base.append(temp % 2)
        temp //= 2
    index2base.append(temp)
    for i, num in enumerate(index2base):
        if num == 1:
            ans *= remainder_list[i]
    return ans % C


print(solution())
