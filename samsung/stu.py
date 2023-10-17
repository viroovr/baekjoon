import heapq

pq = []
heapq.heappush(pq, 1)
heapq.heappush(pq, 9)
heapq.heappush(pq, 5)
heapq.heappush(pq, 10)
heapq.heappush(pq, 7)
print(pq)
while pq:
    print(heapq.heappop(pq))