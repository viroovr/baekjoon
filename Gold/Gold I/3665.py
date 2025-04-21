"""
Khan's Algorithm을 활용해서 위상정렬을 했다.
그리고 처음에 주어지는 순위 정보가 N(N - 1) // 2개로 충분하므로 변경만 가할 경우
확실하지 않은 순위가 나올 수 없다.

확실하지 않은 순위가 있다는 것은 위상 정렬 과정에서 indegree가 0이 되는 것이 2개 이상있다는 것인데
이 말은 옳지만 문제에서 주어진 경우에는 존재할 수 없다.

IMPOSSIBLE이 아니면서 ?인 경우가 존재하려면 위상 정렬과정에서 1인 것이 2개 이상 그리고 2인 것이 2개이상
.. 있어야한다. 이 경우 전체 순위 정보에 비해 항상 작은 쌍이 필요하므로 이는 순서만 뒤집는 경우에 불가능하다.

따라서 ?인 경우는 존재하지 않는다.

리스트에서 순위 정보만 받아서 빠르게 해결한 방법도 있지만 이 방법으로 진행함

42924	408
"""

import sys
from collections import deque

input = sys.stdin.readline

def get_grade(N, graph, indegrees):
    q = deque()
    for i in range(1, N + 1):
        if indegrees[i] == 0:
            q.append(i)

    result = []

    while q:
        # if len(q) > 1:
        #     return "?"
        
        x = q.popleft()
        result.append(x)

        for nxt in graph[x]:
            indegrees[nxt] -= 1
            if indegrees[nxt] == 0:
                q.append(nxt)
    
    return " ".join(map(str, result)) if len(result) == N else "IMPOSSIBLE"


def sol():
    T = int(input())
    res = []

    for i in range(T):
        n = int(input())
        last_grade = list(map(int, input().rstrip().split()))
        m = int(input())
        
        graph = [set() for _ in range(n + 1)]
        indegrees = [0] * (n + 1)

        for i in range(n):
            f = last_grade[i]
            for j in range(i + 1, n):
                indegrees[last_grade[j]] += 1
                graph[f].add(last_grade[j])
        
        def change_grade(a, b):
            graph[a].remove(b)
            indegrees[b] -= 1
            graph[b].add(a)
            indegrees[a] += 1

        for _ in range(m):
            a, b = map(int, input().split())
            if b in graph[a]:
                change_grade(a, b)
            else:
                change_grade(b, a)

        res.append(get_grade(n, graph, indegrees))
    
    sys.stdout.write("\n".join(res)+"\n")

sol()