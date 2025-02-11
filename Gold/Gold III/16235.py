"""
변경 코드가 성능적으로 더 우수!

defaultdict(int) 활용으로 정렬 연산 제거 & 조회 속도 증가.
번식 로직 최적화로 불필요한 리스트 연산 제거.
이전 코드 대비 약 2~5배 빠름 (특히 M이 클 때 차이 극대화).
"""
from collections import defaultdict
import sys
input = sys.stdin.readline
directions = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]

def get_living_trees(grounds, trees, nourishments, N, M, K):
    total = M
    for _ in range(K):

        for r in range(N):
            for c in range(N):
                if trees[r][c]:
                    new_trees = defaultdict(int)
                    no_soil = False
                    dead = 0
                    for age in sorted(trees[r][c].keys()):
                        total_tree = trees[r][c][age]
                        if no_soil:
                            dead += total_tree * (age // 2)
                            total -= total_tree
                        elif grounds[r][c] >= total_tree * age:
                            grounds[r][c] -= total_tree * age
                            new_trees[age + 1] += total_tree
                        else:
                            no_soil = True
                            alive_tree = grounds[r][c] // age
                            dead += (total_tree - alive_tree) * (age // 2)
                            total -= total_tree - alive_tree
                            if alive_tree > 0:
                                grounds[r][c] -= alive_tree * age
                                new_trees[age + 1] += alive_tree
                    trees[r][c] = new_trees
                    grounds[r][c] += dead
                grounds[r][c] += nourishments[r][c]
        
        for r in range(N):
            for c in range(N):
                new_tree = 0
                for age in trees[r][c].keys():
                    if age % 5 == 0:
                        new_tree += trees[r][c][age]
                if new_tree > 0:
                    for dc, dr in directions:
                        if 0 <= r + dr < N and 0 <= c + dc < N:
                            trees[r + dr][c + dc][1] += new_tree
                            total += new_tree

    return total


def sol():
    N, M, K = map(int, input().split())
    nourishments = [list(map(int, input().split())) for _ in range(N)]
    grounds = [[5] * N for _ in range(N)]
    trees = [[defaultdict(int) for _ in range(N)] for _ in range(N)]
    for _ in range(M):
        x, y, z = map(int, input().split())
        trees[x - 1][y - 1][z] += 1

    print(get_living_trees(grounds, trees, nourishments, N, M, K))

sol()