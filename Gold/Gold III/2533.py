"""
tree의 dp 문제. 적으면서 아이디어를 정리하면 더 잘풀리는 것 같다.

317720	4892    함수 recursion dfs
305264	4136    리스트 stack으로 order형성 후, 리프부터 dp 설정
305088	4104    deque로 형성
"""

import sys
from collections import deque
input = sys.stdin.readline

def get_early_adaptors(N, edges):
    dp = [[0, 0] for _ in range(N + 1)]
    visited = [False] * (N + 1)
    parent = [0] * (N + 1)

    q = deque([1])
    order = []
    visited[1] = True

    while q:
        node = q.popleft()
        order.append(node)
        for child in edges[node]:
            if not visited[child]:
                q.append(child)
                visited[child] = True
                parent[child] = node
    
    for node in reversed(order):
        dp[node][1] = 1
        for child in edges[node]:
            if child == parent[node]:
                continue

            dp[node][0] += dp[child][1]
            dp[node][1] += min(dp[child][0], dp[child][1])
    print(min(dp[1][0], dp[1][1]))

def main():
    N = int(input().rstrip())
    edges = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = map(int, input().rstrip().split())
        edges[a].append(b)
        edges[b].append(a)
    
    get_early_adaptors(N, edges)

if __name__ == "__main__":
    main()
