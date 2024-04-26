from math import sqrt
from bisect import bisect_right, bisect_left
from bisect import bisect

def isPrime(x):
    for i in range(3, int(sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True


def get_answer(nl, dic):
    global N, prime
    if len(dic[0]) != N // 2:
        return [-1]
    key = nl[0] % 2
    op = 0 if key else 1
    ret = {x: set() for x in dic[key]}
    for x in dic[key]:
        for k in prime:
            if k <= x:
                continue
            br = bisect_right(dic[op], k - x)
            if 0 < br - bisect_left(dic[op], k - x):
                ret[x].add(k - x)
            elif N // 2 == br:
                break
    u = set()
    for x in ret.values():
        u = u.union(x)
    print(u)
    # for t in ret[nl[0]]:
    #     mark = {x: False for x in u}
    #     mark[t] = True
    #     for k in u:
    #         for t in ret.values():
            
    # for x in ret[nl[0]]:
    #     le = [list(k) for k in ret.values()]
    #     for c in le:
    #         try:
    #             c.remove(x)
    #         except ValueError:
    #             pass
                
    print(ret)
    return ret[nl[0]]



N = int(input())
nl = list(map(int, input().split()))
dic = {0: [], 1: []}
for x in nl:
    dic[x % 2].append(x)
dic[0].sort()
dic[1].sort()
print(dic)
# N = 50
# [1 2 3 4 5 6 7 999 1000]
prime = [3]
prime.extend([x for x in range(5, 2000, 2) if isPrime(x)])
print(N, nl, prime[:10], len(prime))
print(" ".join(map(str, get_answer(nl, dic))))