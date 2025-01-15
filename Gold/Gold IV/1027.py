from time import time

def logger(func):
    def wrapper(*args):
        s = time()
        func(*args)
        e = time()
        print(f"{func.__name__} is ended in {e - s:.5f}")
        return func
    return wrapper

def isSeeing(x1, y1, x2, y2, x3, y3):
    height = (y2 - y1) / (x2 - x1)
    return float(y3 - y2) > (height * (x3 - x2))

def maxSeeing(n, buildings):
    ret = 0
    for cur in range(n):
        def cnt(direction, cur):
            index = cur + direction
            if not (0 <= index < n):
                return 0
            temp_max = 1
            index_max = index
            index_max_max = buildings[index_max]
            while 0 <= index < n:
                if isSeeing(cur, buildings[cur], index_max, index_max_max, index, buildings[index]):
                    temp_max += 1
                    index_max = index
                    index_max_max = buildings[index]
                index += direction
            return temp_max
        k = cnt(-1, cur) + cnt(1, cur)
        ret = max(ret, k)
                
    return ret

@logger
def test_maxSeeing(n, buildings, expected):
    a = maxSeeing(n, buildings)
    assert expected == a, f"{expected} expected, but {a}" 

def sol():
    N = int(input())
    buildings = list(map(int, input().split()))
    print(maxSeeing(N, buildings))

def parse_list(input_val):
    return list(map(int, input_val.split()))

def test_fun():
    test_maxSeeing(4, parse_list("5 5 5 5"), 2)
    test_maxSeeing(5, parse_list("1 2 7 3 2"), 4)
    test_maxSeeing(1, parse_list("10"), 0)
    test_maxSeeing(10, parse_list("1000000000 999999999 999999998 999999997 999999996 1 2 3 4 5"), 6)
    test_maxSeeing(15, parse_list("1 5 3 2 6 3 2 6 4 2 5 7 3 1 5"), 7)

if __name__ == "__main__":
    test = 0
    if test == 1:
        test_fun()
    else:
        sol()