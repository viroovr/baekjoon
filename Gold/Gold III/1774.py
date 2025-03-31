"""
MST를 구하는 문제이지만 미리 연결된 요소들이 있다. 이 요소들은 비용이 0으로 연결되있고 새로 연결될
것만 고려하면 된다.

미리 연결된 요소들에 대해 어떻게 처리하는지가 시간단축에 핵심이다.

M으로 주어진 요소들은 union으로 tree화 한다.
find(i) != find(j) 인 요소들만 edges에 추가한다.
edges.sort()는 10^6 * 20 으로 10*7 연산이 필요하다. 최소 edge만 뽑는 것이므로 우선순위 큐를 이용해 시간단축
한다.

다음 최소 거리를 뽑아내면서, 종료 조건을 확인해야 한다. parent[find(i)]가 -N이면 종료하도록 했다.

1. heapq
2. union에서 root size에 tree height가 아닌, 포함된 node 수를 가지게함
3. 2중 for문에서 j요소가 이미 처리된 요소는 포함이 안되도록 함.
    3.1 find
    3.2 j가 i + 1 ~ N
4. 종료 조건
    4.1 parent에서 음수 값이 1개인 경우만
    4.2 parent[find(i)] == -N
182108	1532    
178708	1580   2, 4.1
182108	1680   2, 3.1, 4.1
195340	1920   2, 3.1, find(i) == -N -> 잘못된 확인법
195340	1316   2, 3.1, 4.2
177904	756    2, 3.1, 4.2, 1
109212	384    2, 3.1, 4.2, 1, 3.2
"""
from heapq import heappop, heappush
import sys
input = sys.stdin.readline
def find(a):
    if parent[a] < 0:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    if a == b:
        return False
    root_a = find(a)
    root_b = find(b)

    if root_a != root_b:
        if parent[root_a] < parent[root_b]:
            parent[root_a] += parent[root_b]
            parent[root_b] = root_a
        else:
            parent[root_b] += parent[root_a]
            parent[root_a] = root_b
        return True
    return False

def sol():
    global parent
    N, M = map(int, input().split())
    coords = [-1]
    for i in range(N):
        x, y = map(int, input().split())
        coords.append((x, y))

    parent = [-1] * (N + 1)
    for _ in range(M):
        i, j = map(int, input().split())
        union(i, j)

    edges = []
    for i in range(1, N + 1):
        x1, y1 = coords[i]
        root_i = find(i)
        for j in range(i + 1, N + 1):
            if root_i != find(j):
                x2, y2 = coords[j]
                d = (x1 - x2) ** 2 + (y1 - y2) ** 2
                heappush(edges, (d, i, j))
    
    res = 0

    while edges:
        d, i, j = heappop(edges)
        if union(i, j):
            res += d ** 0.5
            if parent[find(i)] == -N:
                break
        
    print(f"{res:.2f}")

sol()
