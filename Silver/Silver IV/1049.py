from math import ceil

def getMinPrice(n, m, brands):
    minSix, minOne = 1234, 1234
    for brand in brands:
        minSix = min(brand[0], minSix)
        minOne = min(brand[1], minOne)
    return min(minOne * n, n // 6 * minSix + n % 6 * minOne, ceil(n / 6) * minSix)

def test_getMinPrice(n, m, brands, expected):
    a = getMinPrice(n, m, brands)
    assert a == expected, f"{expected} expected but {a}"

def sol():
    n, m =  map(int, input().split())
    brands = [list(map(int, input().split())) for _ in range(m)]
    print(getMinPrice(n, m, brands))

def test_fun():
    test_getMinPrice(4, 2, [[12, 3], [15, 4]], 12)
    test_getMinPrice(10, 3, [[20, 8], [40, 7], [60, 4]], 36)
    test_getMinPrice(15, 1, [[100, 40]], 300)
    test_getMinPrice(17, 1, [[12, 3]], 36)
    test_getMinPrice(7, 2, [[10, 3], [12, 2]], 12)

if __name__ == "__main__":
    tes = 1
    if tes == 1:
        test_fun()
    else:
        sol()