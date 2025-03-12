"""
다익스트라를 활용하면 O(n * (n + m)logn) 이므로 10^8을 넘기게 된다. 따라서 n이 적은 O(n^3)인 플로이드-워셜
알고리즘을 사용한다. 이는 dp방법으로 최소 거리를 경유하거나 직접 가거나를 모두 비교하여 최솟값을 갱신한다.
	33432	2612
    33432	232 input=sys.stdin.readline
"""

import sys
input = sys.stdin.readline

def sol():
    INF = int(1e8)
    n = int(input())
    m = int(input())
    distance = [[INF] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int ,input().split())
        distance[a][b] = min(distance[a][b], c)

    for i in range(1, n + 1):
        distance[i][i] = 0
    
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if distance[i][j] == INF:
                print(0, end=" ")
            else:
                print(distance[i][j], end=" ")
        print()

sol()