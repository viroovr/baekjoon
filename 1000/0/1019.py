from math import log10
N = int(input())
nl = map(str, [x for x in range(1, N + 1)])
num_list = [0] * 10


def get_num_list(n):
    t = list(reversed(str(n)))
    ret = [0] * 10
    for i, v in enumerate(t):
        if n == N:
            print(f"gg i : {i}, v : {v}")
        if i > 0:
            if n == N:
                print(f"i : {i}, v : {v}, int(t[i - 1]) : {int(t[i - 1])}")
            for _ in range(int(v)):
                for j, k in enumerate(dp[i - 1]):
                    ret[j] += k
            # p = (int(t[i - 1])) * 10 ** (i - 1)
            p = n % (10 ** i) + 1
            if n == N:
                print("p:   ", p)
            ret[int(v)] += p
            for j in range(1, int(v)):
                ret[j] += 10 ** i
            if 0 < i < len(str(n)) - 1:
                if int(v) != 0:
                    if int(t[i + 1]) != 0:
                        if i != len(str(n)) - 2:
                            u = (10 ** i) * (int(t[i + 1]) + 1)
                        else:
                            u = (10 ** i) * (int(t[i + 1]))
                    else:
                        u = (10 ** i) * (int(t[i + 1]) + 1)
                else:
                    if int(t[i + 1]) != 0:
                        if i != len(str(n)) - 2:
                            u = (10 ** i) * (int(t[i + 1]))
                        else:
                            u = (10 ** i) * (int(t[i + 1]) - 1)
                    else:
                        if i != len(str(n)) - 2:
                            u = (10 ** i) * (int(t[i + 1]) + 1)
                        else:
                            u = (10 ** i) * (int(t[i + 1]))
                    
                ret[0] += u
                if n == N:
                    print("u:   ", u)
        else:
            for j in range(0, int(v) + 1):
                ret[j] += 1
    return ret


# print(list(t))
num_len = len(str(N)) - 1
# print(num_len)
dp = []
for i in range(len(str(N))):
    j = 10 ** (i + 1) - 1
    dp.append(get_num_list(j))
num_list = get_num_list(N)
print(dp)

an_num = [0] * 10
for x in nl:
    for c in x:
        an_num[int(c)] += 1
num_list[0] -= 1
print("num_list:    ", num_list)
print("an_num:      ", an_num)