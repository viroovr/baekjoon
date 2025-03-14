"""
거리를 갱신할 때, 거리가 INF인경우 건너뛰어 연산량 감소
-> 시간초과
1. 캐시 효율성 문제
    - graph[i][k] == INF를 체크하는 과정에서 CPU의 브랜치 예측 실패(Branch Misprediction) 가 발생할 가능성이 있음.
    - 특히 행렬을 순회할 때 캐시 친화적인 접근 방식이 중요함.
2. INF 체크가 오히려 불필요한 반복문 호출을 유발
    - graph[i][k] == INF 체크가 빠른 종료를 도울 것 같지만, 실제로는 오히려 추가적인 조건 검사를 초래하여 실행 시간을 증가시킬 수 있음.
    - 플로이드-워셜은 모든 정점 쌍 간 거리를 갱신해야 하므로, 조건문을 추가하는 것이 오히려 불필요한 연산을 증가시킬 수 있음.

최단거리 싸이클을 찾는 것이기 때문에 자신한테 오는 거리값도 업데이트가 필요하다. 이를 0으로
기본 설정하지 않고, INF값으로 두어, 최단거리를 구하는 방식으로 변경했다.
37660	6204 graph[i][j] + graph[j][i] 값으로 갱신
37660	6560 graph[i][i]값으로 갱신
"""

import sys
input = sys.stdin.readline

def get_min_cycle(V, graph):
    for k in range(1, V + 1):
        for i in range(1, V + 1):
            for j in range(1, V + 1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    result = INF
    for i in range(1, V + 1):
        if graph[i][i] != INF:
            result = min(result, graph[i][i])
    
    print(result if result < INF else -1)

def sol():
    global INF
    INF = int(1e8)
    V, E = map(int, input().split())
    graph = [[INF] * (V + 1) for _ in range(V + 1)]
    for _ in range(E):
        a, b, c = map(int, input().split())
        graph[a][b] = c
    
    get_min_cycle(V, graph)

sol()