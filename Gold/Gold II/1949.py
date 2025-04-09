"""
적어도 한 개의 우수마을과 인접해야 한다는 조건이 헷갈리게 만드는 문제다.
아무것도 인접하지 않은 마을은 최적해가 안된다는 것을 생각하면 쉽게 답을 내릴 수 있는 문제다.
반대 가정을 해봐야 겠다.

37448	60  dfs로 subtree의 dp설정
36424	60  dp없이 dfs return
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
def get_great_village_cnt(N, villagers, edges):
    def dfs(node, parent):
        include, notinclude = villagers[node], 0

        for child in edges[node]:
            if child == parent:
                continue

            i, ni = dfs(child, node)

            include += ni
            notinclude += max(i, ni)

        return include, notinclude
    print(max(dfs(1, -1)))

def sol():
    N = int(input())
    villagers = (0, ) + tuple(map(int, input().rstrip().split()))
    edges = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = map(int, input().rstrip().split())
        edges[a].append(b)
        edges[b].append(a)
    
    get_great_village_cnt(N, villagers, edges)

sol()

    