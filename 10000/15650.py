N, M = map(int, input().split())


def func(prefix: str, n, m):
    # print("n", n, "m", m)
    if m <= 0:
        return prefix
    for i in range(n, N + 1):
        ap = prefix + " " + str(i)
        k = func(ap, i + 1, m - 1)
        if k:
            print(k.strip())


func("", 1, M)
