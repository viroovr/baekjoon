N = int(input())
count = 0
remain_hour = 3

if N - 3 >= 0:
    count = count + 60 ** 2
    remain_hour = remain_hour + N - 3
else:
    remain_hour = N + 1
if N - 13 >= 0:
    count = count + 60 ** 2
    remain_hour = remain_hour + 9
    remain_hour = remain_hour + N - 13

t = (6 * 10) ** 2 - (5 * 9) ** 2
count = count + t * remain_hour

print(count)
