"""
dp를 활용해 해당 문자로 마치는 경로가 얼만큼 있는지 저장한다.
35480	3004

dp를 갱신하지 않고
dp에 target 인덱스 정보도 저장했을때 메모리 사용량이 거의 2.5배 더 들어서 이전 풀이로 돌아갔다.
84032	3460

탐색에서 한 방향으로 K만큼 밀고가다가 범위를 벗어나면 break하도록 for문을 변경했다.
35480	2720

dp + dfs로 풀었을 때, 첫 문자에 대해 시작하면, 시간초과가 나고 맨 끝 부터 시작하면 안나는 것 같다.
처음부터 시작했을 때 풀이를 그대로 맨 끝 부터 시작하도록 변경했는데 시간이 1/40났다.
기존 제일 낮은 시간 가진 사람의 풀이랑 비교하면, dp[x][y][index], dp[index][x][y] 차이가 
나는데, 캐싱이 전자가 더 잘되나보다.
38992	68
"""

import sys
input = sys.stdin.readline

def get_path_count(N, M, K, grids, target):
    A = ord("Z") - ord("A") + 1
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    alpha_index = lambda x: ord(x) - ord("A")

    dp = [[1] * M for _ in range(N)]

    alphabet_pos = [[] for _ in range(A)]
    for i in range(N):
        for j in range(M):
            alphabet_pos[alpha_index(grids[i][j])].append((i, j))
    
    if len(target) == 1:
        return len(alphabet_pos[alpha_index(target[0])])

    for i, t2 in enumerate(target[1:]):
        t1 = target[i]
        new_dp = [[0] * M for _ in range(N)]
        for r, c in alphabet_pos[alpha_index(t2)]:
            for dr, dc in directions:
                nr, nc = r, c
                for _ in range(K):
                    nr += dr; nc += dc
                    if not (0 <= nr < N and 0 <= nc < M):
                        break
                    if grids[nr][nc] == t1:
                        new_dp[r][c] += dp[nr][nc]
        dp = new_dp

    last_char = alpha_index(target[-1])
    return sum(dp[r][c] for r, c in alphabet_pos[last_char])

def sol():
    N, M, K = map(int, input().split())
    grids = [list(input().strip()) for _ in range(N)]
    target = list(input().strip())

    print(get_path_count(N, M, K, grids, target))

sol()