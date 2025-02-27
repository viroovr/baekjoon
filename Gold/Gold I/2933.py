"""
행이 아닌 열의 맨아래 부분이 닿아야 하는 부분을 간과했는데 제출했을 때 맞았다. 이부분에대한 테스트케이스가
없는 것 같다.
그래서 다시 열에 아래부분이 닿으면 종료되도록 고치는과정에서 4시간 정도 더 소요됐다.
나눠진 두개의 cluster1, cluste2 에대해
1. cluster 1이 바닥에 처음부터 닿아있는가? 
2. cluster 2가 바닥에 처음부터 닿아있는가? 
3. cluster1 또는 cluster2가 떨어지다가 다른 cluster에 부딪혔는가?
    0. 다른 cluster에 부딪혔다면 해당 cluster는 그 cluster와 union 해야한다.
    1. 다른 cluster란 나눠진 cluster1 또는 cluster2 중 하나인가? 아니면 두개 외에 나머지인가?
    2. 새롭게 업데이트하기 위한 clusters의 조건.
4. 부딪히는 cluster없이 바닥에 부딪히는가?
이러한 조건들을 고려해서 순서를 정하고 clusters를 갱신하는 과정에서 머리가 터져버렸다.
"""

from collections import deque, defaultdict
directions = [(-1, 0), (0, 1), (0, -1), (1, 0)]
def throw_stick(caves, height, left):
    if left == 1:
        for c in range(C):
            if caves[height][c] == 'x':
                caves[height][c] = '.'
                return height, c
    else:
        for c in range(C - 1, -1, -1):
            if caves[height][c] == 'x':
                caves[height][c] = '.'
                return height, c
    return None, None

def bfs_cluster(caves, start_r, start_c, visited):
    queue = deque([(start_r, start_c)])
    cluster = set([(start_r, start_c)])
    visited[start_r][start_c] = True
    
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and caves[nr][nc] == 'x':
                visited[nr][nc] = True
                queue.append((nr, nc))
                cluster.add((nr, nc))

    return cluster

def make_cluster(caves):
    clusters = []
    visited = [[False] * C for _ in range(R)]
    
    for r in range(R):
        for c in range(C):
            if caves[r][c] == 'x' and not visited[r][c]:
                clusters.append(bfs_cluster(caves, r, c, visited))

    return clusters


def find_bottom_minerals(cluster, caves):
    bottom_minerals = defaultdict(list)
    for r, c in cluster:
        if r + 1 >= R:
            return None, True
        elif r + 1 < R and caves[r + 1][c] == ".":
            bottom_minerals[r].append(c)
    return bottom_minerals, False

def cluster_gravity(cluster, clusters, caves, bottom_minerals):
    move_distance = 1
    while True:
        bottom = False
        for r, c_list in bottom_minerals.items():
            for c in c_list:
                nr = r + move_distance + 1
                if nr >= R:
                    bottom = True
                    continue
                if caves[nr][c] == 'x' and (nr, c) not in cluster:
                    for cr, cc in sorted(cluster, reverse=True):
                        caves[cr][cc] = '.'
                        caves[cr + move_distance][cc] = 'x'
                    n_cluster = set((cr + move_distance, cc) for cr, cc in cluster)
                    for cl in clusters:
                        if (nr, c) in cl:
                            cl.update(n_cluster)
                            return
        if bottom:
            for r, c in sorted(cluster, reverse=True):
                caves[r][c] = '.'
                caves[r + move_distance][c] = 'x'
            clusters.append(set((r + move_distance, c) for r, c in cluster))
            return
        move_distance += 1

def process_throw(caves, h, left, clusters):
    r, c = throw_stick(caves, h, left)
    if r is None:
        return

    visited = [[False] * C for _ in range(R)]
    origin_cluster = None
    cluster1, cluster2 = None, None

    for cluster in clusters:
        if (r, c) in cluster:
            cluster.remove((r, c))
            origin_cluster = cluster
            clusters.remove(cluster)
            break
    
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0<=nr<R and 0<=nc<C and caves[nr][nc] == "x":
            cluster1 = bfs_cluster(caves, nr, nc, visited)
            cluster2 = origin_cluster - cluster1 if origin_cluster else None
            break

    bottom1, bottom2 = None, None
    if cluster1:
        bottom_minerals1, bottom1 = find_bottom_minerals(cluster1, caves)
    if cluster2:
        bottom_minerals2, bottom2 = find_bottom_minerals(cluster2, caves)
    if bottom1:
        clusters.append(cluster1)
    if bottom2:
        clusters.append(cluster2)
    if cluster1 and not bottom1:
        cluster_gravity(cluster1, clusters, caves, bottom_minerals1)
    if cluster2 and not bottom2:
        cluster_gravity(cluster2, clusters, caves, bottom_minerals2)

def get_minerals(caves, heights):
    clusters = make_cluster(caves)
    for i, h in enumerate(heights):
        left = -1 if i % 2 else 1
        process_throw(caves, R - h, left, clusters)

    for row in caves:
        print("".join(row))

def sol():
    global R, C
    R, C = map(int, input().split())
    caves = [list(input()) for _ in range(R)]
    N = int(input())
    heights = tuple(map(int, input().split()))
    get_minerals(caves, heights)

sol()

"""
반례모음
9 8
........
.xxxx...
.x......
.x.xxxx.
.x....x.
.x....x.
.xxxx.x.
....xxx.
......x.
1
2

3 8
...xxxxx
...xx...
...xx...
4
1 1 1 1

5 5
xxxxx
x....
xxxxx
x....
x....
10 
1 2 3 4 5 1 2 3 4 5

10 10
xxxxxxxxxx
....x.....
...xxx....
.....x....
....xx....
.....x....
xxxxxx....
..x.......
.xxxx.....
...xxxxxxx
10 
9 8 7 6 5 4 3 2 1 1

3 3
...
..x
x.x
2
1 1

4 4
...x
..xx
xx.x
x..x
2 
1 1

4 4
...x
..xx
.xxx
xxxx
10
1 2 3 4 1 2 3 4 3 4
"""