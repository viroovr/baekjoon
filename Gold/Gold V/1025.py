from time import time
from math import sqrt

def logger(func):
    def wrapper(*args):
        s = time()
        func(*args)
        e = time()
        print(f"{func.__name__} is ended in {e - s:.5f}")
        return func
    return wrapper

def isPerfectSquare(n):
    return float.is_integer(sqrt(n))

@logger
def test_isPerfectSquare(n, expected):
    assert isPerfectSquare(n) == expected

def makeString(row, col, table):
    w = set()
    t = ""
    if len(row) == 1:
        y = row[0]
        for x in col:
            w.add((y, x))
            t += table[y][x]
    elif len(col) == 1:
        x = col[0]
        for y in row:
            w.add((y, x))
            t += table[y][x]
    elif len(row) == len(col):
        for y, x in zip(row, col):
            w.add((y, x))
            t += table[y][x]
    return t

def maximumPerfectSquareNum(n, m, table):
    # 1의 간격이 일정한 이진수 크기 n, m
    max_num = -1
    rows = set()
    cols = set()
    rows.add((0,))
    cols.add((0,))
    for i in range(n):
        for j in range(1, n + 1):
            for k in range(1, n):
                rows.add(tuple(range(i, j, k)))
                rows.add(tuple(reversed(range(i, j, k))))
    for i in range(m):
        for j in range(1, m + 1):
            for k in range(1, m):
                cols.add(tuple(range(i, j, k)))
                cols.add(tuple(reversed(range(i, j, k))))
    for row in rows:
        for col in cols:
            if row or col:
                p = makeString(row, col, table)
                if p != -1 and p != "":
                    if isPerfectSquare(int(p)):
                        max_num = max(max_num, int(p))
    return max_num
    # 이진수의 앞, 뒤로 오가며 1인 부분의 인덱스를 table에서 읽어오기
    
        

def parse(input_val):
    put = input_val.split("\n")
    N, M = map(int, put[0].split())
    table = [list(t) for t in put[1:]]
    return N, M, table

@logger
def test_maximumPerfectSquareNum(input_val, expected):
    N, M, table = parse(input_val)
    actual = maximumPerfectSquareNum(N, M, table)
    assert expected == actual, f"{expected} expected, but {actual}"

def sol():
    N, M = map(int, input().split())
    table = [list(list(input())) for _ in range(N)]
    print(maximumPerfectSquareNum(N, M, table))

def test_fun():
    print([(x, y) for x, y in zip((0, ), (5,4,3,2,1))])
    print([(x, y) for x, y in zip((5,4,3,2,1), (0, ))])
    test_isPerfectSquare(64, True)
    test_isPerfectSquare(320356, True)
    test_isPerfectSquare(95481, True)
    test_isPerfectSquare(0, True)
    test_isPerfectSquare(123, False)
    test_maximumPerfectSquareNum("""5 5
00000
00000
00200
00000
00000""", 0)
    test_maximumPerfectSquareNum(
    """2 3
123
456""", 64)
    test_maximumPerfectSquareNum("""6 7
3791178
1283252
4103617
8233494
8725572
2937261""", 320356)
    test_maximumPerfectSquareNum("""5 9
135791357
357913579
579135791
791357913
913579135""", 9)
    test_maximumPerfectSquareNum("""9 9
553333733
775337775
777537775
777357333
755553557
355533335
373773573
337373777
775557777""", -1)
    test_maximumPerfectSquareNum("""9 9
257240281
197510846
014345401
035562575
974935632
865865933
684684987
768934659
287493867""", 95481)
    test_maximumPerfectSquareNum("""9 9
000000000
000000000
100010004
000010092
001000704
000002003
100090026
000000000
001000001""", 49729)
    test_maximumPerfectSquareNum("""9 9
387527643
634972451
497863494
039670092
193472764
983762343
658793836
675894029
581234407""", 49729)
    test_maximumPerfectSquareNum("""1 1
1""", 1)
    test_maximumPerfectSquareNum("""1 1
0""", 0)
    test_maximumPerfectSquareNum("""3 1
0
0
1""", 100)

if __name__ == "__main__":
    test = 0
    if test == 1:
        test_fun()
    else:
        sol()