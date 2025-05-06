"""
기존의 1D 세그먼트 트리를 이용해서 풀었다. x축 세그먼트 트리를 y축 개수만큼 생성해서
x축에서의 구간합을 구하고, 반복문을 사용해 y축 수 만큼 연산 후 결과를 냈다.
하지만, 이는 시간초과가 발생한다. O(MNlogN) 이기 때문이다.

이를 검색을 통해 2D 세그먼트 트리가 있음을 알아냈다. 세그먼트 트리의 각 노드가 세그먼트
트리가 되는 것이다. 전체적인 세그먼트 트리는 x축을 range로 두고 노드의 세그먼트트리는 y축을
range로 둔다.

이는 O(M(logN)^2)으로 원하는 시간에 동작한다. 공간 복잡도는 O(N^2)이다.
하지만, 실제 실행시간은 더 느리다. 이를 개선한것이 Fenwick Tree로 구현이 간단하고
상수값이 작아 더 빠르다.

197136	4052
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(2**12)

def build_tree(N, numbers):
    size = 1
    while size < N:
        size <<= 1
    
    trees = [[0] * 2 * size for _ in range(2 * size)]

    for i in range(N):
        t, n = trees[size + i], numbers[i]
        for j in range(N):
            t[size + j] = n[j]
    
    for i in range(N):
        t = trees[size + i]
        for j in range(size - 1, 0, -1):
            t[j] = t[2 * j] + t[2 * j + 1]

    for i in range(size - 1, 0, -1):
        t = trees[i]
        for j in range(1, 2 * size):
            t[j] = trees[2 * i][j] + trees[2 * i + 1][j]
    
    return trees, size

def update_node(tree, y, value, size):
    cur = size + y
    tree[cur] = value
    while cur > 1:
        cur //= 2
        tree[cur] = tree[2 * cur] + tree[2 * cur + 1]

def update(trees, x, y, value, size):
    x += size
    y += size
    trees[x][y] = value

    ty = y
    while ty > 1:
        ty //= 2
        trees[x][ty] = trees[x][2 * ty] + trees[x][2 * ty + 1]
    
    tx = x
    while tx > 1:
        tx //= 2
        ty = y
        while ty >= 1:
            trees[tx][ty] = trees[2 * tx][ty] + trees[2 * tx + 1][ty]
            ty //= 2

def get_node_sum(tree, ly, ry, size):
    res = 0
    left = size + ly
    right = size + ry
    while left <= right:
        if left % 2 == 1:
            res += tree[left]
            left += 1
        if right % 2 == 0:
            res += tree[right]
            right -= 1
        left //= 2
        right //= 2
    return res

def get_sum(trees, lx, ly, rx, ry, size):
    res = 0
    left = size + lx
    right = size + rx
    while left <= right:
        if left % 2 == 1:
            res += get_node_sum(trees[left], ly, ry, size)
            left += 1
        if right % 2 == 0:
            res += get_node_sum(trees[right], ly, ry, size)
            right -= 1
        
        left //= 2
        right //= 2

    return res

def sol():
    global N
    N, M = map(int, input().split())
    trees, size = build_tree(N, [list(map(int, input().split())) for _ in range(N)])
    for _ in range(M):
        q = list(map(int, input().split()))
        if q[0] == 1:
            print(get_sum(trees, q[1] - 1, q[2] - 1, q[3] - 1, q[4] - 1, size))
        else:
            update(trees, q[1] - 1, q[2] - 1, q[3], size)

sol()