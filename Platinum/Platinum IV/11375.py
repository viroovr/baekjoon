"""
이분 매칭 문제이다.
기존 코드에서는 모든 간선을 접근할 때, 도착 노드의 visited여부를 판단하며 match_v를 연결했다.

20배정도 빠른 코드에서는 방문하지 않은 도착 노드를 발견하면 visited 조건없이 바로 match_v를 연결했다.
만약 방문하지 않은 노드가 없으면 visited안 된 노드들에서 dfs를 탐색한다.

모든 간선에서 visited 확인을 하느냐 안하는냐 차이같다.

63196	5860
62884	264
"""

import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**4)

def get_bimatch(N, M, graph):
    match_v = [-1] * M
    
    def dfs(u):
        for v in graph[u]:
            if match_v[v] == -1:
                match_v[v] = u
                return True
        for v in graph[u]:
            if visited[v]:
                continue
            visited[v] = True
            if dfs(match_v[v]):
                match_v[v] = u
                return True
        return False

    res = 0
    for u in range(N):

        visited = [False] * M

        if dfs(u): 
            res += 1
            if res == M:
                break

    return res


def sol():
    N, M = map(int, input().split())
    graph = [list(map(lambda x : int(x) - 1, input().split()))[1:] for _ in range(N)]
    
    print(get_bimatch(N, M, graph))

sol()