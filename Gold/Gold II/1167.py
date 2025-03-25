"""
3시간 반동안 생각해봤지만, 뭔가 익숙한 알고리즘 코딩에 습관이 있어서 거의 근접해
갔는데 결국 떠올리지 못했다.

여태 경로, 최단거리를 구하는 문제 푸는 방식 관념을 버려야 했던 문제.
그리고, tree 구조는 이전 parent 부분이 있어야 시간, 공간 복잡도, 코드 단순화에 기여함을 알았다.

dfs는 함수 스택이 쌓이는 걸로 푸는건데, 항상 bfs보다 나은 점이 없기에 사용 빈도가 낮았었다.
이제는 dfs + backtracking으로 풀어야 하는 문제를 맞닥뜨린것.

해답 아이디어에 거의 근접했는데, 이게 전체 케이스를 커버가능한지를 따지는게 참 어려운것 같다.
즉, 증명이.

96936	364
"""

import sys
sys.setrecursionlimit(10 ** 6)
                
def get_tree_width(V, graph):
    # for row in graph:
    #     print(*row)

    max_dist = 0

    def dfs(start, parent):
        nonlocal max_dist

        top1, top2 = 0, 0

        for node, weight in graph[start]:
            if node == parent:
                continue
            
            sub_tree_sum = dfs(node, start) + weight

            if top1 < sub_tree_sum:
                top2 = top1
                top1 = sub_tree_sum
            elif top2 < sub_tree_sum:
                top2 = sub_tree_sum

        max_dist = max(max_dist, top1 + top2)

        return top1

    dfs(1, -1)

    print(max_dist)

def sol():
    data = sys.stdin.read().rstrip().split("\n")

    V = int(data[0])

    graph = [[] for _ in range(V + 1)]

    for i in range(1, V + 1):
        line = tuple(map(int, data[i].split()))
        start = line[0]
        j = 1
        while line[j] != -1:
            graph[start].append((line[j], line[j + 1])) 
            j += 2
        graph[start].sort(key = lambda x: -x[1])

    get_tree_width(V, graph)

sol()
    
    