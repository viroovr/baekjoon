# from math import log10
# N = int(input())
# nl = map(str, [x for x in range(1, N + 1)])
# num_list = [0] * 10


# def get_num_list(n):
#     t = list(reversed(str(n)))
#     ret = [0] * 10
#     for i, v in enumerate(t):
#         if n == N:
#             print(f"gg i : {i}, v : {v}")
#         if i > 0:
#             if n == N:
#                 print(f"i : {i}, v : {v}, int(t[i - 1]) : {int(t[i - 1])}")
#             for _ in range(int(v)):
#                 for j, k in enumerate(dp[i - 1]):
#                     ret[j] += k
#             # p = (int(t[i - 1])) * 10 ** (i - 1)
#             p = n % (10 ** i) + 1
#             if n == N:
#                 print("p:   ", p)
#             ret[int(v)] += p
#             for j in range(1, int(v)):
#                 ret[j] += 10 ** i
#             if 0 < i < len(str(n)) - 1:
#                 if int(v) != 0:
#                     if int(t[i + 1]) != 0:
#                         if i != len(str(n)) - 2:
#                             u = (10 ** i) * (int(t[i + 1]) + 1)
#                         else:
#                             u = (10 ** i) * (int(t[i + 1]))
#                     else:
#                         u = (10 ** i) * (int(t[i + 1]) + 1)
#                 else:
#                     if int(t[i + 1]) != 0:
#                         if i != len(str(n)) - 2:
#                             u = (10 ** i) * (int(t[i + 1]))
#                         else:
#                             u = (10 ** i) * (int(t[i + 1]) - 1)
#                     else:
#                         if i != len(str(n)) - 2:
#                             u = (10 ** i) * (int(t[i + 1]) + 1)
#                         else:
#                             u = (10 ** i) * (int(t[i + 1]))
                    
#                 ret[0] += u
#                 if n == N:
#                     print("u:   ", u)
#         else:
#             for j in range(0, int(v) + 1):
#                 ret[j] += 1
#     return ret


# # print(list(t))
# num_len = len(str(N)) - 1
# # print(num_len)
# dp = []
# for i in range(len(str(N))):
#     j = 10 ** (i + 1) - 1
#     dp.append(get_num_list(j))
# num_list = get_num_list(N)
# print(dp)

# an_num = [0] * 10
# for x in nl:
#     for c in x:
#         an_num[int(c)] += 1
# num_list[0] -= 1
# print("num_list:    ", num_list)
# print("an_num:      ", an_num)

from time import time
from collections import Counter

def test_logger(func):
    def wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        end = time()
        print(f"{func.__name__} ended in {end - start:.5f}sec")
        return func
    return wrapper

# def countNum(n):
#     if n < 10:
#         ret = {i: 1 for i in range(1, n + 1)}
#         t = [0] * 10
#         for i, v in ret.items():
#             t[int(i)] += v
#         return t
#     ret = Counter()
#     accumulation = [Counter(), Counter()]
#     r = len(str(n))
#     k = 1
#     while r >= k:
#         if r > k:
#             for i in range(10):
#                 accumulation[k] += Counter({str(i): 10 ** (k - 1)}) + accumulation[k - 1]
#             if k == r - 1 and str(n)[0] == '1':
#                 accumulation[k]['0'] -= sum([10 ** p for p in range(k)])
#         else:
#             for i, v in enumerate(list(str(n))):
#                 if i == r - 1:
#                     for j in range(int(v) + 1):
#                         ret += Counter(str(j))
#                 else:
#                     for j in range(int(v)):
#                         if j != 0:
#                             ret += Counter({str(j): 10 ** (k - 1 - i)}) + accumulation[k - 1 - i]
#                         else:
#                             ret += accumulation[k - 1 - i]
#                     ret += Counter({str(n)[i]: n % (10 ** (k - i - 1)) + 1})
#         accumulation.append(Counter())
#         k += 1
#     t = [0] * 10
#     for i, v in ret.items():
#         t[int(i)] += v
#     if str(n)[0] != '1':
#         t[0] -= 1
#     return t

