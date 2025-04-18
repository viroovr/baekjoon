"""
Trie 자료구조를 배우는 문제.
정석적으로도 dictionary 형태이다.

33432	56
"""

import sys
input = sys.stdin.readline

def get_tree(N, infos):
    tree = {}
    for info in infos:
        depth = tree.setdefault(info[0], {})
        for j in range(1, len(info)):
            depth = depth.setdefault(info[j], {})

    def dfs(tree, depth):
        for next_node in sorted(tree.keys()):
            print(f"{'--' * depth}{next_node}")
            dfs(tree[next_node], depth + 1)

    dfs(tree, 0)

def sol():
    N = int(input())
    info = [input().rstrip().split()[1:] for _ in range(N)]

    get_tree(N, info)

sol()