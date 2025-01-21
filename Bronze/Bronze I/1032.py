from time import time

def logger(func):
    def wrapper(*args):
        s = time()
        func(*args)
        e = time()
        print(f"{func.__name__} is ended in {e - s:.5f}")
        return func
    return wrapper

def find_pattern(names):
    ret = []
    file_len = len(names[0])
    for i in range(file_len):
        ret.append(names[0][i])
        for j in range(1, len(names)):
            if names[j][i] != names[0][i]:
                ret.pop()
                ret.append("?")
                break
    return "".join(ret)

@logger
def test_find_pattern(names, expected):
    a = find_pattern(names)
    assert a == expected, f"{expected} expected but {a}"

def sol():
    n = int(input())
    names = [input() for _ in range(n)]
    print(find_pattern(names))

def test_fun():
    test_find_pattern(["config.sys", "config.inf", "configures"], "config????")
    test_find_pattern(["contest.txt", "context.txt"], "conte?t.txt")
    test_find_pattern(["c.user.mike.programs", "c.user.nike.programs", "c.user.rice.programs"], "c.user.?i?e.programs")
    test_find_pattern(["a", "a", "b", "b"], "?")
    test_find_pattern(["onlyonefile"], "onlyonefile")
    test_find_pattern(
        [
            "werowieorweiuoqeviruasdhfjwofpbkrkfkvmqwiqoekf",
            "werowieorweiuoqeviruasdhfjwofpbkrkfkvmqwiqoekf",
            "werowieorweiuoqeviruasdhfjwofpbkrkfkvmqwiqoekf",
            "werowieorweiuorweoiruasdhfjwofpbkrkfkvmxjdiqoekf",
            "werowieorweiuorweoiruasdhfjwofpbkrkfkcazdiqoekf",
            "werowieorweiuorweoiruasdhfjwofpbkrkfkcazdiqoekf",
            "werynieorweiuorweoiruasdhfjwofpbkrkfkvmxjdiqoekf",
            "werynieorweiuorweoiruasdhfjwofpbkrkfkvmxjdiqoekf",
            "werynieorweiuorweoiruasdhfjwofpbkrkfkvmxjdiqoekf",
            "werowieorweiuorweoiruasdhfjwofpbkrkfkvmxjdiqoekf",
            "werowieorweiuorweoiruasdhfjwofpbkrkfkvmxjdiqoekf",
            "werowieorweiuorweoiruasdhfjwofpbkrkfkvmxjdiqoekf",
            "werowieorweiuorweoiruasdhfjwofpbkrkfkvmxjdiqoekf",
            "werowieorweiuorweoiruasdhfjwofpbkrkfkvmxjdiqoekf",
            "werowieorweiuorweoiruasdhfjwofpbkrkfkvmxjdiqoekf",
            "werowieorweiuorweoirchfjwofpbkrkfkvmxjdiqoekf",
            "werowieorweiuorweoirchfjwofpbkrkfkqjdiqoekf",
            "werowieorweiuorweoirchfjwofpbkrkfkqjdiqoekf",
            "werowieorweiuorweoiruasdhfjwofpbkrkfkqjdiqoekf",
            "werowieorweiuorweoiruasdhfjwofpbkrkfkvmxjdiqoekf",
            "werowieorweiuorweoiruasdhfjwofpbkrkfkvmxjdiqoekf",
            "werowieorweiuorweoiqwerasdhfjwofpbkrkfigxjdiqoekf",
            "werowieorweiuorweoiqwerasdhfjwofpbkrkfigxjdiqoekf",
            "werowieorweiuorweoiqwerasdhfjwofpbkrkfigxjdiqoekf",
            "werowieorweiuorweoiruasdhfjwofpbkrkfkvmxjdiqoekf",
            "werowieorweiuoreeoiruasdhfjeofpbkrkfkvmxjdiqoekf",
            "eeroeieoreeiuoreeoiruasdhfjwofpbkrkfkvmxjdiqoekf",
            "werowieorweiuorweoiruqwdfpbkrkfkvmxjdiqoekf",
            "werowieorweiuorweoiruqwdfpbkrkfkvmxjdiqoekf",
            "werowieorweiuorweoiruqwdfpbkrkfkvmxjdiqoekf",
            "werowieorweiuorweoiruasdhfjwofpbkrkfkvmxjdiqoekf",
            "werowieorweiuorweoiruasdhfjwofpbkrkfkvjdiqoekf",
            "werowieorweiuorweoiruasdhfjwofpbkrkfkvjdiqoekf",
            "werowieorweiqwweoiruasdhfjwofpbkrkfkvjdiqoekf",
            "werowieorweiqwweoiruasdhfjwofpbkrkfkvmxjdiqoekf",
            "werowieorweiqwweoiruasdhfjwoyubkrkfkvmxjdiqoekf",
            "werowieorweiuorweoiruasdhfjwoyubkrkfkvmxjdiqoekf",
            "werowieorweiuorweoiruasdhfjwoyubkrkfkvqjdiqoekf",
            "werowieorweiuorweoiruasdhfjwofpbkrkfkvqjdiqoekf",
            "werowieorweiuorweoiruasdhfjwofpbkrkfkvqjdiqoekf",
            "werowieorweiuorweoiruasdhfjwofpbkrkfkvqjdiqoekf",
            "werowieorweiuorweoiruasdhfjwofpbkrkfkvmxjdiqoekf",
            "werowieorweiuorweoawcvsdhfjwofpbkrkfkvmxjdiqoekf",
            "werowieorweiuorweoawcvsdhfjwofpekrkfkvmxjdiqoekf",
            "werowieorweiuorweoawcvsdhfjwofpekrkfkvmxjdiqoekf",
            "werowieorweiuorweoiruasdhfjwofpekrkfkvmxjdiqoekf",
            ], "?er??ieor?ei??????????????????????????????????")

if __name__ == "__main__":
    test = 0
    if test == 1:
        test_fun()
    else:
        sol()