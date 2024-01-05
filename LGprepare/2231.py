N = int(input())

nums = [i for i in str(N)]
# print(nums)
st = [0] * len(nums)
# print(st)


def generator(n, st, length):
    if length < 1 or n < 0:
        return
    print(n, st, length)
    generator(n, st[1:], length - 1)
    for i in range(1, 10):
        st[0] = i
        generator(n - i * (10 ** (length - 1) + 1), st, length)
    return st


generator(N, st, len(nums))
