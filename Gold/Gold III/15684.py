"""
if same + (current_expected_count - count) * 2 < n:
    return
🔹 성능 최적화 효과
이 조건이 없으면 백트래킹으로 인해 불필요한 경로까지 탐색해야 합니다.
하지만 이 조건이 있으면 정답이 나올 가능성이 없는 경우 바로 종료되므로 불필요한 재귀 호출을 막아 탐색 시간을 크게 줄일 수 있습니다.
특히, n이 크고, 가능한 사다리 수(h * (n-1))가 많을수록 이 조건의 효과는 더욱 커집니다.
즉, 불필요한 가지치기(pruning)를 수행하여 탐색 공간을 줄이는 중요한 역할을 합니다.
🔹 성능 비교 (추정)
해당 조건이 없는 경우:
모든 경우를 탐색하므로 시간 복잡도는 최대 O(Combinations(h * (n-1), 3))
해당 조건이 있는 경우:
의미 없는 탐색을 조기 종료하여 실제 탐색하는 경우가 급격히 줄어듦
백트래킹 성능이 대폭 개선됨 → 실제 실행 시간이 몇 배 이상 차이 날 가능성 큼
"""

def check_ladder():
    same = 0
    for i in range(n):
        cur = i
        for j in range(h):
            if ladders[j][cur] == 1:
                cur += 1
            elif ladders[j][cur] == -1:
                cur -= 1
        if cur == i:
            same += 1
    return same

def get_horizoni_result_i(count, current_expected_count):
    global min_val

    if min_val != -1:
        return
    same = check_ladder()
    if same + (current_expected_count - count) * 2 < n:
        return

    if count == current_expected_count:
        if same == n:
            # print("-----")
            # print(f"minval = {min_val}, count = {count}")
            # for i in range(h):
            #     print(*ladders[i])
            # print("-----")
            min_val = count
            return

    for i in range(h):
        for j in range(n - 1):
            if ladders[i][j] == 0 and ladders[i][j + 1] == 0:
                ladders[i][j], ladders[i][j + 1] = 1, -1
                get_horizoni_result_i(count + 1, current_expected_count)
                ladders[i][j], ladders[i][j + 1] = 0, 0

def sol():
    global n, m, h, min_val, ladders
    n, m, h = map(int, input().split())
    ladders = [[0] * n for _ in range(h)]
    min_val = -1

    for _ in range(m):
        a, b = map(int, input().split())
        ladders[a - 1][b - 1] = 1
        ladders[a - 1][b] = -1

    for i in range(4):
        get_horizoni_result_i(0, i)
        if min_val != -1:
            break

    print(min_val)

if __name__ == "__main__":
    sol()
