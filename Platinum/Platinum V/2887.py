"""
초밀집 그래프에서 MST만드는 아이디어가 필요하다.
O(N^2)이 당연할 거라 생각했는데, 거리 규칙이 단순하다면 O(NlogN)으로 가능한게
신기하다.
92384	1064
"""
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def get_min_cost(N, planets):
    parent = [i for i in range(N)]

    def find(x):
        nonlocal parent
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        root_x, root_y = find(x), find(y)
        if root_x == root_y:
            return False
        if root_x < root_y:
            parent[root_y] = root_x
        else:
            parent[root_x] = root_y
        return True

    edges = []
    for i in range(3):
        t = sorted(planets, key=lambda x: x[i])
        for j in range(N - 1):
            dist = abs(t[j][i] - t[j + 1][i])
            heappush(edges, (dist, t[j][3], t[j + 1][3]))
    
    cost = 0
    cnt = 0
    while edges:
        min_dist, x, y = heappop(edges)
        if union(x, y):
            cost += min_dist
            cnt += 1
            if cnt == N - 1:
                break

    return cost

def sol():
    N = int(input())
    planets = []
    for i in range(N):
        x,y,z = map(int, input().split())
        planets.append((x,y,z,i))
    print(get_min_cost(N, planets))

sol()