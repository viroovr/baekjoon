from itertools import combinations
N, M = map(int, input().split())
house = []
chick = []
for i in range(N):
    line = list(map(int, input().split()))
    # print(line)
    for j in range(N):
        if line[j] == 1:
            house.append((i + 1, j + 1))
        elif line[j] == 2:
            chick.append((i + 1, j + 1))

# print(house)
comb = combinations(chick, M)
chicklen = 2500 * 100
for k in comb:
    citydis = 0
    for u in house:
        citydis += min(abs(u[0] - i[0]) + abs(u[1] - i[1]) for i in k)
    chicklen = min(chicklen, citydis)
print(chicklen)
# print(100 * 1716 * 13) = 2_230_800
# print(13*12*11*10*9*8/(6*5*4*3*2*1))
# 100 * 1716 * 13
