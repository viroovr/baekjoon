import sys
import heapq

input = sys.stdin.readline
num = int(input())
pq = []
for _ in range(num):
    x = int(input())
    if x != 0:
        heapq.heappush(pq, (abs(x), x))
    else:
        print(heapq.heappop(pq)[1] if pq else 0)