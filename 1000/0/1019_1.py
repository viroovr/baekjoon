N = int(input())


def bruteforce():
    ans = [0] * 10
    for i in range(1, N + 1):
        for j in str(i):
            ans[int(j)] += 1
    return ans


def solution(n, ans):
    global sub
    p = 10 ** (len(str(n)) - 1)
    k = n % p
    print("p, k", p, k)
    for i in range(0, n // p):
        ans[i] += p
    ans[n // p] += k
    sub += p
    return ans


print("Select mode : b(bruteforth) a(ans)")
# if (input() == 'b'):
#     print(bruteforce())
# else:
ans = [0] * 10
print("ans", solution(N, ans))
