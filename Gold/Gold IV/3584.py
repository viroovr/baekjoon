"""
dfs를 사용하면 sys.setrecursionlimit 조건 확인하기
dfs내에 함수 순서 확인하기
34760	948
34760	56  input
"""

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def get_lca(N, parent, x, y):
    visited = [False] * (N + 1)
    def dfs(x):
        if visited[x]:
            return x

        visited[x] = True

        if parent[x] == -1:
            return -1
        return dfs(parent[x])
    
    dfs(x)
    return dfs(y)
    

def sol():
    T = int(input())
    result = []
    for _ in range(T):
        N = int(input())
        parent = [-1] * (N + 1)
        for _ in range(N - 1):
            A, B = map(int, input().split())
            parent[B] = A
        
        result.append(get_lca(N, parent, *map(int, input().split())))
    
    print("\n".join(map(str, result)))
        
sol()