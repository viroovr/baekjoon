"""
각 노드에서 다른 노드까지의 거리 리스트를 min heap으로 유지하며 최솟값을 찾았지만,
visite와 최솟값 dp 갱신을 따로 두어 최솟값만 유지되도록 dp를 유지할 수도 있다.
그리고 각 노드로 가는 길이를 생각하는게 아니라 각 노드에서 들어오는 길이중에 최솟값을
dp에 저장한다고 생각해야한다.
이경우가 더 빠름
39784	72  heapq
34536	36  dp

"""
from math import dist as calc_distance

def get_min_cost(N, stars):
    INF = int(1e4)

    distance = [INF] * N
    distance[0] = 0
    visited = [False] * N
    cost = 0

    for _ in range(N):
        min_cost, cur_node, min_node = INF, -1, -1
        for i in range(N):
            if not visited[i] and min_cost > distance[i]:
                min_node = i
                min_cost = distance[i]

        visited[min_node] = True
        cost += min_cost

        for i in range(N):
            if not visited[i]:
                dist = calc_distance(stars[min_node], stars[i])
                if dist < distance[i]:
                    distance[i] = dist

    return f"{cost:.2f}"
                
def sol():
    n = int(input())
    stars = [tuple(map(float, input().split())) for _ in range(n)]
    print(get_min_cost(n, stars))

sol()