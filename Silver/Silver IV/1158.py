def josephus(N, K):
    table = [i for i in range(1, N + 1)]
    cur = 0
    ret = []
    while table:
        cur = (cur - 1 + K) % len(table)
        ret.append(table[cur])
        table.pop(cur)
    return ret

def sol():
    N, K = map(int, input().split())
    u = map(str, josephus(N, K))
    print(f"<{', '.join(u)}>")

def test_josephuse1():
    N, K = 7, 3
    expected = [3, 6, 2, 7, 5, 1, 4]
    actual = josephus(N, K)
    assert expected == actual, f"expected {expected}, but actual {actual}"

def test_func():
    test_josephuse1()

if __name__ == "__main__":
    test = 0
    if test == 1:
        test_func()
    else:
        sol()