"""
dfs로 구현했다가, seg fault떠서 bfs로 재작성했다.
bfs 큐가 함수 스택보다 크기가 작은걸 이용하고 중복 조건을 breadth단위로
처리하며 더 효율적으로 중복을 제거한다.

53968	388
"""

from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def is_same_count(A, B, C):
    total = A + B + C
    if total % 3 != 0:
        return 0

    li = tuple(sorted([A, B, C]))
    visited = defaultdict(bool)

    q = deque([li])
    visited[li] = True

    while q:
        x, y, z = q.popleft()
        if x == y == z:
            return 1
        
        for new_x, new_y, new_z in [(x + x, y - x, z), (x + x, y, z - x), (x, y + y, z - y)]:
            if new_y == 0 or new_z == 0:
                continue

            new_state = tuple(sorted([new_x, new_y, new_z]))
            if not visited[new_state]:
                q.append(new_state)
                visited[new_state] = True
    return 0

def sol():
    A, B, C = map(int, input().strip().split())
    print(is_same_count(A, B, C))

sol()