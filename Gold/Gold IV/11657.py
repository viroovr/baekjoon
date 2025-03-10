"""
음수 간선에 대해 최단 거리를 계산하는 알고리즘이 있었지 싶으면서 직접 생각해봤는데,
잘 안됐다. 음수 싸이클 여부 확인을 단순히 현재 비용이 음수인 상태에서 가려는 노드의 거리가 음수이면
참으로 되게 했는데 쉽게 반례를 생각할 수 있었다.
결국, 모르는 알고리즘을 사용하기에, gpt에게 물어봐서 bellman-ford 알고리즘을 확인했다.

최단 거리는 최대 n - 1개의 간선을 활용할 수 있음을 바탕으로, 최단거리를 갱신한다. 그리고 다시 한번
노드를 돌며, 갱신이 가능한지 확인하는데, 갱신이 가능하면 음수 사이클이게 된다.

1. 재갱신때, n - 1번 루프 제거, sol 제거
2. input = sys.stdin.readline
3. sys.stdout.write
4. INF = int(e9)
33432	592
33432	368 1
33432	252 1 2
33432	252 1,2,3
33432	244 1,2,3,4
"""
import sys
input = sys.stdin.readline

def get_min_cost(graph):
    INF = int(1e9)
    distance = [INF] * N
    distance[0] = 0
    for _ in range(N - 1):
        for node in range(N):
            if distance[node] == INF:
                continue
            for next_node, d in graph[node]:
                if distance[node] + d < distance[next_node]:
                    distance[next_node] = distance[node] + d
    
    for node in range(N):
        if distance[node] == INF:
            continue
        for next_node, d in graph[node]:
            if distance[node] + d < distance[next_node]:
                print(-1)
                return

    result = "\n".join([str(distance[i]) if distance[i] != INF else str(-1) for i in range(1, N)])
    sys.stdout.write(result)

f = lambda : map(int, input().split())
N, M = f()
graph = [[] for _ in range(N)]
for _ in range(M):
    A, B, C = f()
    graph[A - 1].append((B - 1, C))
get_min_cost(graph)
