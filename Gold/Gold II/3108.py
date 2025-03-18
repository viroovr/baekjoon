"""
group_id로 변들을 설정하고, 현재 group_id가 지정된 포인트를 만나면 pu를
상승시킨 뒤, 변에 현재 groupId로 갱신하도록 처음에 구상했다.
하지만 이러면 직사각형이 주어지는 순서에따라, pu값이 제대로 반영되지 않는 문제가 있었고,
원래 group_id값을 가지지 못하도록 직사각형 group_id가 전부 변경되어도 실패하는 문제가있다.

따라서 연결되는 직사각형들을 같은 집합에 속하도록 해줘야 하며. 이를
parent깊이가 1정도 되는 생각하는 반례까지만 되게끔 코드를 짰더니 계속 틀렸다.

union_find 를 적용시켜 rank를 효율적으로 병합하며 union이 가능하도록 코드를 변경했다.
40356	80
"""

def get_PU_min(N, recs, M):
    start_x, start_y = M, M
    R = 2 * M + 1

    parent = [i for i in range(N)]
    rank = [1] * N

    def find_parent(i):
        if parent[i] != i:
            parent[i] = find_parent(parent[i])
        return parent[i]

    def union_find(a, b):
        parent_a = find_parent(a)
        parent_b = find_parent(b)

        if parent_a == parent_b:
            return

        if rank[parent_a] > rank[parent_b]:
            parent[parent_b] = parent_a
        elif rank[parent_a] < rank[parent_b]:
            parent[parent_a] = parent_b
        else:
            parent[parent_b] = parent_a
            rank[parent_a] += 1

    grids = [[-1] * R for _ in range(R)]
    for group_id, (x1, y1, x2, y2) in enumerate(recs):
        neighbor = set()
        for y in range(y1, y2 + 1):
            for x in [x1, x2]:
                if grids[y][x] != -1:
                    neighbor.add(grids[y][x])
                grids[y][x] = group_id
        for x in range(x1 + 1, x2):
            for y in [y1, y2]:
                if grids[y][x] != -1:
                    neighbor.add(grids[y][x])
                grids[y][x] = group_id
        
        if neighbor:
            for k in neighbor:
                union_find(k, group_id)
        
    pu = len(set(find_parent(i) for i in range(N)))
    print(pu if grids[start_y][start_x] == -1 else pu - 1)

def sol():
    N = int(input())
    M = 500
    recs = [tuple(map(lambda x: int(x) + M, input().split())) for _ in range(N)]

    get_PU_min(N, recs, M)

sol()