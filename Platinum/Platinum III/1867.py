"""
정답률이 57%이길래 쉬운 문제인줄 알고 접근했다가 큰 코 다쳤다.

row와 col degree를 매번 갱신하며, 큰 순서대로 greedy하게 점을 선택했다. 하지만
매번 갱신하는 것은 시간초과를 유발한다. O(N^2 * K)

결국 검색을 통해, 이 문제는 이분 매칭을 이용해야 함을 알았다.
점을 간선으로 생각하는 아이디어와 함께, Row group: R, Col group: C라 할 때, R -> C로의 이분 매칭을
통해 푼다.

R과 C의 각 점은 항상 한 개 이상의 간선을 가지므로 비어있는 노드 없이 이분 매칭을 선택하면 된다.
그렇다면 선택되지 않은 V그룹 노드는 결괏값에 포함하지 않는다.
32456	44
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

def get_run(N, K, graph):
    # print(graph)

    match_u = [-1] * N
    match_v = [-1] * N

    def dfs(u):
        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                if match_v[v] == -1 or dfs(match_v[v]):
                    match_u[u] = v
                    match_v[v] = u
                    return True

        return False

    res = 0
    for u, lis in enumerate(graph):
        if lis:
            visited = set()
            if dfs(u): res += 1
    
    # print(match_u, match_v)
    return res

def sol():
    N, K = map(int, input().split())
    graph = [[] * N for _ in range(N)]
    for _ in range(K):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)
    
    print(get_run(N, K, graph))

sol()