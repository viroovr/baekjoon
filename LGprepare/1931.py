import sys
input = sys.stdin.readline
schedules = [tuple(map(int, input().split())) for _ in range(int(input()))]
sched = []
count = 0
for i in sorted(schedules, key=lambda x: (x[1], x[0])):
    if sched:
        k = sched[-1]
        if i[0] >= k[1]:
            sched.append(i)
            count += 1
    else:
        sched.append(i)
        count += 1
print(count)
