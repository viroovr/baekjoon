
def solution():
    N = int(input())
    for i in range(1, N + 1):
        decompose_sum = i + sum(int(x) for x in str(i))
        if decompose_sum == N:
            print(i)
            break
    else:
        print(0)


solution()
