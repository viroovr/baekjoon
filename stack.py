# Linked List
# s = []
# s.append(123)
# s.append(456)
# s.append(789)
# print("size : ", len(s))
# while len(s) > 0:
#     print(s[-1])
#     t = s.pop()
#     print(t)

# Queue

# thread - safe
# from queue import Queue

# double-ended queue
# from collections import deque

# q = deque()
# q.append(123)
# q.append(456)
# q.append(789)
# print(q)

# Priority Queue

# import heapq as hq

# pq = []
# hq.heappush(pq, 6)
# hq.heappush(pq, 12)
# hq.heappush(pq, 0)
# hq.heappush(pq, -5)
# hq.heappush(pq, 8)
# print(pq)

# while pq:
#     print(pq[0])
#     hq.heappop(pq)

# Map
m = {}
m["Hyeonwon"] = 40
m["Sky"] = 100
m["Jerry"] = 50
print("size : ", len(m))
for k in m:
    print(k, m[k], sep=",")
