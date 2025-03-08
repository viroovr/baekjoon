"""
방문한 곳과 거리가 일치하는 곳도 처리하는 로직을 짜느라, 시간이 더 소모됐다.
알아보니, s -> g -> h -> x 또는 s -> h -> g -> x 이 경로 중에서 s -> x 최단거리와 일치하는 게 있으면
유효한 루트였다. 곧, s -> x, g -> x, h -> x 세 개의 다익스트라를 구한 뒤 적절히 처리하면 된다.
처음에는 s -> g -> x, s -> h -> x 이 중 최솟값이 s -> x와 같은 지를 찾는 문제인줄 알았다.
하지만 그게 아니라, s -> x로 갈건데, 그 중, h, g경로를 지나는 최단거리를 구하는 문제였다.
처음 아이디어에서 더 파고들었으면 빠르게 풀었을 텐데 아쉽다.
루트를 저장해야 한다는 생각에 사로잡힌 것 같다.

1. 시간 복잡도 감소
    O((V + E) log V)의 다익스트라 알고리즘을 유지하면서, 불필요한 비교 연산을 줄였습니다.
    map(), sorted(), filter()의 활용으로 리스트 내 연산을 줄여 Python의 내부 최적화를 활용할 수 있습니다.
2. 가독성 향상
    is_crossed() 함수를 제거하고 바로 조건문을 사용하여 직관성을 높였습니다.
    sorted(filter(lambda c: check_cross[c], destination_candidates))로 목적지를 더 효율적으로 추려냅니다.
3. 불필요한 연산 제거
    check_cross[i] = False를 불필요하게 초기화하는 부분을 제거했습니다.

49016	248
46772	252 is_crossed() 함수
46772	260 1,2,3
"""
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def get_destiantions(s, g, h, destination_candidates):
    INF = float("inf")
    distances = [INF] * (n + 1)
    check_cross = [False] * (n + 1)

    q = [(0, s)]
    distances[s] = 0

    while q:
        cost, node = heappop(q)
        
        for i, d in roads[node]:
            new_cost = cost + d
            if new_cost > distances[i]:
                continue

            is_via_cross = (node == g and i == h) or (node == h and i == g)

            if new_cost < distances[i]:
                distances[i] = new_cost
                check_cross[i] = check_cross[node] or is_via_cross
                heappush(q, (new_cost, i))
            elif new_cost == distances[i] and (check_cross[node] or is_via_cross):
                check_cross[i] = True

    return " ".join(map(str, sorted(filter(lambda c: check_cross[c], destination_candidates))))

f = lambda: map(int, input().split())
for _ in range(int(input())):
    n, m, t = f()
    s, g, h = f()
    roads = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, d = f()
        roads[a].append((b, d))
        roads[b].append((a, d))

    destination_candidates = [int(input()) for _ in range(t)]

    print(get_destiantions(s, g, h, destination_candidates))

