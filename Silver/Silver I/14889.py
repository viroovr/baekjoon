def calculate_difference(matrix):
    # print(f"matrix : {matrix}")
    a_team, b_team = [], []
    for i in range(n):
        if matrix[i] == 1:
            a_team.append(i)
        elif matrix[i] == 2:
            b_team.append(i)
    a_sum, b_sum = 0, 0
    # print(f"a_team = {a_team}, b_team = {b_team}")
    for i in range(n // 2):
        for j in range(i + 1, n // 2):
            a_sum += statuses[a_team[i]][a_team[j]] + statuses[a_team[j]][a_team[i]]
            b_sum += statuses[b_team[i]][b_team[j]] + statuses[b_team[j]][b_team[i]]
    
    # print(f"a_sum = {a_sum}, b_sum = {b_sum}")
    return abs(a_sum - b_sum)

def get_min_diffrences(depth, matrix, two_sum):
    global min_value

    if depth == n:
        min_value = min(min_value, calculate_difference(matrix))
        return

    if two_sum[0] < n // 2:
        two_sum[0] += 1
        matrix[depth] = 1
        get_min_diffrences(depth + 1, matrix, two_sum)
        two_sum[0] -= 1

    if two_sum[1] < n // 2:
        two_sum[1] += 1
        matrix[depth] = 2
        get_min_diffrences(depth + 1, matrix, two_sum)
        two_sum[1] -= 1

def sol():
    global n, statuses, min_value
    n = int(input())
    statuses = [list(map(int, input().split())) for _ in range(n)]
    min_value = 100 * 20
    matrix = [0] * n
    get_min_diffrences(0, matrix, [0, 0])
    print(min_value)

if __name__ == "__main__":
    sol()
    