"""
아이디어를 트리의 중위 순위 탐색으로 잡았는데, 틀렸다. 이전 요소까지 고려하는게
아닌가 보다. 후위 순위로 탐색해야하고 stack에 쌓으며 나아가야한다.
위상 정렬 문제인데 새롭게 알았으니 배워두자

dfs후위 순위 탐색 + 스택말고도 큐를 이용한 indegree방식도 있다.
41396	120
"""

import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline
    
def sol():
    N, M = map(int, input().split())
    trees = [[] for _ in range(N + 1)]
    for _ in range(M):
        A, B = map(int, input().split())
        trees[A].append(B)
    
    visited = [False] * (N + 1)
    result = []

    def dfs(x):
        visited[x] = True
        for node in trees[x]:
            if not visited[node]:
                dfs(node)
        result.append(x)
    
    for i in range(1, N + 1):
        if not visited[i]:
            dfs(i)
    
    print(" ".join(map(str, reversed(result))))

sol()