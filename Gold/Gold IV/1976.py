"""
rank를 parent의 root에 음수로 저장하는 방법을 사용해봤다.
하지만 이 문제는, rank를 유지할 필요없이 그냥 parent의 대소구분으로만 해도
가능하다.
그저, 연결 유무만 중요하니깐
32412	36
"""

import sys
input = sys.stdin.readline

def is_possible_plan(N, M, graph, plan):
    parent = [-1] * N

    def find_parent(a):
        if parent[a] < 0:
            return a
        parent[a] = find_parent(parent[a])
        return parent[a]

    def union(a, b):
        root_a, root_b = find_parent(a), find_parent(b)
        if root_a == root_b:
            return

        if parent[root_a] > parent[root_b]:
            parent[root_a] = root_b
        else:
            if parent[root_a] == parent[root_b]:
                parent[root_a] -= 1
            parent[root_b] = root_a

    for i in range(N):
        for j in range(i + 1):
            if graph[i][j] == "1":
                union(i, j)

    p = find_parent(plan[0])
    for i in range(1, M):
        if p != find_parent(plan[i]):
            return "NO"
    return "YES"

def sol():
    N = int(input().rstrip())
    M = int(input().rstrip())

    graph = [input().split() for _ in range(N)]
    plan = tuple(map(lambda x: int(x) - 1, input().split()))

    print(is_possible_plan(N, M, graph, plan))

sol()
    