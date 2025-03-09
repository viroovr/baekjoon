"""
처음에, 다익스트라로 최솟값과 최댓값을 우선순위 큐에 넣으면서, 방문하는 곳과 최소, 최대값 비교해
차이가 최소이도록 distance를 갱신해줬다.

하지만 이건, 경로마다 최솟값이 그 이후에 최솟값을 보장해주지 못하기 때문에, 어떻게 보면 그리디로 풀 수 없다.

조건에서 배열의 각 수가 0과 200사이라 했을 때, 왜 적은 범위일까. 를 적극 활용했으면 힌트를 얻을 수 있었게지만,
예측하지 못했다.

배열의 수가 0과 200사이이므로, 경로의 숫자가 브루트 포스하게 정해진 범위내에 있는지 탐색이 가능해보인다.
0,1, 0,2, ... 해당 경우에 200^2의 시간복잡도와 더불어, bfs로 탐색해야하기 때문에 100^2 총 4억번의 연산이 필요하다.

하지만 이분 탐색을 이용하면, log200 * 100^2 ~= 80000번이면 가능하다.
35004	428
"""

from collections import deque

directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
def bfs(n, arr, min_val, max_val):
    if not ((min_val <= arr[0][0] <= max_val) and (min_val <= arr[-1][-1] <= max_val)):
        return False
    visited = [[False] * n for _ in range(n)]
    q = deque([(0, 0)])
    visited[0][0] = True

    while q:
        r, c = q.popleft()
        if (r, c) == (n - 1, n - 1):
            return True
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and min_val <= arr[nr][nc] <= max_val:
                q.append((nr, nc))
                visited[nr][nc] = True

    return False

def get_min_diff(n, arr):
    min_val, max_val = min(map(min, arr)), max(map(max, arr))
    result = max_val - min_val

    left, right = 0, result
    while left <= right:
        mid = (left + right) // 2
        for min_v in range(min_val, max_val - mid + 1):
            max_v = min_v + mid
            if bfs(n, arr, min_v, max_v):
                result = mid
                right = mid - 1
                break
        else:
            left = mid + 1
    
    print(result)

def sol():
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    get_min_diff(n, arr)

sol()