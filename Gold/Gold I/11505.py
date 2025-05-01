"""
재귀함수에서 조건 분기가 많은것도 시간초과에 원인이 됨을 알았다.

tree자료 구조를 만들때, iterative하게도 가능하다.

123688	1096
"""
import sys
from math import log2, ceil
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def build_tree(start, end, cur):
    if start == end:
        tree[cur] = numbers[start]
        return tree[cur]
    mid = (start + end) // 2
    left = build_tree(start, mid, 2 * cur)
    right = build_tree(mid + 1, end, 2 * cur + 1)
    tree[cur] = (left * right) % DIV
    return tree[cur]

def change_number(start, end, cur, b, c):
    if b < start or end < b:
        return tree[cur]
    
    if start == end:
        tree[cur] = c
        return tree[cur]
    mid = (start + end) // 2
    left = change_number(start, mid, 2 * cur, b, c)
    right = change_number(mid + 1, end, 2 * cur + 1, b, c)
    tree[cur] = (left * right) % DIV
    return tree[cur]

def get_mul(start, end, cur, b, c):
    if c < start or end < b:
        return 1
    if b <= start and end <= c:
        return tree[cur]
    
    mid = (start + end) // 2
    left = get_mul(start, mid, 2 * cur, b, c)
    right = get_mul(mid + 1, end, 2 * cur + 1, b, c)
    return (left * right) % DIV

def sol():
    global tree, numbers, DIV
    N, M, K = map(int, input().split())
    numbers = [int(input()) for _ in range(N)]
    tree = [1] * (2 ** (ceil(log2(N)) + 1))
    DIV = 1_000_000_007
    build_tree(0, N - 1, 1)
    for _ in range(M + K):
        a, b, c = map(int, input().split())
        if a == 1:
            change_number(0, N - 1, 1, b - 1, c)
        else:
            print(get_mul(0, N - 1, 1, b - 1, c - 1))

sol()