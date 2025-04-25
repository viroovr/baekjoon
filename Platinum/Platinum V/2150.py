"""
dfs를 두번 해야하는 것까지는 생각했지만 연결요소 끼리 묶는 방법에 대해 생각해내지 못했다.
검색을 통해 알고리즘을 알아냈다. Kosaraju 알고리즘을 사용해서 풀었다.
dfs 두 번을 실행하면서 첫 번째는 방문이 끝난 순서대로 stack에 저장한다.
두 번째는 stack에서 요소를 꺼내며 scc로 묶는다.
stack에서 요소를 꺼낼 때, 이 요소가 마지막 방문이고 SCC의 root일 가능성이 높다.
꺼낸 요소를 transposne한 graph에서 탐색하며, scc를 이룬다.

이 외에도 Tarjan 알고리즘도 존재한다.
Tarjan알고리즘은 각 노드에 id를 부여한다. id는 방문 순서이다.
낮은 방문 순서를 가진 것이 root노드이다.
방문 되는 노드들은 방문 순서가 가장 낮은 노드를 가리킨다.
순서를 잘 생각해야 한다.
40136	3692
43080	156     transpose 그래프 초기화. 두 번의 dfs 반복문 분리
"""

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def get_scc(V, graph, rev_graph):
    visited = [False] * (V + 1)
    stack = []

    def dfs(node):
        visited[node] = True
        for nxt in graph[node]:
            if not visited[nxt]:
                dfs(nxt)
    
        stack.append(node)

    for i in range(1, V + 1):
        if not visited[i]:
            dfs(i)

    visited = [False] * (V + 1)
    result = []

    def t_dfs(node, component):
        visited[node] = True
        component.append(node)
        for nxt in rev_graph[node]:
            if not visited[nxt]:
                t_dfs(nxt, component)
    
    while stack:
        node = stack.pop()
        if not visited[node]:
            component = []
            t_dfs(node, component)
            result.append(sorted(component))

    print(len(result))
    for row in sorted(result):
        print(" ".join(map(str, row)) + " -1")
    
def sol():
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    rev_graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        A, B = map(int, input().split())
        graph[A].append(B)
        rev_graph[B].append(A)
    
    get_scc(V, graph, rev_graph)

sol()