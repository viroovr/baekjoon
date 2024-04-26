from collections import deque
N, M = map(int, input().split())
q = deque([x for x in range(N)])
want = list(map(int, input().split()))
print(q)