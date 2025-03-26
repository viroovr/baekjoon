"""
union find를 활용한 분리집합 문제.
parent는 해당 노드의 1깊이의 부모가 아니라 제일 끝 root 조상을 가리키도록 해야
경로 압축이 된다.

이 외에도 rank를 없애고, 음수의 절댓값이 rank로 양수일때는 root를 가리키도록 해서 rank를 없앨수도 있다.
94324	240
94324	236 parent[a] 가 a의 루트 노드
"""

import sys
def find_parent(a):
    if parent[a] != a:
        parent[a] = find_parent(parent[a])
        return parent[a]
    return parent[a]

def union(a, b):
    parent_a = find_parent(a)
    parent_b = find_parent(b)

    if rank[parent_a] == rank[parent_b]:
        parent[parent_b] = parent_a
        rank[parent_a] += 1
    elif rank[parent_a] > rank[parent_b]:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b

def is_union(a, b):
    return find_parent(a) == find_parent(b)

def sol():
    global parent, rank
    data = sys.stdin.read().split()
    idx = 0
    N, M = int(data[idx]), int(data[idx + 1])
    idx += 2

    parent = [i for i in range(N + 1)]
    rank = [1] * (N + 1)

    result = []
    for _ in range(M):
        a, b = int(data[idx + 1]), int(data[idx + 2])
        if data[idx] == "1":
            result.append("YES" if is_union(a, b) else "NO")
        else:
            union(a, b)
        idx += 3
    
    sys.stdout.write("\n".join(result)+"\n")

sol()