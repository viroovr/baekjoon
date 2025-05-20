"""
아이디어를 얻고 푸는 풀이와 시간차이가 100배 이상 나는 문제

첫 풀이는 BFS를 활용해서 query마다 BFS를 이용해 usado를 구한다.
BFS의 시간복잡도는 O(V + E)이지만, E는 V - 1이므로 O(V)에 수렴한다.
각 쿼리마다 BFS를 돌리므로 O(QV). QV ~= 25,000,000
느리다.
34976	7932
두 번째 풀이는 GPT에게서 Union find아이디어를 얻었다.
오프라인 쿼리라는 아이디어도 함께 알았다.
edge를 가중치로 내림차순으로 구하고, query도 내림차순으로 구한다.
query의 k값 보다 큰 edges들을 union find로 dijoint set을 만들고 v의
disjoint set크기를 쿼리의 idx에 대입한다.
O(QlogQ + NlogN)
34456	56

아이디어가 참신하다.
"""

import sys
input = sys.stdin.readline

def find(x):
    if parent[x] < 0:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[x] += parent[y]
        parent[y] = x


N, Q = map(int, input().split())
edges = []
for _ in range(N - 1):
    p, q, r = map(int, input().split())
    edges.append((r, p, q))

edges.sort(key=lambda x: -x[0])

queries = []
for i in range(Q):
    k, v = map(int, input().split())
    queries.append((k, v, i))

queries.sort(key=lambda x: -x[0])

parent = [-1] * (N + 1)
j = 0
ans = [0] * Q

for k, v, idx in queries:
    while j < len(edges) and edges[j][0] >= k:
        _, p, q = edges[j]
        union(p, q)
        j += 1
    ans[idx] = -parent[find(v)] - 1

for a in ans:
    print(a)
        