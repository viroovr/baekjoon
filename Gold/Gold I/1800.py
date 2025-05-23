"""
이분 탐색을 활용해야 겠다는 생각을 전혀 못했다.
dfs로 풀었지만 시간초과가 나서 검색해 풀이를 알아봤다.

다익스트라의 시간복잡도는 O(P log N)이다.
이분 탐색의 시간복잡도는 O(C)이다. C는 간선의 최대 비용이다.
총 시간복잡도는 O(PC log N)

factorial이나 2의 n승 꼴의 시간복잡도가 나온다면 이분탐색과 dp를 생각해보자.
37556	104
"""

import sys
input = sys.stdin.readline
from heapq import heappop, heappush

def is_possible(mid, N, K, g):
    distance = [float("inf")] * (N + 1)
    distance[1] = 0
    q = [(0, 1)]
    while q:
        cnt, now = heappop(q)
        for nxt, p in g[now]:
            nxt_cnt = cnt + (1 if p > mid else 0)
            if distance[nxt] > nxt_cnt:
                distance[nxt] = nxt_cnt
                heappush(q, (nxt_cnt, nxt))
    
    return distance[N] <= K

def get_min_cost(N, K, g, max_cost):
    left, right = 0, max_cost
    ans = -1
    while left <= right:
        mid = (left + right ) // 2
        if is_possible(mid, N, K, g):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    
    print(ans)

def sol():
    N, P, K = map(int, input().split())
    g = [[] for _ in range(N + 1)]
    max_cost = 0
    for _ in range(P):
        a, b, p = map(int, input().split())
        g[a].append((b, p))
        g[b].append((a, p))
        max_cost = max(max_cost, p)
    
    get_min_cost(N, K, g, max_cost)

sol()