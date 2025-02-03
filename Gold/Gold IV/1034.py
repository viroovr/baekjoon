from time import time
from collections import Counter

def logger(func):
    def wrapper(*args):
        s = time()
        result = func(*args)
        e = time()
        print(f"{args} func is ended in {e - s:.5f}")
        return result
    return wrapper

def getMaxRowLightedRamp(n, m, table, k):
    patterns = Counter(table)
    
    ret = 0
    for key, v in patterns.items():
        zero_cnt = key.count('0')
        if k >= zero_cnt and k % 2 == zero_cnt % 2:
           ret = max(ret, v)
    return ret

@logger
def test_getMaxRowLightedRamp(n,m,table,k,expected):
    a = getMaxRowLightedRamp(n,m,table,k)
    assert a == expected, f"{expected} expected but {a}"

def sol():
    n, m = map(int, input().split())
    table = [input().strip() for _ in range(n)]
    k = int(input())
    print(getMaxRowLightedRamp(n, m, table, k))

def test_fun():
    test_getMaxRowLightedRamp(3, 2, ['01', '10', '10'], 1, 2)
    test_getMaxRowLightedRamp(1, 6, ['101010'], 2, 0)
    test_getMaxRowLightedRamp(2, 2, ['00', '11'], 999, 0)
    test_getMaxRowLightedRamp(5, 1, ['0', '1', '0', '1' , '0'], 1000, 2)
    test_getMaxRowLightedRamp(14, 3, ['001','101','001','000','111','001','101','111','110','000','111','010','110','001'], 6, 4)
    test_getMaxRowLightedRamp(5, 2, ['01','10','01','01','10'], 1, 3)

if __name__ == "__main__":
    t = 1
    if t == 1:
        test_fun()
    else:
        sol()