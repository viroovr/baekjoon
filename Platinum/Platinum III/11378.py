"""
처음에는 Edmonds-Karp 방법을 사용해서 풀이했다.
BFS를 통해 최단경로를 탐색하면서 O(VE^2)의 시간복잡도를 가진다.
직원과 일의 개수가 최대 1000일 때, E가 최대 10^6개가 가능하기 되므로 시간초과가 발생한다.

두 번째로 Ford-Fulkerson 방법을 사용했다.
-   DFS를 통해 유량이 남아있는 경로를 탐색하면서 O(Ef)의 시간복잡도를 가진다. (f는 최대 유량)
-   하지만, SOURCE에서 직원 노드로의 capacity를 K + 1로 설정했는데,
    이는 벌점을 고려하지 않고 기본적으로 K + 1개의 일을 할 수 있는 구조가 되어 오류가 발생했다.
-   올바른 방법은, super worker노드를 두어 추가적인 매칭을 담당하도록 설계하는 것이다.
177740	6744

세 번째로, 이분 매칭을 사용했다.
-   기본 매칭을 먼저 진행하고, 이후 벌점을 사용할 때마다 DFS탐색을 반복했다.
-   벌점의 총합 K만큼 반복 시도하여 최대로 매칭을 늘렸다.
-   이분 매칭의 시간복잡도는 O(VE)이며, 최적의 성능을 보인다.
42376	112

여기서 의문은 Ford-Fulkerson과 이분 매칭의 시간복잡도는 동일한데, 왜 시간 차이가 날까이다.
그 이유는, Ford-Fulkerson의 DFS는 무작위적인 경로를 탐색하기 때문이고 이분 매칭은
탐색할 수 있는 간선만 매칭하기 때문이다.

결과적으로 이분매칭이 가장 효율적이었다.

"""
import sys
sys.setrecursionlimit(int(1e7))
input = sys.stdin.readline

def dfs(employee, visited):
    if visited[employee]:
        return False

    visited[employee] = True
    for task in work_list[employee]:
        if not task_assignment[task]:
            task_assignment[task] = employee
            return True
    
    for task in work_list[employee]:
        if not visited[task_assignment[task]] and dfs(task_assignment[task], visited):
            task_assignment[task] = employee
            return True
    return False

N, M, K = map(int, input().split())
work_list = [[] for _ in range(N + 1)]

for i in range(1, N + 1):
    tasks = list(map(int, input().rstrip().split()))[1:]
    work_list[i].extend(tasks)

task_assignment = [0] * (M + 1)

max_match = 0
for employee in range(1, N + 1):
    visited = [False] * (N + 1)
    if dfs(employee, visited):
        max_match += 1
        if max_match == M:
            break

if max_match == M: print(M); sys.exit(0)

for employee in range(1, N + 1):
    if K==0 or max_match==M: break
    while K > 0:
        visited = [False] * (N + 1)
        if dfs(employee, visited):
            max_match += 1
            K -= 1
        else:
            break
print(max_match)