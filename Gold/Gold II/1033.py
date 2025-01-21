from time import time
from math import gcd

def logger(func):
    def wrapper(*args):
        s = time()
        func(*args)
        e = time()
        print(f"{func.__name__} is ended in {e - s:.5f}")
        return func
    return wrapper

def find_first(n, graph, i):
    mark = [False for _ in range(n)]
    queue = [i]
    mark[i] = True
    while queue:
        k = queue.pop()
        for j in range(n):
            if graph[k][j] != -1 and not mark[j]:
                mark[j] = True
                queue.append(j)
    if mark.count(True) == n:
        return i
    else:
        return -1

def getIngredeients(n, ingredientsRatio):
    ret = [[1, 1] for _ in range(n)]
    mark = [False for _ in range(n)]
    graph = [[-1 for _ in range(n)] for _ in range(n)]
    for a, b, p, q in ingredientsRatio:
        graph[a][b] = (q, p)
    k = 0
    for i in range(n):
        k = find_first(n, graph, i)
        if k != -1:
            break
    if k == -1:
        for a, b, p, q in ingredientsRatio:
            graph[b][a] = (p, q)
        for i in range(n):
            k = find_first(n, graph, i)
            if k != -1:
                break
    mark[k] = True
    queue = [k]
    while queue:
        t = queue.pop()
        for i in range(n):
            if graph[t][i] != -1 and not mark[i]:
                p, q = graph[t][i]
                cd = gcd(p, q)
                ret[i][0] *= (p // cd) * ret[t][0]
                ret[i][1] *= (q // cd) * ret[t][1]
                mark[i] = True
                queue.append(i)
    mul = 1
    for i in range(n):
        mul *= ret[i][1]
    for i in range(n):
        ret[i][0] *= mul // ret[i][1]
    k = gcd(ret[0][0], ret[1][0])
    for i in range(1, n):
        k = gcd(k, ret[i][0])
    
    return [i // k for i, j in ret]

@logger
def test_getIngredients(n, ingredientsRatio, expected):
    a = getIngredeients(n, ingredientsRatio)
    assert a == expected, f"{expected} expected but {a}."

def sol():
    n = int(input())
    ingredientsRatio = [list(map(int, input().split())) for _ in range(n - 1)]
    print(*getIngredeients(n, ingredientsRatio))

def test_fun():
    test_getIngredients(5, [[4,0,1,1], [4,1,3,1], [4,2,5,1], [4,3,7,1]], [105,35,21,15,105])
    test_getIngredients(2, [[0, 1, 6, 4]], [3, 2])
    test_getIngredients(3, [[0,1,9,8], [1,2,9,8]], [81,72,64])
    test_getIngredients(4, [[2,3,6,8],[0,1,9,3],[3,0,7,5]], [60,20,63,84])
    test_getIngredients(2, [[0, 1, 1, 1]], [1, 1])
    test_getIngredients(10, [[0,1,2,1],[1,2,5,4],[1,3,3,2],[0,4,7,3],[4,5,2,3],[4,6,3,1],[4,7,8,9],[7,8,7,5],[9,7,3,7]]
    ,[5880,2940,2352,1960,2520,3780,840,2835,2025,1215])


if __name__ == "__main__":
    test = 0
    if test == 1:
        test_fun()
    else:
        sol()