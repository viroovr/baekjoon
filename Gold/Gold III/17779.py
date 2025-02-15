"""
개선된 점
1. 범위 최적화
    - x의 최대값을 N-2, y의 범위를 2 ~ N-1로 조정.
2. 리스트 인덱싱 최적화
    - row = A[r-1]로 행을 미리 저장하여 A[r-1][c-1] 접근을 최적화.
3. 조건문 구조 개선
    - 불필요한 논리 연산 제거 및 continue를 사용해 불필요한 반복을 줄임.
    - 불필요한 (1 <= x and ...) 조건 제거.
메모리  시간    개선점 유무
32412	1144    
32412	920     3
32412	824     2, 3
32412	824     1, 2, 3
"""
def calc_difference(x, y, d1, d2):
    each_sum = [0] * 5
    for r in range(1, N + 1):
        row = A[r - 1]
        for c in range(1, N + 1):
            if (r < x + d1 and c <= y and c < -(r - x) + y):
                each_sum[0] += row[c - 1]
            elif (r <= x + d2 and y < c and c > (r - x) + y):
                each_sum[1] += row[c - 1]
            elif (x + d1 <= r and c < y - d1 + d2 and c < r - (x + d1) + (y - d1)):
                each_sum[2] += row[c - 1]
            elif (x + d2 < r and y - d1 + d2 <= c and c > -r + (x + d2) + (y + d2)):
                each_sum[3] += row[c - 1]
            else:
                each_sum[4] += row[c - 1]
    return max(each_sum) - min(each_sum)

def sol():
    global N, A
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    min_value = 100 * 20 * 20
    for x in range(1, N - 1):
        for y in range(2, N):
            for d1 in range(1, N):
                for d2 in range(1, N):
                    if x + d1 + d2 > N or 1 > y - d1 or y + d2 > N:
                        continue
                    min_value = min(calc_difference(x, y, d1, d2), min_value)

    print(min_value)
sol()