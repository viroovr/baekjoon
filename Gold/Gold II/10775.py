"""
처음에는, dp list에 오름차순이 유지되게 해서 binary search로 인덱스값 찾고
해당 값과 비교하여 넣을 수 있는지 없는지를 비교했다. 
하지만 넣는 방법이 O(n)이 걸려 결국 O(n^2)이 되어 시간초과가 발생했다.

다양하게 시도하는데, 질문게시판에, bruteforth 최적화 방법을 알려줘서 해봤는데
시간초과나고 생각해보면 잘못된 풀이임을 알수 있었다.

greedy 라는 방법을 생각도 못했고 union-find를 쓰는건지도 몰랐다.
parent, rank에 대한 고정관념을 깨고, greedy방법에 대해서도 숙고해봐야겠다.
41144	124
"""

import sys
input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    root_a, root_b = find(a), find(b)
    parent[root_a] = root_b

def get_max_planes(G, P, g):
    global parent

    parent = list(range(G + 1))

    count = 0
    for a in g:
        docking_gate = find(a)
        print(parent, docking_gate)

        if docking_gate == 0:
            break

        union(docking_gate, docking_gate - 1)
        count += 1
    return count

def sol():
    G = int(input())
    P = int(input())
    g = [int(input()) for _ in range(P)]
    print(get_max_planes(G, P, g))

sol()