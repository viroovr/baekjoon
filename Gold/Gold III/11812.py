"""
recursion을 이용한 stack은 iterate문이나, 일반 자료구조 stack을 활용해 변경할 수 
있음을 새기자

47820	372
47820	308 iterate문으로 변경
"""
import sys

def get_distance(x, y, K):
    if K == 1:
        return str(abs(x - y))

    dist = 0
    while x != y:
        if x < y:
            x, y = y, x

        qx, rx = divmod(x, K)

        x = qx if rx < 2 else qx + 1

        dist += 1

    return str(dist)

def sol():
    global N, Q
    data = sys.stdin.read().split("\n")
    N, K, Q = map(int, data[0].split())

    result = []
    for i in range(1, Q + 1):
        x, y = map(int, data[i].split())
        result.append(get_distance(x, y, K))
    
    print("\n".join(result))

sol()