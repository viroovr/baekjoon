"""
두번의 dfs를 통해 2개의 일을 처리하도록 한다.
63900	212
"""

from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(10**4)

def get_bimatch(N, M, graph):
    match_v = [0] * (M + 1)
    # match_u = [0] * (N + 1)
    def dfs(u):
        for v in graph[u]:
            if not match_v[v]:
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
    for u in range(1, N + 1):
        visited = [False] * (M + 1)
        if dfs(u):
            res += 1
        if dfs(u):
            res += 1
        
        if res == M:
            break
    
    return res

def sol():
    N, M = map(int, input().split())
    graph = [[]] + [list(map(int, input().split()))[1:] for _ in range(N)]
    print(get_bimatch(N, M, graph))

sol()