def countNum(n):
    # 결과를 저장할 배열 (0~9)
    result = [0] * 10

    # 자리수별로 계산 (10의 자리, 100의 자리, ...)
    factor = 1
    while n >= factor:
        lower = n - (n // factor) * factor
        current = (n // factor) % 10
        higher = n // (factor * 10)

        # 현재 자리수에서 0~9의 등장 횟수 계산
        for i in range(10):
            if i < current:
                result[i] += (higher + 1) * factor
            elif i == current:
                result[i] += higher * factor + lower + 1
            else:
                result[i] += higher * factor

        # 0은 자리수가 0 이상일 때만 등장 (예외 처리)
        if factor > 1:
            result[0] -= factor

        factor *= 10
    result[0] -= 1
    return result
        

@test_logger
def test_countNum1():
    n = 11
    expected = [1,4,1,1,1,1,1,1,1,1]
    # 1 2 3 4 5 6 7 8 9 10 11
    # 1 4 1 1 1 1 1 1 1 1
    u = countNum(n)
    assert u == expected, f"{n} expected {expected} but {u}"

@test_logger
def test_countNum11():
    n = 7
    expected = [0,1,1,1,1,1,1,1,0,0]
    # 1 2 3 4 5 6 7 8 9 10 11
    # 1 4 1 1 1 1 1 1 1 1
    u = countNum(n)
    assert u == expected, f"expected {expected} but {u}"

@test_logger
def test_countNum2():
    n = 19
    expected = [1,12,2,2,2,2,2,2,2,2]
    # 1 2 3 4 5 6 7 8 9 10
    # 11 12 13 14 15 16 17 18 19
    # 1 12 2 2 2 2 2 2 2 2
    u = countNum(n)
    assert u == expected, f"expected {expected} but {u}"

@test_logger
def test_countNum21():
    n = 20
    expected = [2,12,3,2,2,2,2,2,2,2]
    # 1 2 3 4 5 6 7 8 9 10
    # 11 12 13 14 15 16 17 18 19
    # 1 12 2 2 2 2 2 2 2 2
    u = countNum(n)
    assert u == expected, f"expected {expected} but {u}"

@test_logger
def test_countNum22():
    n = 100
    expected = [11,21,20,20,20,20,20,20,20,20]
    # 1 2 3 4 5 6 7 8 9 10
    # 11 12 13 14 15 16 17 18 19
    # 1 12 2 2 2 2 2 2 2 2
    u = countNum(n)
    assert u == expected, f"expected {expected} but {u}"

@test_logger
def test_countNum23():
    n = 149
    expected = [24,85,35,35,35,25,25,25,25,25]
    # 1 2 3 4 5 6 7 8 9 10
    # 11 12 13 14 15 16 17 18 19
    # 1 12 2 2 2 2 2 2 2 2
    u = countNum(n)
    assert u == expected, f"expected {expected} but {u}"

@test_logger
def test_countNum24():
    n = 247
    expected = [44,155,103,55,53,45,45,45,44,44]
    # 1 2 3 4 5 6 7 8 9 10
    # 11 12 13 14 15 16 17 18 19
    # 1 12 2 2 2 2 2 2 2 2
    u = countNum(n)
    assert u == expected, f"expected {expected} but {u}"

@test_logger
def test_countNum31():
    n = 999
    expected = [189,300,300,300,300,300,300,300,300,300]
    # 1 2 3 4 5 6 7 8 9 10
    # 11 12 13 14 15 16 17 18 19
    # 1 12 2 2 2 2 2 2 2 2
    u = countNum(n)
    assert u == expected, f"{n} expected {expected} but {u}"

@test_logger
def test_countNum3():
    n = 1000
    expected = [192,301,300,300,300,300,300,300,300,300]
    # 1 2 3 4 5 6 7 8 9 10
    # 11 12 13 14 15 16 17 18 19
    # 1 12 2 2 2 2 2 2 2 2
    u = countNum(n)
    assert u == expected, f"{n} expected {expected} but {u}"

@test_logger
def test_countNum32():
    n = 1001
    expected = [194,303,300,300,300,300,300,300,300,300]
    # 1 2 3 4 5 6 7 8 9 10
    # 11 12 13 14 15 16 17 18 19
    # 1 12 2 2 2 2 2 2 2 2
    u = countNum(n)
    assert u == expected, f"{n} expected {expected} but {u}"

@test_logger
def test_countNum4():
    n = 543212345
    expected = [429904664,541008121,540917467,540117067,533117017,473117011,429904664,429904664,429904664,429904664]
    # 1 2 3 4 5 6 7 8 9 10
    # 11 12 13 14 15 16 17 18 19
    # 1 12 2 2 2 2 2 2 2 2
    u = countNum(n)
    assert u == expected, f"{n} expected {expected} but {u}"

def test_func():
    test_countNum1()
    test_countNum11()
    test_countNum2()
    test_countNum24()
    test_countNum21()
    test_countNum22()
    test_countNum23()
    test_countNum3()
    test_countNum31()
    test_countNum32()
    test_countNum4()


def solution():
    N = int(input())
    k = countNum(N)
    print(*k)

if __name__ == "__main__":
    test = 0
    if test == 1:
        test_func()
    else:
        solution() 