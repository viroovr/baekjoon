from math import sqrt
# import time


def isPrime(x):
    for i in range(3, int(sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True


cmin, cmax = map(int, input().split())
# start = time.time()
# 1000000000000 1000001000000
# 999958000441 999959000441
t = int(sqrt(cmax)) + 1
# print(t)
prime = [4, 9]
prime.extend([x ** 2 for x in range(5, t, 2) if isPrime(x)])
# print(cmin, t ** 2, cmax, int(sqrt(cmax)))

total = set()
for x in prime:
    a = cmin // x
    # print(f"a, b {a}, {b}")
    for i in range(a + 1 if cmin % x != 0 else a, cmax // x + 1):
        total.add(i * x)
    # for i in range(a, b):

# le = set([x for x in range(cmin, cmax + 1)])
ans = cmax - cmin + 1 - len(total)
# adsf = le.difference(total)
# print(f"num {num}, ans {ans}, le_diff {adsf}, len(le_diff) {len(adsf)}, total {total}")
# print(f"num {num}, ans {ans}")
# end = time.time()
# print(end - start)
# print(f"num {num}, ans {ans}, total {total}")
# print(total)
print(ans)
# print(prime[-21:-1])
