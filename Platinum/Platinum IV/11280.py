"""
SAT 문제이다. SCC내에 모순만 되지 않으면 T/F판별이 가능하다.
T가 결정되는 요소들은 위상정렬 후 F를 대입하면서 훑거나
역순으로 훑는다면 T가 되도록 대입해 나간다.

그래프로 풀어나갈 것임은 알았지만, 이게 논리구조에서 그래프가 어떻게 결정되는지를
캐치하지 못했다. 이산수학에서 배운 p->q와 ^p V q를 생각해냈다면 풀어냈을 지도 모른다.

하지만 그렇더라도 SCC내에 x와 -x 요소가 포함되어있는지 여부가 T/F를 판별 여부를 알수 있는지
생각하는 것도 어렵긴 하다.
48264	276
"""

import sys
input = sys.stdin.readline
from collections import defaultdict
sys.setrecursionlimit(10**6)
def is_true(N, graph):
    vo = defaultdict(int)
    parent = defaultdict(int)
    idx = 0

    stack = []
    on_stack = defaultdict(bool)
    
    def dfs(node):
        nonlocal idx
        idx += 1
        vo[node] = parent[node] = idx
        stack.append(node)
        on_stack[node] = True

        for nxt in graph[node]:
            if vo[nxt] == 0:
                dfs(nxt)
                parent[node] = min(parent[nxt], parent[node])
            elif on_stack[nxt]:
                parent[node] = min(vo[nxt], parent[node])
        
        if parent[node] == vo[node]:
            scc = set()
            while stack:
                top = stack.pop()
                on_stack[top] = False
                if abs(top) in scc:
                    print(0)
                    sys.exit(0)

                scc.add(abs(top))
                if top == node:
                    break

    for i in range(1, N + 1):
        if vo[i] == 0:
            dfs(i)
        if vo[-i] == 0:
            dfs(-i)
    
    print(1)
    
def sol():
    N, M = map(int, input().split())
    graph = defaultdict(list)
    
    for _ in range(M):
        a, b = map(int, input().split())
        graph[-a].append(b)
        graph[-b].append(a)
    
    is_true(N, graph)

sol()
